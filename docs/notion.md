# Notion API

## Contexto
O conector Notion permite o gerenciamento e a automação de espaços de trabalho na plataforma, abrangendo a criação e a manipulação de páginas, bancos de dados, blocos, usuários, comentários e outras funcionalidades essenciais. Há duas abordagens suportadas para a conexão, com as mesmas operações disponíveis:

* **Notion Internal:** Focado em workspaces internos e integrações privadas, utilizando a autenticação simplificada por Bearer Token.
* **Notion Public:** Voltado para workspaces públicos e aplicativos de terceiros, realizando a autenticação completa e baseada em permissões via OAuth 2.0.

## Autenticação

As configurações requeridas variam conforme a natureza da conexão escolhida. 

### Notion Internal
**Tipo:** Bearer Token

| Variável | Valor |
| -------- | ----- |
| host | https://api.notion.com |
| porta | 443 |
| token | {{token}} |

Consulte a [Documentação do Notion](https://developers.notion.com/guides/get-started/personal-access-tokens) para obter o Personal Access Token (PAT).


### Notion Public
**Tipo:** OAuth 2.0

| Variável | Valor |
| -------- | ----- |
| Host | https://api.notion.com |
| Porta | 443
| Client ID | {{client_id}} |
| Client Secret | {{client_secret}} |
| Access Token | {{access_token}} |
| Refresh Token | {{refresh_token}} |
| Endpoint de troca de token | https://api.notion.com/v1/oauth/token |
| Chave da resposta com o refresh_token | refresh_token |

#### Procedimento do OAuth2 do Notion Public

Siga a [documentação sobre OAuth2 com callback](inserir-link-depois) para conseguir o primeiro access_token e o refresh_token da API do Notion, com os requisitos adicionais:

A API do Notion exige autenticação Basic nos endpoints do OAuth, onde o usuário é o seu client_id e a senha o seu client_secret, o **Postman** permite usar o Basic facilmente
substituindo a autenticação nesses endpoints em específico. No Studio, a operação **OAuth - Create a token** deverá receber a string do Basic em Base64, os seguintes comandos
podem ser usados para obtê-la:

```bash

# unix
printf '%s' "SEU-CLIENT-ID:SEU-CLIENT-SECRET" | base64

# powershell
$bytes = [System.Text.Encoding]::UTF8.GetBytes("SEU-CLIENT-ID:SEU-CLIENT-SECRET")
$base64 = [System.Convert]::ToBase64String($bytes)
$base64

```

Para usar exclusivamente o Studio no fluxo do OAuth2, também será necessário remover temporariamente da conta conectada a entrada em "Parâmetros no cabeçalho da requisição após autenticação" para evitar conflitos, o par chave-valor é:

```text
Authorization | Bearer <>token</>
```

Após completar o fluxo como descrito na documentação sobre OAuth2 com Callback e obter os tokens, complete a sua conta conectada e insira novamente o Parâmetro no cabeçalho da requisição após autenticação, exatamente como estava.

## Operações

Ambos os conectores (Internal e Public) compartilham a mesma biblioteca de ações. A lista de operações suportadas inclui:

| Nome da Operação | Método | Descrição da Função |
| ---------------- | ------ | ------------------- |
| Views - Create a view | POST | Cria uma nova view em um banco de dados ou widget em dashboard. |
| Search - Search by title | POST | Busca páginas e data sources compartilhados com a conexão pelo título. |
| File Uploads - Create a file upload | POST | Inicia o processo de upload de arquivo no workspace do Notion. |
| File Uploads - List file uploads | GET | Lista os uploads de arquivo da conexão bot atual. |
| File Uploads - Retrieve a file upload | GET | Retorna detalhes de um file upload pelo ID. |
| File Uploads - Send a file upload | POST | Transmite o conteúdo do arquivo para um file upload criado. |
| File Uploads - Complete a file upload | POST | Finaliza um upload multi-part após todos os chunks serem enviados. |
| Data Sources - Create a data source | POST | Cria um data source no Notion. |
| Data Sources - Retrieve a data source | GET | Retorna um data source pelo ID. |
| Data Sources - Update a data source | PATCH | Atualiza atributos de um data source. |
| Data Sources - Query a data source | POST | Consulta entradas de um data source com filtros e ordenação. |
| Data Sources - List data source templates | GET | Lista os templates de página disponíveis para um data source. |
| Comments - Delete a comment | DELETE | Remove um comentário pelo ID. |
| Views - Retrieve a view | GET | Retorna uma view pelo ID. |
| Views - Update a view | PATCH | Atualiza nome, filtro, ordenação ou configuração de uma view. |
| Views - Delete a view | DELETE | Remove uma view de um banco de dados. |
| Views - List views | GET | Lista todas as views de um banco de dados. |
| Views - Create a view query | POST | Executa a query de uma view e retorna a primeira página de resultados. |
| Views - Get view query results | GET | Pagina pelos resultados em cache de uma view query. |
| Views - Delete a view query | DELETE | Remove uma view query em cache. |
| OAuth - Create a token | POST | Cria um access token OAuth para autenticação de terceiros com o Notion. |
| OAuth - Introspect a token | POST | Retorna status, escopo e hora de emissão de um token. |
| OAuth - Revoke a token | POST | Revoga um access token. |
| Pages - Trash a page | PATCH | Move uma página para a lixeira. |
| Blocks - Update a block | PATCH | Atualiza o conteúdo de um bloco pelo ID. |
| Blocks - Delete a block | DELETE | Remove um bloco pelo ID. |
| Blocks - Retrieve block children | GET | Retorna filhos paginados de um bloco. |
| Blocks - Append block children | PATCH | Adiciona novos blocos filhos a um bloco pai. |
| Pages - Create a page | POST | Cria uma nova página filha de uma página ou data source existente. |
| Pages - Retrieve a page | GET | Retorna os valores de propriedades de uma página pelo ID. |
| Pages - Update a page | PATCH | Modifica propriedades, ícone ou capa de uma página. |
| Pages - Retrieve a page property item | GET | Retorna o valor de uma propriedade de uma página. |
| Pages - Retrieve page as markdown | GET | Retorna o conteúdo de uma página renderizado em markdown. |
| Pages - Update page markdown | PATCH | Insere ou substitui conteúdo de uma página usando markdown. |
| Pages - Move a page | POST | Move uma página existente para um novo pai. |
| Blocks - Retrieve a block | GET | Retorna um objeto Block pelo ID. |
| Databases - Create a database | POST | Cria um banco de dados (e data source inicial) no Notion. |
| Databases - Retrieve a database | GET | Retorna um banco de dados pelo ID. |
| Databases - Update a database | PATCH | Atualiza título, descrição, ícone, capa ou propriedades de um banco de dados. |
| Databases - Query a database | POST | Consulta entradas de um banco de dados com filtros e ordenação. |
| Users - List all users | GET | Retorna lista paginada de usuários do workspace. |
| Users - Retrieve a user | GET | Retorna um usuário pelo ID. |
| Users - Retrieve bot user | GET | Retorna o usuário bot associado ao token de API. |
| Comments - List comments | GET | Retorna comentários não resolvidos de uma página ou bloco. |
| Comments - Create a comment | POST | Cria um comentário em uma página, bloco ou thread de discussão. |
| Comments - Retrieve a comment | GET | Retorna um comentário pelo ID. |
| Comments - Update a comment | PATCH | Atualiza o texto de um comentário. |

## Documentação oficial
* [https://developers.notion.com/](https://developers.notion.com/)