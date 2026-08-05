# iac/

JSONs de IAC exportados por conector (source of truth), um arquivo por
conector: `{slug}.json`.

**Atenção:** todo arquivo `.json` colocado aqui é publicado, verbatim, no
site público (via `hooks/iac_assets.py` → `site/iac-data/{slug}.json`,
exposto na página `docs/iac-viewer.md`). Antes de commitar um JSON de IAC
real, confirme que ele não carrega credenciais reais, apenas os
placeholders de template (`<>descricao_do_valor</>`) — nunca segredos em
texto plano.
