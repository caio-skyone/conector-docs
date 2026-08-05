# Reformulação studio-templates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reformular o repositório `conector-docs` em `studio-templates`: rename completo, reestruturação de docs em camadas (conectores / fluxo de desenvolvimento / IAC), pasta `iac/` como source of truth dos JSONs exportados, e um viewer standalone desses JSONs no mkdocs.

**Architecture:** Site mkdocs-material estático. Um hook nativo do mkdocs (`hooks/iac_assets.py`, evento `on_post_build`) copia `iac/*.json` para `site/iac-data/` e gera um índice, sem depender de plugins extras. A página `docs/iac-viewer.md` é HTML/JS/CSS inline, self-contained, que busca esses assets via fetch relativo.

**Tech Stack:** mkdocs 1.6, mkdocs-material, plugin `roamlinks` (já usado), Python (hook), HTML/vanilla JS (viewer).

## Global Constraints

- Este é um projeto de docs/markdown estáticos — não há lógica de aplicação para testar com suíte de testes automatizada. Verificação = `uv run mkdocs build --strict` (sem warnings) + inspeção manual do output/HTML gerado. Não criar testes artificiais.
- Nenhuma página de conector (`docs/connectors/*.md`) deve linkar para `docs/iac-viewer.md`.
- `iac/` não deve ser duplicada manualmente dentro de `docs/`; a injeção no build é feita só pelo hook.
- Manter `docs/callback/` com o mesmo conteúdo, apenas movida para `docs/dev-flow/callback/` (sem reescrever texto).
- Imagens usam sintaxe wikilink (colchetes duplos ao redor do nome do arquivo de imagem) resolvida pelo plugin `roamlinks` por nome de arquivo em toda a árvore de `docs/` — mover arquivos de página não quebra esses links, mas confirmar com o build.

---

### Task 1: Rename connector-docs → studio-templates

**Files:**
- Modify: `pyproject.toml`
- Modify: `mkdocs.yml`
- Modify: `README.md`

**Interfaces:** N/A (config/metadata only).

- [ ] **Step 1: Atualizar `pyproject.toml`**

Em `pyproject.toml`, trocar:

```toml
[project]
name = "conector-docs"
```

por:

```toml
[project]
name = "studio-templates"
```

- [ ] **Step 2: Atualizar `mkdocs.yml`**

Trocar as duas primeiras linhas de `mkdocs.yml`:

```yaml
site_name: Conector Docs
site_url: https://caio-skyone.github.io/conector-docs/
```

por:

```yaml
site_name: Studio Templates
site_url: https://caio-skyone.github.io/studio-templates/
```

(O restante do arquivo — `theme`, `plugins` — fica igual por enquanto; será expandido nas próximas tasks.)

- [ ] **Step 3: Reescrever `README.md`**

Substituir todo o conteúdo de `README.md` por:

```markdown
# studio-templates

Repositório de documentação e fluxo de desenvolvimento dos templates do
Skyone Studio — conectores REST e, futuramente, outros tipos de template.

## Estrutura

- `docs/connectors/` — documentação de cada conector publicado
- `docs/dev-flow/` — guias de apoio ao desenvolvimento de templates (ex: OAuth2/callback)
- `docs/iac-viewer.md` — visualizador dos JSONs de IAC exportados (`iac/`)
- `iac/` — JSONs de IAC exportados por conector (source of truth)
- `.claude/skills/` — skills do Claude Code que guiam plan → build → publish → account → document

## Fluxo de incremento das documentações

Crie a sua branch com o nome da plataforma alvo -> Adicione o arquivo markdown em `docs/connectors/` -> merge na main quando a documentação estiver pronta -> github actions inicia o novo deploy da documentação

Acesse em [Studio Templates](https://caio-skyone.github.io/studio-templates/)
```

- [ ] **Step 4: Verificar**

Run: `grep -rn "conector-docs" pyproject.toml mkdocs.yml README.md`
Expected: nenhum resultado (todas as ocorrências substituídas).

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml mkdocs.yml README.md
git commit -m "Rename project from conector-docs to studio-templates"
```

---

### Task 2: Reestruturar docs em camadas (connectors/ e dev-flow/)

**Files:**
- Move: `docs/databricks.md` → `docs/connectors/databricks.md`
- Move: `docs/github.md` → `docs/connectors/github.md`
- Move: `docs/ifood.md` → `docs/connectors/ifood.md`
- Move: `docs/mailgun.md` → `docs/connectors/mailgun.md`
- Move: `docs/notion.md` → `docs/connectors/notion.md`
- Move: `docs/service-now.md` → `docs/connectors/service-now.md`
- Move: `docs/twilio.md` → `docs/connectors/twilio.md`
- Move: `docs/xero.md` → `docs/connectors/xero.md`
- Move: `docs/zoho-books.md` → `docs/connectors/zoho-books.md`
- Move: `docs/zoho-projects.md` → `docs/connectors/zoho-projects.md`
- Move: `docs/callback/contexto.md` → `docs/dev-flow/callback/contexto.md`
- Move: `docs/callback/oauth2postman.md` → `docs/dev-flow/callback/oauth2postman.md`
- Modify: `mkdocs.yml` (add explicit `nav:`)

> `docs/zoho-analytics.md` and `docs/callback/studio api gateway.md` were
> already removed in a prior cleanup commit (broken links/image with no
> fix available) — they no longer exist and are not part of this move.

**Interfaces:** N/A (file moves + nav config).

- [ ] **Step 1: Mover os markdowns de conector**

```bash
mkdir -p docs/connectors
git mv docs/databricks.md docs/connectors/databricks.md
git mv docs/github.md docs/connectors/github.md
git mv docs/ifood.md docs/connectors/ifood.md
git mv docs/mailgun.md docs/connectors/mailgun.md
git mv docs/notion.md docs/connectors/notion.md
git mv docs/service-now.md docs/connectors/service-now.md
git mv docs/twilio.md docs/connectors/twilio.md
git mv docs/xero.md docs/connectors/xero.md
git mv docs/zoho-books.md docs/connectors/zoho-books.md
git mv docs/zoho-projects.md docs/connectors/zoho-projects.md
```

- [ ] **Step 2: Mover a pasta callback para dev-flow**

```bash
mkdir -p docs/dev-flow
git mv docs/callback docs/dev-flow/callback
```

- [ ] **Step 3: Adicionar nav explícita em `mkdocs.yml`**

Acrescentar ao final de `mkdocs.yml` (após `plugins:`):

```yaml
nav:
- Início: index.md
- Conectores:
  - Databricks: connectors/databricks.md
  - GitHub: connectors/github.md
  - iFood: connectors/ifood.md
  - Mailgun: connectors/mailgun.md
  - Notion: connectors/notion.md
  - Service Now: connectors/service-now.md
  - Twilio: connectors/twilio.md
  - Xero: connectors/xero.md
  - Zoho Books: connectors/zoho-books.md
  - Zoho Projects: connectors/zoho-projects.md
- Fluxo de Desenvolvimento:
  - Callback OAuth2:
    - Contexto: dev-flow/callback/contexto.md
    - Postman: dev-flow/callback/oauth2postman.md
```

(O item **IAC** será adicionado à nav na Task 4, depois que `docs/iac-viewer.md` existir.)

- [ ] **Step 4: Verificar o build**

Run: `uv run mkdocs build --strict`
Expected: build finaliza sem warnings (nenhum link/nav quebrado, nenhuma imagem faltando).

- [ ] **Step 5: Commit**

```bash
git add docs mkdocs.yml
git commit -m "Restructure docs into connectors/ and dev-flow/ layers"
```

---

### Task 3: Hook mkdocs para expor `iac/*.json` no build

**Files:**
- Create: `hooks/iac_assets.py`
- Create: `iac/.gitkeep`
- Modify: `mkdocs.yml` (registrar `hooks:`)

**Interfaces:**
- Produces: durante o build, `site/iac-data/{slug}.json` (cópia de `iac/{slug}.json`) e `site/iac-data/index.json` (lista JSON de slugs, ex: `["databricks", "xero"]`). A Task 4 (viewer) consome esses dois caminhos via `fetch`.

- [ ] **Step 1: Criar `iac/` com placeholder**

```bash
mkdir -p iac
touch iac/.gitkeep
```

(`iac/.gitkeep` mantém a pasta versionada mesmo vazia; será substituído por JSONs reais conforme conectores forem publicados.)

- [ ] **Step 2: Criar o hook `hooks/iac_assets.py`**

```python
"""MkDocs hook: expõe iac/*.json como assets estáticos do build.

Copia cada arquivo de iac/ (raiz do repo) para site/iac-data/ e gera
site/iac-data/index.json com a lista de slugs disponíveis, para a página
docs/iac-viewer.md consumir via fetch. Não duplica os arquivos dentro de
docs/ — a cópia acontece só no momento do build (on_post_build).
"""

import json
import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    repo_root = Path(config.config_file_path).parent
    iac_dir = repo_root / "iac"
    out_dir = Path(config["site_dir"]) / "iac-data"
    out_dir.mkdir(parents=True, exist_ok=True)

    slugs = []
    if iac_dir.is_dir():
        for json_path in sorted(iac_dir.glob("*.json")):
            shutil.copy2(json_path, out_dir / json_path.name)
            slugs.append(json_path.stem)

    (out_dir / "index.json").write_text(
        json.dumps(slugs, ensure_ascii=False, indent=2)
    )
```

- [ ] **Step 3: Registrar o hook em `mkdocs.yml`**

Acrescentar (após `plugins:`, antes de `nav:`):

```yaml
hooks:
- hooks/iac_assets.py
```

- [ ] **Step 4: Verificar com um JSON de exemplo temporário**

```bash
cat > iac/example.json <<'EOF'
{
  "name": "Example Connector",
  "settings": { "authentication_type": "bearer-token" },
  "operations": [
    { "name": "Users - Get all users", "request": { "method": "GET" } }
  ]
}
EOF
uv run mkdocs build --strict
cat site/iac-data/index.json
cat site/iac-data/example.json
rm iac/example.json
```

Expected: `site/iac-data/index.json` contém `["example"]` e
`site/iac-data/example.json` é uma cópia idêntica ao arquivo de origem.
Depois de confirmar, o `example.json` é removido (era só para testar o hook).

- [ ] **Step 5: Commit**

```bash
git add hooks iac mkdocs.yml
git commit -m "Add mkdocs hook to expose iac/*.json as build assets"
```

---

### Task 4: Página standalone do IAC viewer

**Files:**
- Create: `docs/iac-viewer.md`
- Modify: `mkdocs.yml` (adicionar item de nav **IAC**)

**Interfaces:**
- Consumes: `../iac-data/index.json` e `../iac-data/{slug}.json` (produzidos pelo hook da Task 3).

- [ ] **Step 1: Criar `docs/iac-viewer.md`**

```markdown
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
    fetch('../iac-data/' + slug + '.json')
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
```

- [ ] **Step 2: Adicionar o item de nav IAC**

Em `mkdocs.yml`, ao final do bloco `nav:` (depois de `Fluxo de Desenvolvimento`), adicionar:

```yaml
- IAC: iac-viewer.md
```

- [ ] **Step 3: Verificar build e comportamento com dado de exemplo**

```bash
cat > iac/example.json <<'EOF'
{
  "name": "Example Connector",
  "settings": { "authentication_type": "bearer-token" },
  "operations": [
    { "name": "Users - Get all users", "request": { "method": "GET" } }
  ]
}
EOF
uv run mkdocs build --strict
```

Expected: build sem warnings; `site/iac-viewer/index.html` existe e contém o
script inline.

Depois, rodar `uv run mkdocs serve` e no navegador abrir a página **IAC**:
confirmar que o select lista `example`, que escolher `example` renderiza a
árvore colapsável (nós `settings`, `operations` expansíveis), e que digitar
`bearer` no campo de busca destaca o nó `authentication_type`. Encerrar o
`mkdocs serve` (Ctrl+C) e remover o exemplo:

```bash
rm iac/example.json
```

- [ ] **Step 4: Confirmar isolamento (sem link a partir dos conectores)**

Run: `grep -rl "iac-viewer" docs/connectors/`
Expected: nenhum resultado.

- [ ] **Step 5: Commit**

```bash
git add docs/iac-viewer.md mkdocs.yml
git commit -m "Add standalone IAC JSON viewer page"
```

---

> **Nota de escopo:** os arquivos `.claude/skills/studio-connector-*/SKILL.md`
> são gerados/gerenciados pelo `skytk` (toolkit-hub) a partir do toolkit
> remoto `toolkit-studio-connectors` (ver `.toolkit-hub.yaml`) e estão no
> `.gitignore` com aviso explícito "não edite à mão". Alinhar o caminho de
> saída da doc (`iac/docs/{slug}.md` → `docs/connectors/{slug}.md`) e a
> persistência de `iac/{slug}.json` nessas skills fica **fora do escopo
> deste repositório** — precisa ser feito na fonte do toolkit, em outro
> lugar. Nenhuma task deste plano edita esses arquivos.

### Task 5: Verificação final de repositório

**Files:** nenhum (task de verificação, sem alterações de arquivo).

**Interfaces:** N/A.

- [ ] **Step 1: Build estrito completo**

Run: `uv run mkdocs build --strict`
Expected: build finaliza sem warnings.

- [ ] **Step 2: Confirmar ausência de referências antigas**

Run: `grep -rn "conector-docs" . --include="*.md" --include="*.toml" --include="*.yml" --exclude-dir=.git --exclude-dir=site`
Expected: nenhum resultado.

- [ ] **Step 3: Confirmar que `iac/` está versionada e vazia (exceto `.gitkeep`)**

Run: `git status --porcelain iac/ && ls iac/`
Expected: `iac/` sob controle de versão, contendo apenas `.gitkeep` (nenhum
JSON de teste esquecido).

- [ ] **Step 4: Confirmar isolamento do viewer**

Run: `grep -rl "iac-viewer" docs/connectors/ docs/dev-flow/`
Expected: nenhum resultado.

- [ ] **Step 5: Limpar artefato de build local**

```bash
rm -rf site
```

(O diretório `site/` é gerado pelo `mkdocs build`; não deve ser commitado —
confirmar que não está rastreado: `git status --porcelain site` deve ficar
vazio depois do `rm`.)
