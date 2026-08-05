# Reformulação connector-docs → studio-templates

## Contexto

O repositório `conector-docs` hoje é um site mkdocs com documentação markdown
flat (`docs/*.md`, uma por conector) e um conjunto de skills Claude Code
(`studio-connector-plan/build/publish/account/document`) que guiam a criação
de conectores REST no Skyone Studio via MCP. O skill `studio-connector-document`
já referencia um caminho `iac/docs/{slug}.md` que não existe no repo — sinal de
que a estrutura de pastas ficou para trás do que as skills esperam.

O repo vai deixar de ser só docs de conectores para comportar todo o fluxo de
desenvolvimento de templates do Studio, com layout preparado para outros tipos
de template além de conector (mesmo sem tipos concretos definidos ainda), além
de uma forma de expor os JSONs de IAC exportados.

## Escopo

1. Rename completo `connector-docs` → `studio-templates` (pyproject, mkdocs,
   README).
2. Reestruturação de pastas/nav do mkdocs em camadas, isolando docs de
   conector do restante.
3. Pasta `iac/` na raiz do repo como source of truth dos JSONs de IAC
   exportados por conector.
4. Página standalone no mkdocs para visualizar esses JSONs (viewer
   colapsável/pesquisável), sem link a partir das páginas de doc de conector.
5. Atualização das skills afetadas pela mudança de caminho de saída e pela
   nova responsabilidade de persistir o IAC exportado no repo.

Fora de escopo: definir novos tipos de template concretos (só preparar o
layout para comportá-los); documentação humana do fluxo plan→build→publish
(dev-flow index) — descartado nesta rodada.

## Estrutura de pastas e nav

```
docs/
  index.md
  connectors/          # movidos de docs/*.md (databricks.md, github.md, ifood.md, ...)
    {slug}.md
  dev-flow/            # guias de apoio ao desenvolvimento (hoje: callback)
    callback/
      contexto.md
      oauth2postman.md
      studio api gateway.md
  iac-viewer.md         # página standalone — não linkada a partir de connectors/
  img/                  # inalterado (paths de imagem ajustados junto com o move)

iac/                    # novo, raiz do repo — source of truth
  {slug}.json           # JSON de IAC exportado por conector

hooks/
  iac_assets.py          # mkdocs hook (on_files) — injeta iac/*.json no build
```

`docs/callback/` é renomeada para `docs/dev-flow/callback/` (mesmo conteúdo,
só a categorização muda para refletir que é um guia de apoio ao
desenvolvimento, não doc de conector).

Nav do `mkdocs.yml` em blocos top-level:

- **Início** → `index.md`
- **Conectores** → `connectors/*.md`
- **Fluxo de Desenvolvimento** → `dev-flow/callback/*.md`
- **IAC** → `iac-viewer.md` (isolado, sem entrada cruzada com Conectores)

## Rename

- `pyproject.toml`: `name = "studio-templates"`.
- `mkdocs.yml`: `site_name: Studio Templates`; `site_url` atualizada para o
  novo endereço do GitHub Pages (`https://caio-skyone.github.io/studio-templates/`).
- `README.md`: reescrito — repositório agora cobre fluxo de desenvolvimento de
  templates do Studio (não só docs de conector), com layout em camadas
  preparado para outros tipos de template.

## Viewer de IAC

**Problema:** mkdocs só publica arquivos dentro de `docs_dir`; `iac/*.json`
fica fora, pois é versionado como source of truth independente dos docs
renderizados.

**Mecanismo:** hook nativo do mkdocs (`hooks:` no `mkdocs.yml`, disponível
desde mkdocs ≥1.5, sem dependência nova) em `hooks/iac_assets.py`. No evento
`on_files`, o hook:

1. Lista todo `iac/*.json` no repo.
2. Injeta cada arquivo no build como asset estático em `/iac-data/{slug}.json`.
3. Gera `/iac-data/index.json` com a lista de slugs disponíveis.

Nenhum arquivo é duplicado manualmente dentro de `docs/` — a injeção acontece
só no momento do build.

**Página `docs/iac-viewer.md`:** HTML/JS inline, self-contained (sem CDN
externo):

- `<select>` populado via `fetch('iac-data/index.json')`.
- Ao escolher um slug, `fetch('iac-data/{slug}.json')` e renderiza uma árvore
  colapsável (expandir/recolher nós objeto/array).
- Campo de busca com filtro por chave/valor, destacando nós que batem
  (substring match, sem regex).

A página não é referenciada a partir de `docs/connectors/{slug}.md` — só
aparece no item de nav próprio ("IAC").

## Skills afetadas

- `studio-connector-document/SKILL.md`: caminho de saída muda de
  `iac/docs/{slug}.md` para `docs/connectors/{slug}.md`. Ajustar todas as
  referências ao path no arquivo (tabela "Output path", workflow, exemplos).
- `studio-connector-publish/SKILL.md`: adicionar passo, após push/export bem
  sucedido, para persistir o JSON exportado também em `iac/{slug}.json` no
  repo (git-tracked) — é o que alimenta o viewer. Deixar claro que isso é
  além do `export_draft` (que grava em `~/.studio-mcp/exports/`); o agente
  copia/grava o conteúdo para dentro do repo.

Nenhuma outra skill (`plan`, `build`, `account`) referencia caminhos de doc/
IAC no repo, então não precisam de mudança.

## Testando

- `mkdocs build --strict` deve passar sem warnings de nav quebrada após o
  move de `docs/*.md` → `docs/connectors/*.md` e `docs/callback/` →
  `docs/dev-flow/callback/`.
- `mkdocs serve`: navegar Conectores, Fluxo de Desenvolvimento e IAC
  manualmente; confirmar que a página IAC lista os slugs de `iac/*.json` de
  teste, renderiza a árvore e o filtro de busca funciona.
- Conferir que nenhuma página de conector linka para `iac-viewer.md`.
