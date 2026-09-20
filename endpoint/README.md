# Form endpoint

`form.php` receives the three forms on alprojects.co, emails each submission to
the office with its attachments, and answers the browser with JSON.

**It does not belong in this repository's published tree.** GitHub Pages serves
files, it does not execute them — a `.php` committed at the site root would be
downloaded as source, config and all. It lives here as the deliverable for
whoever installs it, and the site only ever holds its URL.

## Install

1. Upload `form.php` to the company's own hosting — anywhere PHP 7.4 or later
   runs. The mailbox for `@alprojects.eu` almost certainly sits on hosting that
   does.
2. Edit the block at the top:
   - `MAILTO` — where submissions arrive. Currently `info@alprojects.eu`.
   - `MAILFROM` — must be an address the host is allowed to send as, or SPF
     will bounce it. `website@alprojects.eu` is the usual shape.
   - `ALLOWED_ORIGIN` — leave as is unless the site moves domain.
3. Check two PHP settings on the host:

   ```ini
   upload_max_filesize = 12M   ; the careers form offers 10 MB per file
   post_max_size       = 30M   ; must exceed MAX_BYTES (25 MB) plus the fields
   ```

   This is the one that bites. With the default `post_max_size = 8M`, PHP
   discards the whole body **before the script runs**: `$_POST` and `$_FILES`
   arrive empty, the script sees a submission with no fields, and the visitor
   gets a validation error about a field they filled in. Nothing in the log
   says why.
4. Put the three URLs in `js/main.js`:

   ```js
   var CAREERS_ENDPOINT = "https://<host>/form.php?f=careers";
   var CONTACT_ENDPOINT = "https://<host>/form.php?f=contact";
   var FORM_ENDPOINT    = "https://<host>/form.php?f=subscribe";
   ```

   Leave `PROCESSOR_NAME = ""` — the privacy policy then names `<host>` itself,
   which is correct when the endpoint is the company's own.
5. Send one real submission from each form, one of them with an attachment.
   This is the audit's own acceptance step.

## No secrets in this file

It sits in a public repository and GitHub Pages will serve it as text, so
`form.php` holds no key and no shared secret — only addresses that are already
on the contacts page. What stops a stranger using it is the origin check, the
honeypot and the throttle, plus the fact that the worst it can do is send an
email to the office. If a future version needs a credential, it goes in an
environment variable or a file outside the web root on the host, never here.

## What the site sends

| | `/careers` | `/contacts` | newsletter |
|---|---|---|---|
| Encoding | multipart | multipart | JSON |
| Files | `attachment[]`, up to 6 | `attachment[]` | — |
| Honeypot | `company` | `website` | — |
| Consent | `consent`, `consent_text`, `consent_page`, `consent_lang` | same | same |

`attachment[]` carries the brackets on purpose: PHP builds `$_FILES` arrays only
for bracketed names, and under a bare `attachment` it keeps the last file and
discards the rest — an application would have arrived with the certificate scan
and no CV, silently. A hosted service that documents a bare `attachment` would
want them dropped; the script reads either shape.

The consent fields are the GDPR Art. 7(1) record: the state, the exact sentence
shown, the page and the language. The script **refuses** a submission whose
`consent` is not `yes`, so the server is not the weaker of the two checks.

## What it refuses

Anything that is not a POST from an allowed origin; a filled honeypot (answered
`200` so a script learns nothing); more than 6 files or 25 MB in total; an
extension not on the list; a second submission from the same address inside 60
seconds; a missing required field; a submission without consent.

## What it does not do

No database, no files written to disk, no logging of submissions. The enquiries
already go to `info@` and are worked from there — a second copy would be a
second thing to secure, to find on a subject-access request, and to delete after
24 months, for no benefit. Nothing about the visitor is stored by this file.

## Verified

Syntax parsed with `php-parser` 3.7 (PHP 7 grammar) — clean. The client side was
driven end to end in a real browser against a local endpoint speaking the same
contract, with a 240 KB PDF and a second file attached: all fields, both files
and the consent record arrived, and all three forms reset and reported success.

**`mail()` itself is unverified** — there is no PHP on the machine this was
written on, so the send path has not been executed. That is what step 5 checks.
If `mail()` is disabled on the host (some providers disable it in favour of
SMTP), the script answers `502` and the form shows its failure note rather than
claiming success; swapping `mail()` for the host's SMTP is then a few lines.
