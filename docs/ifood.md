# iFood Merchant API

## Contexto

O **iFood Merchant API** é a API REST para integradores que operam **lojas parceiras** no ecossistema iFood (restaurantes e outros verticais no portal de desenvolvedores). Permite automatizar gestão de **lojas** (merchants), **status operacional**, **horários** e **interrupções**, consumo de **eventos** de pedidos (polling), manutenção do **catálogo** (categorias, itens, complementos, preços, estoque e imagens) e o **ciclo de vida de pedidos** (confirmação, preparo, pronto, entrega, cancelamento e validações).

Este conector cobre **43 operações** nos domínios: **Merchant**, **Events**, **Catalog** e **Order**.

**Convenções usadas pelo conector:**

- **Autenticação:** OAuth 2.0 (`oauth-2`) — as requisições usam `Authorization: Bearer <access_token>`. O token é obtido na API de autenticação do iFood com `client_id` e `client_secret` da aplicação registrada no [Developer Portal](https://developer.ifood.com.br/pt-BR/developer/applications). Como o Skyone Studio usa comunicação servidor para servidor nos conectores, é recomendado o método de **Aplicação centralizada**.

- **Host na conta conectada:** em geral `https://merchant-api.ifood.com.br` (caminhos das operações são relativos a essa base, ex.: `/merchant/v1.0/...`, `/order/v1.0/...`).

- **Eventos:** polling recomendado a cada **30 segundos**; após processar, confirmar com acknowledge.

- **Pedidos:** confirmação obrigatória em até **8 minutos** após o evento de novo pedido.

Conceitos comuns: **merchant** (loja), **interruption** (pausa no recebimento), **opening hours**, **catalog / category / item / option** (complementos), **sellable / unsellable**, **inventory**, **order** e **event** (notificações assíncronas de mudança de estado).

---

## Autenticação

**Tipo:** OAuth 2.0

**Configuração da conta conectada:**

| Variável | Valor |
| -------- | ----- |
| Host | `https://merchant-api.ifood.com.br` |
| Client ID | {{client_id}} |
| Client Secret | {{client_secret}} |
| Access Token | {{access_token}} |
| Refresh Token | {{refresh_token}} |
| Endpoint de troca de token | `https://merchant-api.ifood.com.br/authentication/v1.0/oauth/token` |

 Consulte [a documentação](https://developer.ifood.com.br/pt-BR/docs/guides/modules/authentication/intro) para informações sobre como obter as credenciais. Note que o método de aplicação centralizada não necessita de um Callback, caso deseje usar o método de aplicação distribuída, será necessário usar um [callback](callback/contexto.md).

---

## Operações

| Nome da Operação | Método | Descrição da Função |
| :--------------- | :----- | :------------------ |
| **Merchant - List stores** | **GET** | Lista todas as lojas vinculadas ao token de acesso. |
| **Merchant - Get store details** | **GET** | Retorna detalhes completos de uma loja específica. |
| **Merchant - Get store status** | **GET** | Retorna o status operacional de uma loja. |
| **Merchant - Get operation status** | **GET** | Retorna o status de uma operação específica da loja (DELIVERY, TAKEOUT, INDOOR). |
| **Merchant - List interruptions** | **GET** | Lista as interrupções (pausas) ativas e futuras de uma loja. |
| **Merchant - Create interruption** | **POST** | Cria uma pausa no recebimento de pedidos. |
| **Merchant - Delete interruption** | **DELETE** | Remove uma interrupção e reabre a loja. |
| **Merchant - List opening hours** | **GET** | Retorna os horários de funcionamento configurados da loja. |
| **Merchant - Update opening hours** | **PUT** | Atualiza os horários de funcionamento da loja (substituição completa). |
| **Merchant - Generate checkin QR code** | **POST** | Gera PDF com QR codes para check-in de entregadores (até 20 lojas). |
| **Events - Get polling events** | **GET** | Consulta novos eventos de pedidos via polling (recomendado a cada 30s). |
| **Events - Acknowledge events** | **POST** | Confirma o recebimento e processamento de eventos. |
| **Catalog - List catalogs** | **GET** | Lista todos os catálogos da loja e seus contextos. |
| **Catalog - List categories** | **GET** | Lista as categorias do catálogo. Use include_items=true para incluir itens. |
| **Catalog - Create category** | **POST** | Cria uma categoria para agrupar itens no catálogo. |
| **Catalog - Create or update item** | **PUT** | Cria ou atualiza um item completo com produtos, grupos e complementos. |
| **Catalog - List items by category** | **GET** | Lista os itens de uma categoria com seus complementos. |
| **Catalog - Get item details** | **GET** | Retorna um item com todos seus componentes (produto, grupos, opções). |
| **Catalog - List sellable items** | **GET** | Lista os itens ativos e disponíveis para venda em um catálogo. |
| **Catalog - List unsellable items** | **GET** | Lista os itens bloqueados e o motivo de cada bloqueio. |
| **Catalog - Update item price** | **PATCH** | Altera o preço de um item globalmente ou por contexto de catálogo. |
| **Catalog - Update item status** | **PATCH** | Pausa ou reativa um item globalmente ou por contexto de catálogo. |
| **Catalog - Update item external code** | **PATCH** | Atualiza o código externo (POS) de um item globalmente ou por contexto. |
| **Catalog - Update option price** | **PATCH** | Altera o preço de um complemento globalmente ou por contexto. |
| **Catalog - Update option status** | **PATCH** | Pausa ou reativa um complemento globalmente ou por contexto. |
| **Catalog - Update option external code** | **PATCH** | Atualiza o código externo (POS) de um complemento por contexto. |
| **Catalog - Batch update prices** | **PATCH** | Atualiza preços de itens e complementos em lote (assíncrono). |
| **Catalog - Batch update status** | **PATCH** | Atualiza status de itens e complementos em lote (assíncrono). |
| **Catalog - Get batch operation status** | **GET** | Consulta o progresso de uma operação em lote assíncrona. |
| **Catalog - Create inventory** | **POST** | Define a quantidade máxima vendível de um produto. |
| **Catalog - Get inventory** | **GET** | Retorna o inventário atual de um produto. |
| **Catalog - Delete inventory** | **POST** | Remove o limite de inventário de um ou mais produtos. |
| **Catalog - Upload image** | **POST** | Envia uma imagem em base64 para uso em itens do catálogo. |
| **Order - Get order details** | **GET** | Retorna informações completas de um pedido. |
| **Order - Confirm order** | **POST** | Confirma um pedido recebido (obrigatório em até 8 minutos). |
| **Order - Start preparation** | **POST** | Inicia a preparação do pedido após confirmação. |
| **Order - Notify order ready** | **POST** | Notifica que o pedido está pronto para retirada ou entrega. |
| **Order - Dispatch order** | **POST** | Notifica que o pedido saiu para entrega própria (deliveredBy MERCHANT). |
| **Order - Get cancellation reasons** | **GET** | Retorna os motivos de cancelamento válidos para um pedido. |
| **Order - Request cancellation** | **POST** | Solicita o cancelamento de um pedido com motivo válido. |
| **Order - Track driver** | **GET** | Retorna a localização em tempo real do entregador iFood. |
| **Order - Validate pickup code** | **POST** | Valida o código de coleta fornecido pelo entregador. |
| **Order - Verify delivery code** | **POST** | Valida e confirma a entrega ou retirada do pedido. |
| **Order - Get events polling** | **GET** | Consulta novos eventos de pedidos via polling. |
| **Order - Acknowledge events** | **POST** | Confirma o processamento de eventos de pedidos. |

---

## Documentação oficial

[iFood Developer — documentação e guias de integração](https://developer.ifood.com.br/pt-BR/docs/getting-started)
