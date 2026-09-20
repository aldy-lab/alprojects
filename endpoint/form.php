<?php
/* ============================================================
   ALPROJECTS — form endpoint
   ============================================================
   One file. Accepts the three forms on alprojects.co, emails the submission
   to the office with its attachments, answers the browser with JSON.

   Why a mailbox and not a database: the enquiries and applications already go
   to info@ and are worked from there. Storing them a second time would create
   a second copy to secure, to find on a subject-access request, and to delete
   after 24 months -- for no benefit. Nothing is written to disk by this file.

   ---- INSTALL ----------------------------------------------------------
   1. Upload to the company's own hosting, anywhere PHP runs. NOT into the
      alprojects.co repository: GitHub Pages serves files, it does not execute
      them, and a .php committed there would be downloaded as text.
   2. Set MAILTO and MAILFROM below. There is no shared secret and no API key:
      this file is committed to a public repository and read by anyone, so it
      must never hold one. What keeps it from being useful to a stranger is the
      origin check, the honeypot and the throttle -- and the fact that the worst
      it can do is email the office.
   3. Put the three URLs in js/main.js:
        CAREERS_ENDPOINT = "https://<host>/form.php?f=careers"
        CONTACT_ENDPOINT = "https://<host>/form.php?f=contact"
        FORM_ENDPOINT    = "https://<host>/form.php?f=subscribe"
      and PROCESSOR_NAME = "" so the privacy policy names <host> itself.
   4. Send one real submission from each form, with an attachment.

   ---- WHAT IT REFUSES --------------------------------------------------
   Anything not a POST from an allowed origin; a filled honeypot; more than
   MAX_FILES files or MAX_BYTES total; an extension not on the list; a body
   over PHP's own limits (check post_max_size and upload_max_filesize on the
   host -- the form offers 10 MB per file and the default post_max_size of 8M
   would reject a single CV, silently, with an empty $_POST).
   ============================================================
   PHP 7.4 syntax deliberately: no match, no never, no str_starts_with. Shared
   hosting runs a version or two behind, and a parse error here is a blank 500
   with nothing in it to read.
   ============================================================ */

// ------------------------------------------------------------------ config
const MAILTO        = 'info@alprojects.eu';
const MAILFROM      = 'website@alprojects.eu';   // must be a domain you can send as
const ALLOWED_ORIGIN = ['https://alprojects.co', 'https://www.alprojects.co'];
const MAX_FILES     = 6;
const MAX_BYTES     = 25 * 1024 * 1024;          // total, all attachments
const ALLOWED_EXT   = ['pdf','doc','docx','jpg','jpeg','png','webp','heic',
                       'dwg','dxf','step','stp','igs','iges','zip','txt'];
// A minute between submissions from one address. Not security -- it only
// blunts a script hammering the form; the honeypot does the rest.
const THROTTLE_SEC  = 60;

// ------------------------------------------------------------------ helpers
function json_out($code, array $body) {
    http_response_code($code);
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

/* Anything that reaches a mail header has to lose newlines first, or a value
   like "Name\r\nBcc: someone" adds a recipient. Applies to the subject and to
   every address, and it is the reason nothing from the form is ever used as a
   header without passing through here. */
function header_safe($s) {
    return trim(preg_replace('/[\r\n]+/', ' ', $s) ?? '');
}

function client_ip() {
    return (string)($_SERVER['REMOTE_ADDR'] ?? '0.0.0.0');
}

// ------------------------------------------------------------------ CORS
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if (in_array($origin, ALLOWED_ORIGIN, true)) {
    header('Access-Control-Allow-Origin: ' . $origin);
    header('Vary: Origin');
    header('Access-Control-Allow-Headers: Accept, Content-Type');
    header('Access-Control-Allow-Methods: POST, OPTIONS');
}
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') { http_response_code(204); exit; }
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    json_out(405, ['ok' => false, 'error' => 'method']);
}
/* A browser always sends Origin on a cross-origin POST. Refusing an unknown
   one keeps other sites from posting through this endpoint in a visitor's
   name; it is not a defence against a script, which can send any header it
   likes, and is not treated as one. */
if ($origin !== '' && !in_array($origin, ALLOWED_ORIGIN, true)) {
    json_out(403, ['ok' => false, 'error' => 'origin']);
}

// ------------------------------------------------------------------ throttle
$slot = sys_get_temp_dir() . '/alp-form-' . sha1(client_ip());
if (is_file($slot) && (time() - (int)filemtime($slot)) < THROTTLE_SEC) {
    json_out(429, ['ok' => false, 'error' => 'slow down']);
}
@touch($slot);

// ------------------------------------------------------------------ which form
$which = $_GET['f'] ?? 'contact';
$which = in_array($which, ['careers', 'contact', 'subscribe'], true) ? $which : 'contact';

/* The newsletter posts JSON; the other two post multipart because they carry
   files. Both shapes end up in $fields. */
$fields = [];
$ctype  = $_SERVER['CONTENT_TYPE'] ?? '';
if (stripos($ctype, 'application/json') === 0) {
    $raw = file_get_contents('php://input') ?: '';
    $dec = json_decode($raw, true);
    if (is_array($dec)) {
        foreach ($dec as $k => $v) { if (is_scalar($v)) $fields[(string)$k] = (string)$v; }
    }
} else {
    foreach ($_POST as $k => $v) { if (is_scalar($v)) $fields[(string)$k] = (string)$v; }
}

// ------------------------------------------------------------------ honeypot
/* careers names it "company" (which is not a field there); contacts names it
   "website" (because company IS a field there). Both are invisible to a
   person, so anything in either one is a bot -- answered 200 so the script
   learns nothing from the reply. */
foreach (['website', 'hp'] as $trap) {
    if (($fields[$trap] ?? '') !== '') json_out(200, ['ok' => true]);
}
if ($which === 'careers' && ($fields['company'] ?? '') !== '') {
    json_out(200, ['ok' => true]);
}

// ------------------------------------------------------------------ required
$required = [
    'careers'   => ['name', 'email', 'phone', 'role', 'available'],
    'contact'   => ['first', 'last', 'email', 'message'],
    'subscribe' => ['email'],
];
$need = $required[$which];
foreach ($need as $k) {
    if (trim($fields[$k] ?? '') === '') json_out(422, ['ok' => false, 'error' => "missing $k"]);
}
if (!filter_var($fields['email'], FILTER_VALIDATE_EMAIL)) {
    json_out(422, ['ok' => false, 'error' => 'email']);
}
/* The consent record the site now sends with every submission. Refusing a
   submission that says "no" is the point: the forms gate on it client-side and
   the server must not be the weaker of the two. */
if (($fields['consent'] ?? '') !== 'yes') {
    json_out(422, ['ok' => false, 'error' => 'consent']);
}

// ------------------------------------------------------------------ files
$files = [];
$total = 0;
/* The site posts attachment[]; a hosted service might want a bare attachment.
   Read whichever arrived rather than depending on one. */
$fkey = !empty($_FILES['attachment']['name']) ? 'attachment' : null;
if ($fkey === null && !empty($_FILES['attachment'][0]['name'])) $fkey = 'attachment';
if ($fkey !== null) {
    $f = $_FILES[$fkey];
    $names = is_array($f['name']) ? $f['name'] : [$f['name']];
    $tmps  = is_array($f['tmp_name']) ? $f['tmp_name'] : [$f['tmp_name']];
    $errs  = is_array($f['error']) ? $f['error'] : [$f['error']];
    $sizes = is_array($f['size']) ? $f['size'] : [$f['size']];
    if (count($names) > MAX_FILES) json_out(422, ['ok' => false, 'error' => 'too many files']);
    for ($i = 0; $i < count($names); $i++) {
        if ((int)$errs[$i] !== UPLOAD_ERR_OK) continue;
        if (!is_uploaded_file($tmps[$i])) continue;          // never trust the path
        $ext = strtolower(pathinfo((string)$names[$i], PATHINFO_EXTENSION));
        if (!in_array($ext, ALLOWED_EXT, true)) {
            json_out(422, ['ok' => false, 'error' => "file type .$ext"]);
        }
        $total += (int)$sizes[$i];
        if ($total > MAX_BYTES) json_out(422, ['ok' => false, 'error' => 'attachments too large']);
        /* basename() and a whitelist on the name: the value comes from the
           browser and "../../x.pdf" is a legal thing for it to send. The file
           is attached and never written anywhere, so this only keeps the name
           in the email sane. */
        $safe = preg_replace('/[^A-Za-z0-9._ -]+/', '_', basename((string)$names[$i])) ?? 'file';
        $files[] = ['name' => substr($safe, 0, 120),
                    'body' => (string)file_get_contents($tmps[$i])];
    }
}

// ------------------------------------------------------------------ the email
$labels = [
    'careers'   => 'Application',
    'contact'   => 'Project enquiry',
    'subscribe' => 'Newsletter subscription',
];
$who = $which === 'contact'
    ? trim(($fields['first'] ?? '') . ' ' . ($fields['last'] ?? ''))
    : ($fields['name'] ?? $fields['email']);
$subject = header_safe(sprintf('[%s] %s', $labels[$which], $who !== '' ? $who : $fields['email']));

$order = ['role','name','first','last','email','phone','country','company','group','topic',
          'years','certifications','available','rotation','countries','message'];
$lines = [];
foreach ($order as $k) {
    if (($fields[$k] ?? '') !== '') $lines[] = sprintf('%-16s %s', $k . ':', $fields[$k]);
}
foreach ($fields as $k => $v) {
    if (in_array($k, $order, true) || $v === '') continue;
    if (strpos($k, 'consent') === 0) continue;               // grouped below
    $lines[] = sprintf('%-16s %s', $k . ':', $v);
}
$lines[] = '';
$lines[] = '--- consent -------------------------------------------------';
$lines[] = 'given:           ' . ($fields['consent'] ?? '');
$lines[] = 'page:            ' . ($fields['consent_page'] ?? '');
$lines[] = 'language:        ' . ($fields['consent_lang'] ?? '');
$lines[] = 'wording shown:   ' . ($fields['consent_text'] ?? '');
$lines[] = '';
$lines[] = '--- request -------------------------------------------------';
$lines[] = 'received:        ' . gmdate('Y-m-d H:i:s') . ' UTC';
$lines[] = 'ip:              ' . client_ip();
$lines[] = 'attachments:     ' . count($files);
$body = implode("\n", $lines) . "\n";

$boundary = 'alp' . bin2hex(random_bytes(12));
$headers  = [
    'From: ALPROJECTS website <' . MAILFROM . '>',
    /* Reply-To carries the visitor's address so the office can answer from the
       mailbox. From: stays on our own domain: putting a stranger's address
       there is what gets the mail rejected by SPF or filed as spam. */
    'Reply-To: ' . header_safe($fields['email']),
    'MIME-Version: 1.0',
    'Content-Type: multipart/mixed; boundary="' . $boundary . '"',
];

$msg  = "--$boundary\r\n"
      . "Content-Type: text/plain; charset=utf-8\r\n"
      . "Content-Transfer-Encoding: 8bit\r\n\r\n"
      . $body . "\r\n";
foreach ($files as $file) {
    $msg .= "--$boundary\r\n"
          . 'Content-Type: application/octet-stream; name="' . $file['name'] . "\"\r\n"
          . 'Content-Disposition: attachment; filename="' . $file['name'] . "\"\r\n"
          . "Content-Transfer-Encoding: base64\r\n\r\n"
          . chunk_split(base64_encode($file['body'])) . "\r\n";
}
$msg .= "--$boundary--\r\n";

$sent = mail(MAILTO, $subject, $msg, implode("\r\n", $headers));
if (!$sent) {
    /* Say so rather than answering 200: the form shows its failure note and the
       visitor keeps what they typed, which is the whole reason the mailto
       fallback was not good enough. */
    json_out(502, ['ok' => false, 'error' => 'mail']);
}
json_out(200, ['ok' => true]);
