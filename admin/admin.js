/* The editor. One file, no framework, no CDN -- the site makes no third-party
 * request and this page is part of the site.
 *
 * TWO LANGUAGES
 * Russian and English, switched without a reload and remembered per browser.
 * Every string the client reads comes out of L below, including the field
 * labels and the confirm prompts; nothing is written into the markup twice.
 * The <html lang> attribute follows, so a screen reader changes voice with it.
 *
 * THE FORM IS BUILT FROM THE DATA
 * A string is a box, a long string a textarea, a list of strings a numbered
 * list with add and remove, a boolean a checkbox, an ISO date a date field.
 * Describing 715 fields by hand would be out of date the first time a record
 * gained a line. A key starting with an underscore is structure rather than
 * copy: dimmed, sorted after the copy, and offered as a list to pick from
 * where its value has to match something.
 */
(function () {
  "use strict";

  var API = "/api/cms";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var el = function (t, c, x) {
    var n = document.createElement(t);
    if (c) n.className = c;
    if (x != null) n.textContent = x;
    return n;
  };
  var pad = function (n) { return (n < 10 ? "0" : "") + n; };

  /* ---------------------------------------------------------------- words */
  /* [ru, en]. One table, so a string cannot exist in one language only. */
  var L = {
    editor:      ["РЕДАКТОР", "EDITOR"],
    gate_h1:     ["Редактор", "Editor"],
    gate_sub:    ["Содержимое сайта alprojects.eu", "The content of alprojects.eu"],
    password:    ["Пароль", "Password"],
    sign_in:     ["Войти", "Sign in"],
    sign_out:    ["Выйти", "Sign out"],
    checking:    ["Проверяем…", "Checking…"],
    wrong_pw:    ["Неверный пароль.", "Wrong password."],
    not_set_up:  ["Редактор ещё не настроен на этом сайте.",
                  "The editor is not configured on this deployment."],
    no_network:  ["Сеть недоступна.", "No network."],
    yours:       ["Ваше", "Yours"],
    the_rest:    ["Остальное", "The rest"],
    loading:     ["Загружаем…", "Loading…"],
    load_failed: ["Не удалось загрузить", "Could not load"],
    sheet:       ["Лист", "Sheet"],
    state:       ["Состояние", "State"],
    saved_state: ["Сохранено", "Saved"],
    unsaved:     ["Есть несохранённые изменения", "Unsaved changes"],
    saving:      ["Сохраняем…", "Saving…"],
    saved_msg:   ["Сохранено. Сайт пересоберётся за пару минут.",
                  "Saved. The site rebuilds in a couple of minutes."],
    save:        ["Сохранить", "Save"],
    discard:     ["Отменить", "Discard"],
    conflict:    ["Кто-то сохранил это, пока страница была открыта. Обновите страницу.",
                  "Somebody saved this while the page was open. Reload."],
    not_saved:   ["Не сохранилось", "Not saved"],
    add:         ["+ Добавить", "+ Add"],
    up:          ["Выше", "Up"],
    down:        ["Ниже", "Down"],
    remove:      ["Удалить", "Remove"],
    add_line:    ["+ строка", "+ line"],
    nothing_tr:  ["Переводить нечего", "Nothing to translate"],
    loading_tr:  ["Загружаем переводы…", "Loading translations…"],
    tr_ok:       ["переведено", "translated"],
    tr_none:     ["нет перевода", "not translated"],
    tr_stale:    ["английский изменился", "English changed"],
    tr_unknown:  ["проверьте", "check this"],
    tr_machine:  ["машинный перевод", "machine translation"],
    translating: ["Переводим…", "Translating…"],
    tr_failed:   ["Перевести не удалось, текст остался английским",
                  "Translation failed; the text stays in English"],
    auto_on:     ["Переводить автоматически", "Translate automatically"],
    auto_hint:   ["При сохранении всё непереведённое и всё, где английский изменился, переводится машиной и помечается как машинный перевод.",
                  "On save, anything untranslated or whose English has changed is machine translated and marked as such."],
    tr_checking: ["…", "…"],
    translation: ["Перевод", "Translation"],
    content:     ["Содержание", "Content"],
    not_chosen:  ["— не выбрано —", "— not chosen —"],
    not_in_list: ["нет в списке", "not on the list"],
    upload:      ["Загрузить фото", "Upload a photo"],
    upload_hint: ["JPEG, PNG или WebP, до 12 МБ. Размеры посчитает сборка.",
                  "JPEG, PNG or WebP, up to 12 MB. The build works out the size."],
    uploading:   ["Загружаем", "Uploading"],
    uploaded:    ["Загружено. Фото появится на сайте после сохранения.",
                  "Uploaded. The photo appears on the site once you save."],
    upload_fail: ["Не загрузилось", "Upload failed"],
    ask_leave:   ["Изменения не сохранены. Уйти и потерять их?",
                  "There are unsaved changes. Leave and lose them?"],
    ask_discard: ["Вернуть всё как было при открытии?",
                  "Put everything back to how it was when you opened it?"],
    ask_slug:    ["Короткое имя латиницей, из него получится адрес страницы:\nнапример  crane-foundation-package",
                  "A short latin name — it becomes the page address:\nfor example  crane-foundation-package"],
    bad_slug:    ["Такое имя не подходит.", "That name will not do."],
    slug_taken:  ["Запись с таким именем уже есть.", "A record with that name already exists."],
    ask_remove:  ["Удалить «%s»?\n\nПосле сохранения страница пропадёт с сайта и из карты сайта, на всех языках.",
                  "Remove “%s”?\n\nOnce you save, the page leaves the site and the sitemap, in every language."],
    unprinted_count: ["Сейчас на сайте не выводится — строку убрали из карточки. Формулировка оставлена в файле на случай, если понадобится.",
                      "Not shown on the site today: the row was removed from the card and the wording kept in the file in case it is wanted."],
  };

  var TITLES = {
    positions: ["Вакансии", "Vacancies"],
    articles:  ["Новости", "News"],
    services:  ["Услуги", "Services"],
    cases:     ["Проекты", "Projects"],
    sectors:   ["Отрасли", "Sectors"],
    site:      ["Тексты сайта", "Site text"],
  };

  /* Only the keys whose own name would be a guess. Anything else shows its
     key, which is honest and stays right when a field is added. */
  var LABELS = {
    title: ["Заголовок", "Title"], lead: ["Вводный абзац", "Lead"],
    body: ["Текст", "Body"], summary: ["Описание", "Summary"],
    needs: ["Требования", "Requirements"], cat: ["Рубрика", "Category"],
    alt: ["Описание фото (alt)", "Photo description (alt)"],
    seo: ["Заголовок для поиска", "Search title"], cta: ["Призыв к действию", "Call to action"],
    location: ["Место работы", "Location"], contract: ["Договор", "Contract"],
    rotation: ["Вахта", "Rotation"], start: ["Начало", "Start"], rate: ["Ставка", "Rate"],
    count: ["Количество", "Count"], nav: ["Пункт меню", "Menu item"],
    h1: ["Заголовок страницы", "Page heading"], points: ["Пункты", "Points"],
    name: ["Название", "Name"], facts: ["Факты", "Facts"],
    label: ["Подпись", "Label"], value: ["Значение", "Value"], note: ["Примечание", "Note"],
    _open: ["Открыта", "Open"], _posted: ["Опубликовано", "Posted"],
    _valid_through: ["Действительна до", "Valid through"],
    _employment_type: ["Тип занятости", "Employment type"],
    _countries: ["Страны", "Countries"], _discipline: ["Специальность", "Discipline"],
    _img: ["Файл фото", "Photo file"], _date: ["Дата", "Date"],
    _iso: ["Дата (ISO)", "Date (ISO)"], _w: ["Ширина", "Width"], _h: ["Высота", "Height"],
  };

  /* Values that have to match something else exactly. _discipline is the one
     that breaks visibly: it must equal an option in the application form's
     list or the Apply button on that vacancy selects nothing, and a text box
     invites a typo nobody sees until somebody tries to apply. */
  var CHOICES = {
    _discipline: ["site", ["form_options", "disciplines"]],
    _employment_type: [null, ["FULL_TIME", "PART_TIME", "CONTRACTOR",
                              "TEMPORARY", "INTERN", "OTHER"]],
  };

  /* Copy that is in the files on purpose and printed nowhere. Saying so is the
     point: otherwise the client translates a line into four languages and
     never finds it on the site. */
  var UNPRINTED = { "positions.count": "unprinted_count" };

  var MINE = ["positions", "articles"];
  var TR_LANGS = [["t-ru", "RU"], ["t-fr", "FR"], ["t-de", "DE"], ["t-it", "IT"]];
  var UI_LANGS = [["ru", "RU"], ["en", "EN"]];

  var lang = 0;
  try {
    if (localStorage.getItem("cms_lang") === "en") lang = 1;
  } catch (e) { /* private window: the default is fine */ }

  function t(key) { var r = L[key]; return r ? r[lang] : key; }
  function title(name) { var r = TITLES[name]; return r ? r[lang] : name; }
  function labelFor(key) { var r = LABELS[key]; return r ? r[lang] : key; }

  function setLang(i) {
    lang = i;
    try { localStorage.setItem("cms_lang", UI_LANGS[i][0]); } catch (e) {}
    document.documentElement.lang = UI_LANGS[i][0];
    paintStatic();
    if (state.name) render();
  }

  /* Everything marked data-t in the markup, so a label cannot be left behind
     in the other language when a string is renamed. */
  function paintStatic() {
    Array.prototype.forEach.call(document.querySelectorAll("[data-t]"),
      function (n) { n.textContent = t(n.dataset.t); });
    [["#gate-langs", true], ["#ui-langs", false]].forEach(function (pair) {
      var host = $(pair[0]);
      if (!host) return;
      host.innerHTML = "";
      UI_LANGS.forEach(function (p, i) {
        var b = el("button", i === lang ? "on" : "", p[1]);
        b.type = "button";
        b.addEventListener("click", function () { setLang(i); });
        host.appendChild(b);
      });
    });
    $("#bar-sheet").textContent = state.name ? title(state.name).toUpperCase() : "";
    /* The rail is built once, in start(), so a language switch has to repaint
       it by hand. The first version did not, and the collections stayed in the
       old language while everything else changed -- which looks like a broken
       toggle rather than a missed call. */
    Array.prototype.forEach.call(document.querySelectorAll("#rail a[data-name]"),
      function (a) {
        var first = a.querySelector("span");
        if (first) first.textContent = title(a.dataset.name);
      });
    paintMsg();
    if (gateSay.key) gateSay(gateSay.key, gateSay.extra);
  }

  var state = { name: null, data: null, sha: null, rec: null,
                lang: "t-ru", tr: {}, dirty: false, msg: null };

  /* ------------------------------------------------------------ plumbing */

  function api(path, opts) {
    return fetch(API + path, Object.assign({ credentials: "same-origin" }, opts || {}))
      .then(function (r) {
        return r.json().catch(function () { return {}; })
          .then(function (j) { j.status = r.status; return j; });
      });
  }

  /* A message set from code is not in the markup, so paintStatic() cannot find
     it. Both of these therefore remember WHICH string they are showing rather
     than the text they showed: switching language with a message on screen
     left it in the old language, which looks like half a toggle.
     `extra` is the part that is not translatable -- a file name, an error from
     the server -- and it is kept separate so the translated half can change
     under it. */
  function say(key, kind, extra) {
    state.msg = key ? [key, kind || "", extra || ""] : null;
    paintMsg();
  }

  function paintMsg() {
    var s = $("#state");
    if (!s) return;
    if (!state.msg) { s.textContent = ""; s.className = "v"; return; }
    s.textContent = t(state.msg[0]) + (state.msg[2] ? ": " + state.msg[2] : "");
    s.className = "v" + (state.msg[1] ? " " + state.msg[1] : "");
  }

  function gateSay(key, extra) {
    var m = $("#gate-msg");
    gateSay.key = key || null;
    gateSay.extra = extra || "";
    m.textContent = key ? t(key) + (extra ? ": " + extra : "") : "";
  }

  function markDirty() {
    state.dirty = true;
    say("unsaved", "dirty");
    $("#bar").classList.add("on");
    /* Editing the English changes what the translation panel is about, so the
       panel has to follow -- otherwise it sits there showing the sentence
       before the edit, next to a badge about that older sentence. Only that
       node is rebuilt, never the form: a full render would take the caret out
       of the field being typed in. Debounced, because this runs on every
       keystroke. */
    if (_panelTimer) clearTimeout(_panelTimer);
    _panelTimer = setTimeout(refreshTranslations, 700);
  }

  var _panelTimer = null;

  function refreshTranslations() {
    _panelTimer = null;
    var old = document.querySelector("#main .panel-tr");
    if (!old || !state.rec || MINE.indexOf(state.name) < 0) return;
    /* Do not steal the caret from a translation being typed in this panel. */
    if (old.contains(document.activeElement)) return;
    old.parentNode.replaceChild(translationPanel(), old);
  }

  /* ------------------------------------------------------------ the gate */

  $("#login").addEventListener("submit", function (e) {
    e.preventDefault();
    gateSay("checking");
    api("?a=login", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ password: $("#pw").value }),
    }).then(function (r) {
      if (r.ok) { $("#pw").value = ""; start(); return; }
      gateSay(r.status === 503 ? "not_set_up" : "wrong_pw");
    }).catch(function () { gateSay("no_network"); });
  });

  $("#out").addEventListener("click", function () {
    api("?a=logout", { method: "POST" }).then(function () { location.reload(); });
  });

  /* ------------------------------------------------------- the collections */

  function start() {
    api("?a=list").then(function (r) {
      if (!r.ok) { location.reload(); return; }
      $("#gate").style.display = "none";
      $("#app").classList.add("on");
      var mine = $("#rail-mine"), rest = $("#rail-rest");
      mine.innerHTML = rest.innerHTML = "";
      r.collections.forEach(function (n) {
        if (n.indexOf("t-") === 0) return;      /* reached from a record */
        var a = el("a");
        a.dataset.name = n;
        a.appendChild(el("span", "", title(n)));
        a.appendChild(el("span", "n"));
        a.addEventListener("click", function () { open(n); });
        (MINE.indexOf(n) >= 0 ? mine : rest).appendChild(a);
      });
      open(MINE[0]);
    });
  }

  function open(name) {
    if (state.dirty && !confirm(t("ask_leave"))) return;
    state.name = name; state.rec = null; state.dirty = false; state.tr = {};
    $("#bar").classList.remove("on");
    Array.prototype.forEach.call(document.querySelectorAll("#rail a[data-name]"),
      function (a) { a.classList.toggle("on", a.dataset.name === name); });
    $("#main").innerHTML = "";
    $("#main").appendChild(el("p", "empty", t("loading")));
    api("?a=load&f=" + encodeURIComponent(name)).then(function (r) {
      if (!r.ok) {
        $("#main").innerHTML = "";
        $("#main").appendChild(el("p", "empty", r.error || t("load_failed")));
        return;
      }
      state.data = r.data;
      state.sha = r.sha;
      if (Array.isArray(r.data._order) && r.data._order.length) state.rec = r.data._order[0];
      var a = $('#rail a[data-name="' + name + '"] .n');
      if (a) a.textContent = Array.isArray(r.data._order) ? r.data._order.length : "";
      paintStatic();
      render();
    });
  }

  /* ------------------------------------------------------------- rendering */

  function heading(text, over) {
    var h = el("div", "head");
    var row = el("div", "over");
    if (over) row.appendChild(el("span", "lbl", over));
    h.appendChild(row);
    h.appendChild(el("h1", "", text));
    h.appendChild(el("div", "rule"));
    return h;
  }

  function render() {
    var m = $("#main");
    m.innerHTML = "";
    m.appendChild(heading(title(state.name)));

    if (!Array.isArray(state.data._order)) {
      var box = el("div", "panel");
      fieldsInto(box, state.data, []);
      m.appendChild(box);
      return;
    }

    var cols = el("div", "cols");
    cols.appendChild(recordList());
    var right = el("div");
    if (state.rec) {
      var f = el("div", "panel");
      var cap = el("div", "cap");
      cap.appendChild(el("span", "lbl", t("content")));
      cap.appendChild(el("span", "rule"));
      f.appendChild(cap);
      fieldsInto(f, state.data[state.rec], [state.rec]);
      right.appendChild(f);
      if (MINE.indexOf(state.name) >= 0) right.appendChild(translationPanel());
    }
    cols.appendChild(right);
    m.appendChild(cols);
  }

  function recordList() {
    var wrap = el("div", "recs");
    state.data._order.forEach(function (slug, i) {
      var r = state.data[slug] || {};
      var row = el("div", "rec" + (slug === state.rec ? " on" : ""));
      row.appendChild(el("span", "num", pad(i + 1)));

      var nm = el("button", "nm", r.title || r.name || slug);
      nm.type = "button";
      nm.addEventListener("click", function () { state.rec = slug; render(); });
      row.appendChild(nm);

      var acts = el("div", "acts");
      if (typeof r._open === "boolean")
        acts.appendChild(el("span", "dot" + (r._open ? "" : " off")));
      [["↑", -1, "up"], ["↓", 1, "down"]].forEach(function (p) {
        var b = el("button", "mv", p[0]);
        b.type = "button"; b.title = t(p[2]);
        if ((p[1] < 0 && i === 0) || (p[1] > 0 && i === state.data._order.length - 1))
          b.disabled = true;
        b.addEventListener("click", function () { move(i, p[1]); });
        acts.appendChild(b);
      });
      var rm = el("button", "mv rm", "×");
      rm.type = "button"; rm.title = t("remove");
      rm.addEventListener("click", function () { removeRecord(slug); });
      acts.appendChild(rm);
      row.appendChild(acts);
      wrap.appendChild(row);
    });
    var add = el("button", "add", t("add"));
    add.type = "button";
    add.addEventListener("click", addRecord);
    wrap.appendChild(add);
    return wrap;
  }

  function move(i, d) {
    var o = state.data._order, j = i + d;
    if (j < 0 || j >= o.length) return;
    var x = o[i]; o[i] = o[j]; o[j] = x;
    markDirty(); render();
  }

  function addRecord() {
    var raw = prompt(t("ask_slug"));
    if (!raw) return;
    var slug = raw.trim().toLowerCase().replace(/[^a-z0-9-]+/g, "-").replace(/^-|-$/g, "");
    if (!slug) { alert(t("bad_slug")); return; }
    if (state.data[slug]) { alert(t("slug_taken")); return; }
    /* Copied from the first record and emptied, so a new one carries every
       field the build expects. Inventing the shape here would mean describing
       it twice and getting it wrong the first time a field is added. */
    state.data[slug] = blank(state.data[state.data._order[0]] || {});
    state.data._order.unshift(slug);
    state.rec = slug;
    markDirty(); render();
  }

  function blank(v) {
    if (Array.isArray(v)) return v.length && typeof v[0] === "object" ? [blank(v[0])] : [];
    if (v && typeof v === "object") {
      var o = {};
      Object.keys(v).forEach(function (k) { o[k] = blank(v[k]); });
      return o;
    }
    if (typeof v === "boolean") return true;
    if (typeof v === "number") return v;
    return "";
  }

  function removeRecord(slug) {
    var r = state.data[slug] || {};
    if (!confirm(t("ask_remove").replace("%s", r.title || r.name || slug))) return;
    delete state.data[slug];
    state.data._order = state.data._order.filter(function (s) { return s !== slug; });
    if (state.rec === slug) state.rec = state.data._order[0] || null;
    markDirty(); render();
  }

  /* ---------------------------------------------------------- the fields */

  function fieldsInto(box, obj, path) {
    /* Copy first, structure after. The file's key order puts _discipline above
       the title on a vacancy, which is the build's order of business and not
       the client's -- he came to change a sentence. Underscore keys keep their
       own relative order, so the dates stay in the sequence somebody chose. */
    var keys = Object.keys(obj).filter(function (k) { return k !== "_order"; });
    var copy = keys.filter(function (k) { return k.charAt(0) !== "_"; });
    var struct = keys.filter(function (k) { return k.charAt(0) === "_"; });
    copy.concat(struct).forEach(function (k) {
      box.appendChild(fieldFor(k, obj, k, path.concat(k)));
    });
  }

  function fieldFor(key, parent, k, path) {
    var v = parent[k];
    var struct = key.charAt(0) === "_";

    if (typeof v === "boolean") {
      var w = el("div", "f" + (struct ? " struct" : ""));
      var lab = el("label", "chk");
      var cb = el("input"); cb.type = "checkbox"; cb.checked = v;
      cb.addEventListener("change", function () { parent[k] = cb.checked; markDirty(); });
      lab.appendChild(cb);
      lab.appendChild(el("span", "lbl", labelFor(key)));
      w.appendChild(lab);
      return w;
    }

    if (Array.isArray(v)) {
      var g = el("div", "group");
      g.appendChild(el("span", "lbl", labelFor(key)));
      v.forEach(function (item, i) {
        if (item && typeof item === "object") {
          var sub = el("div", "group");
          sub.appendChild(el("span", "lbl", pad(i + 1)));
          fieldsInto(sub, item, path.concat(i));
          g.appendChild(sub);
          return;
        }
        var row = el("div", "list-row");
        row.appendChild(el("span", "num", pad(i + 1)));
        var ta = el("textarea"); ta.value = item; ta.rows = 2;
        ta.addEventListener("input", function () { v[i] = ta.value; markDirty(); });
        var x = el("button", "btn btn-q", "×");
        x.type = "button"; x.title = t("remove");
        x.addEventListener("click", function () { v.splice(i, 1); markDirty(); render(); });
        row.appendChild(ta); row.appendChild(x);
        g.appendChild(row);
      });
      if (!v.length || typeof v[0] !== "object") {
        var plus = el("button", "btn btn-q", t("add_line"));
        plus.type = "button";
        plus.addEventListener("click", function () { v.push(""); markDirty(); render(); });
        g.appendChild(plus);
      }
      return g;
    }

    if (v && typeof v === "object") {
      var gg = el("div", "group");
      gg.appendChild(el("span", "lbl", labelFor(key)));
      fieldsInto(gg, v, path);
      return gg;
    }

    var f = el("div", "f" + (struct ? " struct" : ""));
    f.appendChild(el("label", "lbl", labelFor(key)));

    if (CHOICES[key]) {
      var sel = el("select");
      var fill = function (opts) {
        sel.innerHTML = "";
        var b0 = el("option", "", t("not_chosen")); b0.value = "";
        sel.appendChild(b0);
        opts.forEach(function (o) {
          var op = el("option", "", o); op.value = o;
          if (o === v) op.selected = true;
          sel.appendChild(op);
        });
        /* A value already in the file that is not on the list is kept and
           shown as wrong, never silently replaced: it is somebody's data. */
        if (v && opts.indexOf(v) < 0) {
          var odd = el("option", "", v + "  (" + t("not_in_list") + ")");
          odd.value = v; odd.selected = true;
          sel.appendChild(odd);
        }
      };
      sel.addEventListener("change", function () { parent[k] = sel.value; markDirty(); });
      var spec = CHOICES[key];
      if (spec[0] === null) fill(spec[1]);
      else { fill(v ? [v] : []); choices(spec[0], spec[1]).then(fill); }
      f.appendChild(sel);
      return f;
    }

    var input;
    if (typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v)) {
      input = el("input"); input.type = "date"; input.value = v;
    } else if (typeof v === "string" && (v.length > 110 || v.indexOf("\n") >= 0)) {
      input = el("textarea"); input.value = v;
      input.rows = Math.min(14, Math.max(3, Math.ceil(v.length / 70)));
    } else {
      input = el("input"); input.type = "text"; input.value = v;
    }
    input.addEventListener("input", function () { parent[k] = input.value; markDirty(); });
    f.appendChild(input);

    if (key === "_img") f.appendChild(photoPicker(parent, k, input));
    var un = UNPRINTED[state.name + "." + key];
    if (un) f.appendChild(el("div", "hint", t(un)));
    return f;
  }

  /* The photograph goes up as the original the phone produced; the build
     derives the sizes the page needs and reads the real pixel dimensions off
     the result, which is why width and height are not something to type. They
     were typed once, disagreed with the file, and the news cards served 600px
     images into 626px boxes. */
  function photoPicker(parent, k, pathInput) {
    var wrap = el("div");
    var row = el("div", "list-item");
    var pick = el("button", "btn btn-q", t("upload"));
    pick.type = "button";
    var file = el("input");
    file.type = "file";
    file.accept = "image/jpeg,image/png,image/webp";
    file.style.display = "none";
    var note = el("span", "hint", t("upload_hint"));

    pick.addEventListener("click", function () { file.click(); });
    file.addEventListener("change", function () {
      var f = file.files && file.files[0];
      if (!f) return;
      pick.disabled = true;
      note.textContent = t("uploading") + " " + f.name + "…";
      /* The bytes, raw. No multipart and no base64 on the way up: the endpoint
         sniffs the magic numbers, so the body is the file and nothing else. */
      api("?a=upload&name=" + encodeURIComponent(f.name), {
        method: "POST",
        headers: { "content-type": "application/octet-stream" },
        body: f,
      }).then(function (r) {
        pick.disabled = false;
        file.value = "";
        if (!r.ok) { note.textContent = t("upload_fail") + ": " + (r.error || ""); return; }
        parent[k] = r.img;
        pathInput.value = r.img;
        note.textContent = t("uploaded");
        markDirty();
      }).catch(function () {
        pick.disabled = false;
        note.textContent = t("upload_fail");
      });
    });

    row.appendChild(pick); row.appendChild(note);
    wrap.appendChild(row); wrap.appendChild(file);
    return wrap;
  }

  /* Option lists, fetched once. Outside `state` because they belong to the
     site rather than to whatever is open. */
  var _choices = {};
  function choices(file, pathIn) {
    var key = file + "/" + pathIn.join(".");
    if (_choices[key]) return _choices[key];
    _choices[key] = api("?a=load&f=" + encodeURIComponent(file)).then(function (r) {
      var node = r.ok ? r.data : null;
      for (var i = 0; node && i < pathIn.length; i++) node = node[pathIn[i]];
      return Array.isArray(node) ? node : [];
    }).catch(function () { return []; });
    return _choices[key];
  }

  /* The same fingerprint content.py computes: sha1 of the UTF-8 text, first
     ten hex characters. The store keeps that rather than the English itself,
     so without this the page could not tell a fresh translation from one whose
     English has since been edited -- and it showed "translated" for a field
     the site was already serving in English. The client would have had no way
     to know the line had fallen out.

     crypto.subtle needs a secure context, which https and localhost both are.
     If it is missing the row says "check this" rather than "translated":
     erring toward look-at-it, never toward all-good. */
  function fingerprint(text) {
    if (!(window.crypto && crypto.subtle && window.TextEncoder))
      return Promise.resolve(null);
    return crypto.subtle.digest("SHA-1", new TextEncoder().encode(text))
      .then(function (buf) {
        var out = "";
        new Uint8Array(buf).forEach(function (b) {
          out += (b < 16 ? "0" : "") + b.toString(16);
        });
        return out.slice(0, 10);
      }).catch(function () { return null; });
  }

  /* ------------------------------------------------------- translations */

  /* The same leaves the build counts: every non-underscore string under this
     record. Mirrored here rather than fetched so the panel can be drawn before
     anything is saved; tools/content.py flatten() is the original. */
  function leaves(obj, prefix, out) {
    out = out || [];
    if (Array.isArray(obj)) {
      obj.forEach(function (v, i) { leaves(v, prefix + "." + (i + 1), out); });
    } else if (obj && typeof obj === "object") {
      Object.keys(obj).forEach(function (k) {
        if (k.charAt(0) === "_") return;
        leaves(obj[k], prefix ? prefix + "." + k : k, out);
      });
    } else if (typeof obj === "string" && obj.trim()) {
      out.push([prefix, obj]);
    }
    return out;
  }

  function translationPanel() {
    var wrap = el("div", "panel panel-tr");
    var cap = el("div", "cap");
    cap.appendChild(el("span", "lbl", t("translation")));
    cap.appendChild(el("span", "rule"));
    wrap.appendChild(cap);

    var auto = el("label", "chk");
    var acb = el("input"); acb.type = "checkbox"; acb.checked = autoTranslate();
    acb.addEventListener("change", function () {
      try { localStorage.setItem("cms_auto", acb.checked ? "1" : "0"); } catch (e) {}
    });
    auto.appendChild(acb);
    auto.appendChild(el("span", "lbl", t("auto_on")));
    wrap.appendChild(auto);
    wrap.appendChild(el("div", "hint", t("auto_hint")));

    var tabs = el("div", "tabs");
    TR_LANGS.forEach(function (p) {
      var b = el("button", p[0] === state.lang ? "on" : "", p[1]);
      b.type = "button";
      b.addEventListener("click", function () { state.lang = p[0]; render(); });
      tabs.appendChild(b);
    });
    wrap.appendChild(tabs);

    var store = state.tr[state.lang];
    if (!store) {
      wrap.appendChild(el("p", "empty", t("loading_tr")));
      api("?a=load&f=" + state.lang).then(function (r) {
        if (!r.ok) return;
        state.tr[state.lang] = { data: r.data, sha: r.sha };
        render();
      });
      return wrap;
    }

    var rows = leaves(state.data[state.rec], "", []).filter(function (pair) {
      /* No point asking for four translations of a line that reaches no page. */
      return !UNPRINTED[state.name + "." + pair[0].split(".")[0]];
    });
    if (!rows.length) { wrap.appendChild(el("p", "empty", t("nothing_tr"))); return wrap; }

    rows.forEach(function (pair) {
      var id = state.name + "." + state.rec + "." + pair[0];
      var english = pair[1];
      var rec = store.data[id];
      var tr = el("div", "tr");
      var top = el("div", "top");
      top.appendChild(el("span", "lbl", pair[0]));
      /* Three states, three different jobs: write this, check this, nothing to
         do. Decided by the fingerprint the build uses, computed here -- see
         fingerprint(). An edit made in this session is caught by `src`
         without waiting for the digest. */
      var badge = el("span", "tag bad", t("tr_none"));
      top.appendChild(badge);
      var setBadge = function (cls, key) {
        badge.className = "tag " + cls;
        badge.textContent = t(key);
      };
      var fresh = function () {
        /* A machine line is finished as far as the site is concerned -- the
           page will not be in English -- but it is not the same claim as a
           line somebody read. Its own badge, so the two never look alike. */
        setBadge(rec.by === "machine" ? "mach" : "ok",
                 rec.by === "machine" ? "tr_machine" : "tr_ok");
      };
      if (!rec || !rec.t) setBadge("bad", "tr_none");
      else if (rec.src != null && rec.src !== english) setBadge("warn", "tr_stale");
      else {
        setBadge("", "tr_checking");
        fingerprint(english).then(function (h) {
          if (h === null) setBadge("warn", "tr_unknown");
          else if (rec.en && rec.en === h) fresh();
          else setBadge("warn", "tr_stale");
        });
      }
      tr.appendChild(top);
      tr.appendChild(el("div", "en", english));
      var ta = el("textarea");
      ta.rows = Math.min(10, Math.max(2, Math.ceil(english.length / 70)));
      ta.value = (rec && rec.t) || "";
      ta.addEventListener("input", function () {
        /* Touched by a person, so it stops being a machine line. `by` is
           simply left off rather than set to "human": absent is what every
           translation written before this feature existed looks like. */
        store.data[id] = { en: (rec && rec.en) || "", t: ta.value, src: english };
        store.dirty = true;
        if (rec) rec.by = undefined;
        setBadge("ok", "tr_ok");
        markDirty();
      });
      tr.appendChild(ta);
      wrap.appendChild(tr);
    });
    return wrap;
  }

  /* ------------------------------------------------------------- saving */

  $("#revert").addEventListener("click", function () {
    if (!confirm(t("ask_discard"))) return;
    state.dirty = false;
    open(state.name);
  });

  function autoTranslate() {
    try { return localStorage.getItem("cms_auto") !== "0"; } catch (e) { return true; }
  }

  /* Everything in this record that would otherwise render in English: no
     translation at all, or one made from English that has since changed. The
     fingerprint decides, the same one the build uses. */
  function needsTranslation(storeData, rows) {
    return Promise.all(rows.map(function (pair) {
      var id = state.name + "." + state.rec + "." + pair[0];
      var rec = storeData[id];
      if (!rec || !rec.t) return { id: id, text: pair[1] };
      if (rec.src != null && rec.src !== pair[1]) return { id: id, text: pair[1] };
      return fingerprint(pair[1]).then(function (h) {
        if (h !== null && rec.en === h) return null;     /* current, leave it */
        return { id: id, text: pair[1] };
      });
    })).then(function (list) { return list.filter(Boolean); });
  }

  /* Fill every language before anything is written. Order matters and it is
     the opposite of what it was: the stores are saved BEFORE the content file,
     so the commit that starts the rebuild already has the translations beside
     it. Saved the other way round there is a window -- a minute or two of a
     Russian page with an English line on it, which is the thing this feature
     exists to remove. */
  function translateAll() {
    if (!autoTranslate() || MINE.indexOf(state.name) < 0) return Promise.resolve();
    var rows = leaves(state.data[state.rec], "", []).filter(function (pair) {
      return !UNPRINTED[state.name + "." + pair[0].split(".")[0]];
    });
    if (!rows.length) return Promise.resolve();

    return TR_LANGS.reduce(function (chain, pair) {
      var code = pair[0];
      return chain.then(function () {
        var load = state.tr[code]
          ? Promise.resolve(state.tr[code])
          : api("?a=load&f=" + code).then(function (r) {
              if (!r.ok) return null;
              state.tr[code] = { data: r.data, sha: r.sha };
              return state.tr[code];
            });
        return load.then(function (store) {
          if (!store) return;
          return needsTranslation(store.data, rows).then(function (items) {
            if (!items.length) return;
            say("translating", "dirty", pair[1]);
            return api("?a=translate&to=" + code.replace("t-", ""), {
              method: "POST",
              headers: { "content-type": "application/json" },
              body: JSON.stringify({ items: items }),
            }).then(function (r) {
              if (!r.ok || !r.out) { translateAll.failed = true; return; }
              return Promise.all(Object.keys(r.out).map(function (id) {
                var src = (items.filter(function (i) { return i.id === id; })[0] || {}).text;
                return fingerprint(src || "").then(function (h) {
                  store.data[id] = { en: h || "", t: r.out[id], by: "machine" };
                });
              })).then(function () { store.dirty = true; });
            });
          });
        });
      });
    }, Promise.resolve());
  }

  $("#save").addEventListener("click", function () {
    var btn = $("#save");
    btn.disabled = true;
    say("saving");

    translateAll.failed = false;
    /* Translate, then write the stores, then write the content LAST. The
       content commit is what starts the rebuild, so by the time it lands the
       translations are already beside it and no page is built with an English
       line in it. The first version saved content first, on the reasoning that
       a translation pointing at unsaved content points at nothing -- true, and
       the lesser of the two problems: a store ahead of its content reads as
       stale and falls back to English, which is exactly where it was anyway. */
    translateAll().then(function () {
      return Object.keys(state.tr).filter(function (l) { return state.tr[l].dirty; })
        .reduce(function (chain, l) {
          return chain.then(function () {
            var st = state.tr[l];
            /* `src` is this page's bookkeeping and has no business in the file:
               the build reads `en`, `t` and `by`, and nothing else. */
            var clean = {};
            Object.keys(st.data).forEach(function (key) {
              var r = st.data[key];
              clean[key] = { en: r.en || "", t: r.t };
              if (r.by) clean[key].by = r.by;
            });
            return post(l, clean, st.sha).then(function (rr) {
              if (!rr.ok) throw rr;
              st.sha = rr.sha; st.dirty = false;
            });
          });
        }, Promise.resolve());
    }).then(function () {
      return post(state.name, state.data, state.sha).then(function (r) {
        if (!r.ok) throw r;
        state.sha = r.sha;
      });
    }).then(function () {
      state.dirty = false;
      /* A failed translation is not a failed save: the content went in and the
         page will show English for those lines. Say which it is rather than
         "saved" over the top of it. */
      say(translateAll.failed ? "tr_failed" : "saved_msg",
          translateAll.failed ? "warn" : "ok");
      btn.disabled = false;
      render();
    }).catch(function (r) {
      btn.disabled = false;
      if (r && r.status === 409) say("conflict", "bad");
      else say("not_saved", "bad", (r && r.error) || "");
    });
  });

  function post(name, data, sha) {
    return api("?a=save&f=" + encodeURIComponent(name), {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ data: data, sha: sha, message: "Edit " + name }),
    });
  }

  window.addEventListener("beforeunload", function (e) {
    if (state.dirty) { e.preventDefault(); e.returnValue = ""; }
  });

  /* --------------------------------------------------------------- boot */

  document.documentElement.lang = UI_LANGS[lang][0];
  paintStatic();
  api("?a=session").then(function (r) {
    if (r.signedIn) { start(); return; }
    if (!r.configured) gateSay("not_set_up");
  });
})();
