# Visualizador de IAC

Selecione um conector para inspecionar o JSON de IAC exportado.

<div id="iac-viewer">
  <div class="iac-controls">
    <select id="iac-select"><option value="">Selecione um conector…</option></select>
    <input id="iac-search" type="search" placeholder="Buscar chave ou valor…" disabled>
  </div>
  <div id="iac-status"></div>
  <div id="iac-tree"></div>
</div>

<style>
#iac-viewer { font-family: var(--md-text-font-family, sans-serif); }
.iac-controls { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
.iac-controls select, .iac-controls input { padding: 0.4rem; font-size: 0.9rem; }
#iac-status { font-size: 0.85rem; opacity: 0.7; margin-bottom: 0.5rem; }
#iac-tree { font-family: var(--md-code-font-family, monospace); font-size: 0.85rem; }
.iac-node-header { cursor: pointer; user-select: none; }
.iac-node-header:hover { text-decoration: underline; }
.iac-toggle { display: inline-block; width: 1rem; }
.iac-children { margin-left: 1.25rem; }
.iac-children.iac-collapsed { display: none; }
.iac-leaf { margin-left: 1.25rem; }
.iac-key { font-weight: 600; }
.iac-match { background: rgba(255, 220, 0, 0.35); border-radius: 2px; }
</style>

<script>
(function () {
  var select = document.getElementById('iac-select');
  var search = document.getElementById('iac-search');
  var status = document.getElementById('iac-status');
  var tree = document.getElementById('iac-tree');
  var currentData = null;

  function nodeMatches(key, value, query) {
    if (!query) return true;
    var q = query.toLowerCase();
    if (String(key).toLowerCase().indexOf(q) !== -1) return true;
    if (value !== null && typeof value === 'object') {
      var entries = Array.isArray(value)
        ? value.map(function (v, i) { return [i, v]; })
        : Object.entries(value);
      for (var i = 0; i < entries.length; i++) {
        if (nodeMatches(entries[i][0], entries[i][1], query)) return true;
      }
      return false;
    }
    return String(value).toLowerCase().indexOf(q) !== -1;
  }

  function highlight(text, query) {
    if (!query) return text;
    var q = query.toLowerCase();
    var idx = text.toLowerCase().indexOf(q);
    if (idx === -1) return text;
    var span = document.createElement('span');
    span.appendChild(document.createTextNode(text.slice(0, idx)));
    var mark = document.createElement('span');
    mark.className = 'iac-match';
    mark.textContent = text.slice(idx, idx + query.length);
    span.appendChild(mark);
    span.appendChild(document.createTextNode(text.slice(idx + query.length)));
    return span;
  }

  function appendText(el, textOrNode) {
    if (typeof textOrNode === 'string') {
      el.appendChild(document.createTextNode(textOrNode));
    } else {
      el.appendChild(textOrNode);
    }
  }

  function renderNode(key, value, container, query, depth) {
    if (!nodeMatches(key, value, query)) return;
    var item = document.createElement('div');
    item.className = 'iac-node';

    if (value !== null && typeof value === 'object') {
      var isArray = Array.isArray(value);
      var entries = isArray
        ? value.map(function (v, i) { return [i, v]; })
        : Object.entries(value);

      var toggle = document.createElement('span');
      toggle.className = 'iac-toggle';
      var expanded = Boolean(query) || depth < 1;
      toggle.textContent = expanded ? '▾' : '▸';

      var label = document.createElement('span');
      label.className = 'iac-key';
      appendText(label, highlight(String(key), query));
      var countLabel = document.createElement('span');
      countLabel.textContent = ' ' + (isArray ? '[' + entries.length + ']' : '{' + entries.length + '}');

      var header = document.createElement('div');
      header.className = 'iac-node-header';
      header.appendChild(toggle);
      header.appendChild(label);
      header.appendChild(countLabel);

      var children = document.createElement('div');
      children.className = 'iac-children' + (expanded ? '' : ' iac-collapsed');
      entries.forEach(function (entry) {
        renderNode(entry[0], entry[1], children, query, depth + 1);
      });

      header.addEventListener('click', function () {
        var collapsed = children.classList.toggle('iac-collapsed');
        toggle.textContent = collapsed ? '▸' : '▾';
      });

      item.appendChild(header);
      item.appendChild(children);
    } else {
      var row = document.createElement('div');
      row.className = 'iac-leaf';
      var keySpan = document.createElement('span');
      keySpan.className = 'iac-key';
      appendText(keySpan, highlight(String(key), query));
      row.appendChild(keySpan);
      row.appendChild(document.createTextNode(': '));
      var valueSpan = document.createElement('span');
      valueSpan.className = 'iac-value';
      appendText(valueSpan, highlight(JSON.stringify(value), query));
      row.appendChild(valueSpan);
      item.appendChild(row);
    }

    container.appendChild(item);
  }

  function render(query) {
    tree.innerHTML = '';
    if (!currentData) return;
    renderNode(currentData.__slug, currentData.value, tree, query || '', 0);
  }

  search.addEventListener('input', function () {
    render(search.value.trim());
  });

  select.addEventListener('change', function () {
    var slug = select.value;
    tree.innerHTML = '';
    if (!slug) {
      currentData = null;
      search.disabled = true;
      return;
    }
    status.textContent = 'Carregando ' + slug + '…';
    fetch('../iac-data/' + encodeURIComponent(slug) + '.json')
      .then(function (res) { return res.json(); })
      .then(function (data) {
        currentData = { __slug: slug, value: data };
        search.disabled = false;
        search.value = '';
        status.textContent = '';
        render('');
      })
      .catch(function (err) {
        status.textContent = 'Falha ao carregar ' + slug + ': ' + err;
      });
  });

  fetch('../iac-data/index.json')
    .then(function (res) { return res.json(); })
    .then(function (slugs) {
      if (!slugs.length) {
        status.textContent = 'Nenhum JSON de IAC encontrado em iac/.';
        return;
      }
      slugs.forEach(function (slug) {
        var option = document.createElement('option');
        option.value = slug;
        option.textContent = slug;
        select.appendChild(option);
      });
    })
    .catch(function (err) {
      status.textContent = 'Falha ao carregar lista de conectores: ' + err;
    });
})();
</script>
