/* The editor. One file, no framework, no CDN.
 *
 * The site makes no third-party request and this page is part of the site, so
 * it does not get to be the exception. Everything here is what the browser
 * already has.
 *
 * WHAT IT EDITS
 * The six content files, through /api/cms. The endpoint decides what is
 * reachable -- this page only ever asks for a collection by the names the
 * endpoint itself returns. Nothing here can widen that, which is the point of
 * the rule living there rather than here.
 *
 * HOW THE FORM IS BUILT
 * From the shape of the JSON, not from a schema written twice. A string
 * becomes a box, a list of strings becomes a list of boxes with add and
 * remove, a boolean becomes a checkbox, an ISO date becomes a date field. A
 * key starting with an underscore is structure rather than copy -- it is shown
 * dimmed and, where it has to match something, as a list to pick from.
 *
 * The alternative was a field-by-field description of 715 fields kept in step
 * with the files by hand. It would have been out of date the first time a
 * record gained a line.
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

  /* Names the client reads, for the files the build reads. The key is the
     endpoint's own name for the collection. */
  var TITLES = {
    positions: "Вакансии", articles: "Новости", services: "Услуги",
    cases: "Проекты", sectors: "Отрасли", site: "Тексты сайта",
    "t-ru": "Переводы · русский", "t-fr": "Переводы · французский",
    "t-de": "Переводы · немецкий", "t-it": "Переводы · итальянский",
  };
  var MINE = ["positions", "articles"];
  var LANGS = [["t-ru", "RU"], ["t-fr", "FR"], ["t-de", "DE"], ["t-it", "IT"]];

  /* Field labels. Only the ones whose name would otherwise be a guess -- the
     rest show their own key, which is honest and stays right when a field is
     added. */
  var LABELS = {
    title: "Заголовок", lead: "Вводный абзац", body: "Текст", summary: "Описание",
    needs: "Требования", cat: "Рубрика", alt: "Описание фото (alt)",
    seo: "Заголовок для поиска", cta: "Призыв к действию", location: "Место работы",
    contract: "Договор", rotation: "Вахта", start: "Начало", rate: "Ставка",
    count: "Количество", nav: "Пункт меню", h1: "Заголовок страницы",
    points: "Пункты", name: "Название", facts: "Факты", label: "Подпись",
    value: "Значение", note: "Примечание",
    _order: "Порядок", _open: "Открыта", _posted: "Опубликовано",
    _valid_through: "Действительна до", _employment_type: "Тип занятости",
    _countries: "Страны", _discipline: "Специальность", _img: "Файл фото",
    _date: "Дата", _iso: "Дата (ISO)", _w: "Ширина", _h: "Высота",
  };

  /* Fields whose value has to match something else exactly. _discipline is the
     one that breaks visibly: it has to equal an option in the application
     form's list or the Apply button on that vacancy selects nothing, and a
     text box invites a typo that nobody sees until somebody tries to apply.
     The options come from content/site.json, loaded once and only if a field
     that needs them is drawn. */
  var CHOICES = {
    _discipline: ["site", ["form_options", "disciplines"]],
    _employment_type: [null, ["FULL_TIME", "PART_TIME", "CONTRACTOR",
                              "TEMPORARY", "INTERN", "OTHER"]],
  };

  /* Copy that is in the files on purpose and printed nowhere today. Saying so
     is the point: without it the client translates a line into four languages
     and never finds it on the site. The reason is the comment above the field
     in tools/build-pages.py, shortened. */
  var UNPRINTED = {
    "positions.count": "Сейчас на сайте не выводится — строку убрали из карточки. " +
                       "Формулировка оставлена в файле на случай, если понадобится.",
  };

  var state = {
    name: null,      /* collection open */
    data: null,      /* its JSON, as edited */
    clean: null,     /* the same as loaded, for Отменить */
    sha: null,
    rec: null,       /* record slug selected */
    lang: "t-ru",
    tr: {},          /* lang -> {data, sha, clean} */
    dirty: false,
  };

  /* ------------------------------------------------------------ plumbing */

  function api(path, opts) {
    return fetch(API + path, Object.assign({ credentials: "same-origin" }, opts || {}))
      .then(function (r) {
        return r.json().catch(function () { return {}; })
          .then(function (j) { j.status = r.status; return j; });
      });
  }

  function say(text, kind) {
    var s = $("#state");
    s.textContent = text || "";
    s.className = "state" + (kind ? " " + kind : "");
  }

  function markDirty() {
    state.dirty = true;
    say("Есть несохранённые изменения", "dirty");
    $("#bar").style.display = "flex";
  }

  /* ------------------------------------------------------------ the gate */

  $("#login").addEventListener("submit", function (e) {
    e.preventDefault();
    var msg = $("#gate-msg");
    msg.className = "msg";
    msg.textContent = "Проверяем…";
    api("?a=login", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ password: $("#pw").value }),
    }).then(function (r) {
      if (r.ok) { $("#pw").value = ""; start(); return; }
      msg.textContent = r.status === 503
        ? "Редактор ещё не настроен на этом сайте."
        : "Неверный пароль.";
    }).catch(function () { msg.textContent = "Сеть недоступна."; });
  });

  $("#out").addEventListener("click", function () {
    api("?a=logout", { method: "POST" }).then(function () { location.reload(); });
  });

  /* --------------------------------------------------------- the collections */

  function start() {
    api("?a=list").then(function (r) {
      if (!r.ok) { location.reload(); return; }
      $("#gate").style.display = "none";
      $("#app").classList.add("on");
      var mine = $("#rail-mine"), rest = $("#rail-rest");
      mine.innerHTML = rest.innerHTML = "";
      r.collections.forEach(function (n) {
        if (n.indexOf("t-") === 0) return;        /* reached from a record */
        var b = el("button", "", TITLES[n] || n);
        b.dataset.name = n;
        b.addEventListener("click", function () { open(n); });
        (MINE.indexOf(n) >= 0 ? mine : rest).appendChild(b);
      });
      open(MINE[0]);
    });
  }

  function open(name) {
    if (state.dirty && !confirm("Изменения не сохранены. Уйти и потерять их?")) return;
    state.name = name; state.rec = null; state.dirty = false; state.tr = {};
    $("#bar").style.display = "none";
    Array.prototype.forEach.call(document.querySelectorAll("#rail button[data-name]"),
      function (b) { b.classList.toggle("on", b.dataset.name === name); });
    $("#main").innerHTML = "";
    $("#main").appendChild(el("p", "lbl", "Загружаем…"));
    api("?a=load&f=" + encodeURIComponent(name)).then(function (r) {
      if (!r.ok) { $("#main").innerHTML = ""; $("#main").appendChild(el("p", "msg", r.error || "Не удалось загрузить")); return; }
      state.data = r.data;
      state.clean = JSON.parse(JSON.stringify(r.data));
      state.sha = r.sha;
      if (Array.isArray(r.data._order) && r.data._order.length) state.rec = r.data._order[0];
      render();
    });
  }

  /* ------------------------------------------------------------- rendering */

  function render() {
    var m = $("#main");
    m.innerHTML = "";
    var head = el("div", "head");
    head.appendChild(el("h1", "", TITLES[state.name] || state.name));
    head.appendChild(el("span", "sp"));
    m.appendChild(head);

    if (!Array.isArray(state.data._order)) {     /* site.json and friends */
      var box = el("div", "fields");
      fieldsInto(box, state.data, []);
      m.appendChild(box);
      return;
    }

    var cols = el("div", "cols");
    cols.appendChild(recordList());
    var right = el("div");
    if (state.rec) {
      var f = el("div", "fields");
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
      var row = el("div", "rec" + (slug === state.rec ? " on" : ""));
      var up = el("button", "mv", "↑"), dn = el("button", "mv", "↓");
      up.type = dn.type = "button";
      up.title = "Выше"; dn.title = "Ниже";
      if (i === 0) up.disabled = true;
      if (i === state.data._order.length - 1) dn.disabled = true;
      up.addEventListener("click", function () { move(i, -1); });
      dn.addEventListener("click", function () { move(i, 1); });
      var nm = el("button", "nm", (state.data[slug] || {}).title || slug);
      nm.type = "button";
      nm.addEventListener("click", function () { state.rec = slug; render(); });
      var rm = el("button", "mv", "×");
      rm.type = "button"; rm.title = "Удалить";
      rm.addEventListener("click", function () { removeRecord(slug); });
      row.appendChild(up); row.appendChild(dn); row.appendChild(nm); row.appendChild(rm);
      wrap.appendChild(row);
    });
    var add = el("button", "add", "+ Добавить");
    add.type = "button";
    add.addEventListener("click", addRecord);
    wrap.appendChild(add);
    return wrap;
  }

  function move(i, d) {
    var o = state.data._order, j = i + d;
    if (j < 0 || j >= o.length) return;
    var t = o[i]; o[i] = o[j]; o[j] = t;
    markDirty(); render();
  }

  function addRecord() {
    var slug = prompt("Короткое имя латиницей, из него получится адрес страницы:\n" +
                      "например  crane-foundation-package");
    if (!slug) return;
    slug = slug.trim().toLowerCase().replace(/[^a-z0-9-]+/g, "-").replace(/^-|-$/g, "");
    if (!slug) { alert("Такое имя не подходит."); return; }
    if (state.data[slug]) { alert("Запись с таким именем уже есть."); return; }
    /* Copied from the first record and emptied, so a new one has every field
       the build expects. Inventing the shape here would mean describing it
       twice and getting it wrong the first time a field is added. */
    var model = state.data[state.data._order[0]] || {};
    state.data[slug] = blank(model);
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
    if (!confirm("Удалить «" + ((state.data[slug] || {}).title || slug) +
                 "»?\n\nПосле сохранения страница пропадёт с сайта и из карты сайта," +
                 " на всех языках.")) return;
    delete state.data[slug];
    state.data._order = state.data._order.filter(function (s) { return s !== slug; });
    if (state.rec === slug) state.rec = state.data._order[0] || null;
    markDirty(); render();
  }

  /* ---------------------------------------------------------- the fields */

  function labelFor(key) { return LABELS[key] || key; }

  function fieldsInto(box, obj, path) {
    /* Copy first, structure after. The file's own key order puts _discipline
       above the title on a vacancy, which is the build's order of business and
       not the client's -- he came to change a sentence. Underscore keys keep
       their own relative order among themselves, so the dates stay in the
       sequence somebody chose. */
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
          fieldsInto(sub, item, path.concat(i));
          g.appendChild(sub);
          return;
        }
        var row = el("div", "list-item");
        var ta = el("textarea"); ta.value = item; ta.rows = 2;
        ta.addEventListener("input", function () { v[i] = ta.value; markDirty(); });
        var x = el("button", "btn btn-s", "×"); x.type = "button";
        x.addEventListener("click", function () { v.splice(i, 1); markDirty(); render(); });
        row.appendChild(ta); row.appendChild(x);
        g.appendChild(row);
      });
      if (!v.length || typeof v[0] !== "object") {
        var plus = el("button", "btn btn-s", "+ строка"); plus.type = "button";
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
        var blankOpt = el("option", "", "— не выбрано —");
        blankOpt.value = "";
        sel.appendChild(blankOpt);
        opts.forEach(function (o) {
          var op = el("option", "", o);
          op.value = o;
          if (o === v) op.selected = true;
          sel.appendChild(op);
        });
        /* A value already in the file that is not on the list is kept and
           shown as wrong, never silently replaced: it is somebody's data, and
           the one thing worse than a bad value is losing it on open. */
        if (v && opts.indexOf(v) < 0) {
          var odd = el("option", "", v + "  (нет в списке)");
          odd.value = v; odd.selected = true;
          sel.appendChild(odd);
        }
      };
      sel.addEventListener("change", function () { parent[k] = sel.value; markDirty(); });
      var spec = CHOICES[key];
      if (spec[0] === null) fill(spec[1]);
      else {
        fill(v ? [v] : []);
        choices(spec[0], spec[1]).then(fill);
      }
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
    if (un) f.appendChild(el("div", "hint", un));
    return f;
  }

  /* The photograph. It goes up as the original the phone produced; the build
     derives the sizes the page needs and reads the real pixel dimensions off
     the result, so the width and height fields are not something to type.
     Which is why they are not offered: they were typed once, disagreed with
     the file, and the news cards served 600px images into 626px boxes. */
  function photoPicker(parent, k, pathInput) {
    var wrap = el("div");
    var row = el("div", "list-item");
    var pick = el("button", "btn btn-s", "Загрузить фото");
    pick.type = "button";
    var file = el("input");
    file.type = "file";
    file.accept = "image/jpeg,image/png,image/webp";
    file.style.display = "none";
    var note = el("span", "hint");
    note.style.flex = "1";
    note.textContent = "JPEG, PNG или WebP, до 12 МБ. Размеры посчитает сборка.";

    pick.addEventListener("click", function () { file.click(); });
    file.addEventListener("change", function () {
      var f = file.files && file.files[0];
      if (!f) return;
      pick.disabled = true;
      note.textContent = "Загружаем " + f.name + "…";
      /* The bytes, raw. No multipart and no base64 on the way up: the endpoint
         sniffs the magic numbers, so the body is the file and nothing else. */
      api("?a=upload&name=" + encodeURIComponent(f.name), {
        method: "POST",
        headers: { "content-type": "application/octet-stream" },
        body: f,
      }).then(function (r) {
        pick.disabled = false;
        file.value = "";
        if (!r.ok) { note.textContent = "Не загрузилось: " + (r.error || "ошибка"); return; }
        parent[k] = r.img;
        pathInput.value = r.img;
        note.textContent = "Загружено. Фото появится на сайте после сохранения.";
        markDirty();
      }).catch(function () {
        pick.disabled = false;
        note.textContent = "Не загрузилось: нет связи";
      });
    });

    row.appendChild(pick); row.appendChild(note);
    wrap.appendChild(row); wrap.appendChild(file);
    return wrap;
  }

  /* Option lists, fetched once. Kept outside `state` because they belong to
     the site rather than to whatever is open. */
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
    var wrap = el("div", "fields");
    wrap.style.marginTop = "22px";
    var tabs = el("div", "tabs");
    LANGS.forEach(function (p) {
      var b = el("button", p[0] === state.lang ? "on" : "", p[1]);
      b.type = "button";
      b.addEventListener("click", function () { state.lang = p[0]; render(); });
      tabs.appendChild(b);
    });
    wrap.appendChild(tabs);

    var store = state.tr[state.lang];
    if (!store) {
      wrap.appendChild(el("p", "lbl", "Загружаем переводы…"));
      api("?a=load&f=" + state.lang).then(function (r) {
        if (!r.ok) return;
        state.tr[state.lang] = { data: r.data, sha: r.sha };
        render();
      });
      return wrap;
    }

    var rows = leaves(state.data[state.rec], "", []);
    if (!rows.length) { wrap.appendChild(el("p", "lbl", "Переводить нечего")); return wrap; }

    rows = rows.filter(function (pair) {
      /* No point asking for four translations of a line that reaches no page.
         The field itself is still editable above -- it is in the file on
         purpose -- it just does not go to a translator. */
      return !UNPRINTED[state.name + "." + pair[0].split(".")[0]];
    });

    rows.forEach(function (pair) {
      var id = state.name + "." + state.rec + "." + pair[0];
      var english = pair[1];
      var rec = store.data[id];
      var tr = el("div", "tr");
      var head = el("div");
      head.appendChild(el("span", "lbl", pair[0]));
      /* Three states, and they are three different jobs. The fingerprint is
         computed by the build, not here -- this page can only say whether a
         record exists and whether the English it was made from is still the
         English on screen, which is the same question with a cheaper answer:
         the stored English is not kept, so a changed record shows as "check". */
      var tag, cls;
      if (!rec || !rec.t) { tag = "нет перевода"; cls = "bad"; }
      else if (rec.src != null && rec.src !== english) { tag = "английский изменился"; cls = "warn"; }
      else { tag = "переведено"; cls = "ok"; }
      head.appendChild(el("span", "tag " + cls, tag));
      tr.appendChild(head);
      tr.appendChild(el("div", "en", english));
      var ta = el("textarea");
      ta.rows = Math.min(10, Math.max(2, Math.ceil(english.length / 70)));
      ta.value = (rec && rec.t) || "";
      ta.addEventListener("input", function () {
        /* `src` is what this page just saw in English. The server recomputes
           the fingerprint on its own terms; this is only so the panel can show
           a changed line without another round trip. */
        store.data[id] = { en: (rec && rec.en) || "", t: ta.value, src: english };
        store.dirty = true;
        markDirty();
      });
      tr.appendChild(ta);
      wrap.appendChild(tr);
    });
    return wrap;
  }

  /* ------------------------------------------------------------- saving */

  $("#revert").addEventListener("click", function () {
    if (!confirm("Вернуть всё как было при открытии?")) return;
    open(state.name);
  });

  $("#save").addEventListener("click", function () {
    var btn = $("#save");
    btn.disabled = true;
    say("Сохраняем…");

    /* The record file first. If it fails nothing else is sent: a translation
       saved against content that did not save is a line pointing at nothing. */
    post(state.name, state.data, state.sha).then(function (r) {
      if (!r.ok) throw r;
      state.sha = r.sha;
      var pending = Object.keys(state.tr).filter(function (l) { return state.tr[l].dirty; });
      return pending.reduce(function (chain, l) {
        return chain.then(function () {
          var s = state.tr[l];
          /* `src` is this page's own bookkeeping and has no business in the
             file. The build reads `en` and `t`, and nothing else. */
          var clean = {};
          Object.keys(s.data).forEach(function (k) {
            clean[k] = { en: s.data[k].en || "", t: s.data[k].t };
          });
          return post(l, clean, s.sha).then(function (rr) {
            if (!rr.ok) throw rr;
            s.sha = rr.sha; s.dirty = false;
          });
        });
      }, Promise.resolve());
    }).then(function () {
      state.dirty = false;
      state.clean = JSON.parse(JSON.stringify(state.data));
      say("Сохранено. Сайт пересоберётся за пару минут.", "ok");
      btn.disabled = false;
    }).catch(function (r) {
      btn.disabled = false;
      say(r && r.status === 409
        ? "Кто-то сохранил это, пока страница была открыта. Обновите страницу."
        : "Не сохранилось: " + ((r && r.error) || "нет связи"), "bad");
    });
  });

  function post(name, data, sha) {
    return api("?a=save&f=" + encodeURIComponent(name), {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ data: data, sha: sha,
                             message: "Правка: " + (TITLES[name] || name) }),
    });
  }

  window.addEventListener("beforeunload", function (e) {
    if (state.dirty) { e.preventDefault(); e.returnValue = ""; }
  });

  /* --------------------------------------------------------------- boot */

  api("?a=session").then(function (r) {
    if (r.signedIn) { start(); return; }
    if (!r.configured)
      $("#gate-msg").textContent = "Редактор ещё не настроен на этом сайте.";
  });
})();
