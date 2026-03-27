## Obtendo Tokens OAuth 2.0 no Postman

O OAuth 2.0 é um protocolo de autorização padrão da indústria que permite que aplicativos obtenham acesso limitado a contas de usuários em um serviço HTTP.

O Postman possui uma ferramenta nativa robusta que facilita imensamente a geração e o gerenciamento desses tokens sem a necessidade de escrever código.

### Pré-requisitos

Antes de iniciar no Postman, você precisará ter em mãos as seguintes credenciais fornecidas pela API ou provedor de identidade que você está tentando acessar:
* **Client ID:** O identificador público do seu aplicativo.
* **Client Secret:** A chave secreta do seu aplicativo (nunca deve ser compartilhada publicamente).
* **Authorization URL:** A URL de login onde o usuário aprovará o acesso.
* **Access Token URL:** A URL da API usada para trocar o código de autorização pelo token final.
* **Scopes (Escopos):** Opcional, dependendo da API. Define o nível de permissão que você está solicitando (ex: `read:users`, `write:data`).

---

### Passo a Passo para Configuração

#### Passo 1: Acesse a aba de Autorização
1. Abra o Postman e crie uma nova requisição (clicando no botão **+** ou em **New** > **HTTP Request**).
2. Logo abaixo da barra de URL da requisição, clique na aba **Authorization**.
3. No menu suspenso **Auth Type**, role a lista e selecione **OAuth 2.0**.
4. Na seção "Add authorization data to", mantenha a opção padrão **Request Headers**.



#### Passo 2: Configure os detalhes do Novo Token
Role a tela para baixo até encontrar a seção chamada **Configure New Token**. É aqui que você preencherá as informações da sua API.



Preencha os campos com base no padrão OAuth 2.0:

* **Token Name:** Dê um nome amigável ao seu token (ex: `MeuTokenAPI`). Isso ajuda a identificá-lo depois se você tiver vários.
* **Grant Type:** O tipo de fluxo de concessão. Os dois mais comuns são:
    * *Authorization Code:* Usado quando a API exige que um usuário faça login em uma página web para aprovar o acesso. (É o padrão mais comum e seguro).
    * *Client Credentials:* Usado para comunicação de servidor para servidor (machine-to-machine), sem a interação de um usuário.
* **Callback URL:** A URL para onde a API redirecionará após o login. Muitas APIs permitem o uso de uma URL padrão do Postman. Você pode deixar em branco e marcar a caixa **Authorize using browser** para que o Postman cuide do redirecionamento de forma automática.
* **Auth URL:** A URL de autorização fornecida pela documentação da API.
* **Access Token URL:** A URL de obtenção do token fornecida pela documentação da API.
* **Client ID:** Cole o Client ID do seu aplicativo.
* **Client Secret:** Cole o Client Secret do seu aplicativo.
* **Scope:** Insira os escopos necessários separados por espaço (ou conforme exigido pela documentação da API específica).
* **State:** Uma string aleatória usada para segurança (prevenção de ataques CSRF). Você pode inserir um valor qualquer, como `123456`, ou deixar em branco se a API não exigir.
* **Client Authentication:** Deixe como **Send as Basic Auth header** (padrão recomendado pela maioria das APIs).

#### Passo 3: Solicite o Token
Com todos os dados preenchidos, role até o final da seção e clique no botão laranja **Get New Access Token**.

O Postman abrirá uma janela do seu navegador de internet padrão. Você verá a tela de login do serviço (ex: tela de login do Google ou da sua empresa). Faça o login e clique em "Autorizar/Permitir". O navegador avisará que você pode fechar a janela e retornar ao Postman.

#### Passo 4: Use o Token na Requisição
Após a autenticação bem-sucedida, o Postman exibirá uma janela de sobreposição mostrando os detalhes do token gerado (como o próprio `Access Token`, quando ele expira e o tipo de token).

1. Clique no botão **Use Token** no canto superior direito dessa janela.
2. O Postman automaticamente injetará esse token na sua requisição atual. O campo "Current Token" na aba de Authorization agora mostrará o token gerado.

Quando você clicar em **Send** para fazer a sua requisição à API, o Postman adicionará automaticamente um cabeçalho HTTP no formato `Authorization: Bearer <seu_token>` e sua requisição será autenticada.
