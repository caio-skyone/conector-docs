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
