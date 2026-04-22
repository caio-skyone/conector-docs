# Service Now

## Contexto  

O template de conector do Service Now permite interações com as APIs Table, Service Catalog e Attachment de forma facilitada e integrada ao Studio. É possível integrar qualquer outra API no Service Now no mesmo conector desde que esteja acessível no mesmo modelo de autenticação das APIs padrão.

A [Table API](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_TableAPI.html) é a interface principal e mais direta para realizar operações de CRUD (Create, Read, Update, Delete) nas tabelas do banco de dados do ServiceNow. Ela permite que aplicações externas consultem registros, criem novos incidentes ou tarefas, atualizem dados existentes ou excluam informações. É a API padrão para integrações gerais de dados e sincronização entre sistemas.

A [Service Catalog API](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_ServiceCatalogAPI.html) é estruturada especificamente para interagir com o Catálogo de Serviços da plataforma. Em vez de simplesmente inserir dados em uma tabela, essa API respeita as regras de negócio de solicitações. Ela permite que você acesse categorias, visualize itens disponíveis e submeta solicitações (_checkout_), acionando os fluxos de trabalho (_workflows_) de aprovação e execução configurados no ServiceNow.

A [Attachment API](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_AttachmentAPI.html) é dedicada ao gerenciamento de arquivos. Ela permite fazer o upload, download e a exclusão de anexos vinculados a registros específicos do ServiceNow. Se você precisa anexar um log de erro a um incidente recém-criado pela Table API ou enviar um formulário PDF em uma requisição do Service Catalog, é esta API que processará o arquivo.

---  
  
## Autenticação  
  
**Tipo:** OAuth2  
  
**Configuração da conta conectada:**  
  
| Variável                   | Valor                   |     |
| -------------------------- | ----------------------- | --- |
| Host                       | {{host}}                |     |
| Porta                      | 443                     |     |
| Client ID                  | {{client_id}}           |     |
| Client Secret              | {{client_secret}}       |     |
| Endpoint de Troca de Token | {{host}}/oauth_token.do |     |
-  Marque Content Type como URL Encoded
- Em **configurações do payload de token**, troque grant_type para **client credentials**

### Host
É a url da sua instância do service now, você pode acessá-la no painel de desenvolvedor, geralmente algo como:
```
https://{subdomínio}.service-now.com/
```
  
### Client ID e Client Secret
1. Na sua instância, clique em **All** e pesquise por OAuth, acesse **System OAuth** > **Application Registry** 
2. Clique em New e na opção **New Inbound Integration Experience** e **New Integration**, a opção recomendada de integração é **OAuth - Client credentials grant**
3. Preencha as informações, é recomendável criar um usuário OAuth específico para essa integração e Auth scopes restritos ao seu uso.

> Observe que o funcionamento das operações do conector dependem do auth scope permitir sua interação

4. O Client ID e o Client Secret estarão nessa tela, não se esqueça de salvar as alterações

---  
  
## Operações  

| Nome da operação | Método | Descrição |
| --- | --- | --- |
| servicecatalog-catalogs-Get Catalogs | GET | Recupera a lista de catálogos acessíveis ao usuário. |
| table-Retrieve a record | GET | Obtém dados de um registro específico da tabela. |
| table-Retrieve records from a table | GET | Recupera registros da tabela. |
| import-Insert Multiple Records from same request | POST | Encaminha vários registros de uma vez em uma única requisição. |
| attachment-Retrieve metadata for attachments | GET | Obtém metadados dos anexos. |
| servicecatalog-cart-Checkout Cart | POST | Finaliza a compra dos itens existentes no carrinho no catálogo de serviços. |
| servicecatalog-cart-Update Cart Item | PUT | Atualiza um item no carrinho de serviços do catálogo. |
| servicecatalog-service_fulfillment-step_configs-Get Fulfillment Step Configs | GET | Recupera as configurações de etapas de fulfillment de serviços. |
| servicecatalog-catalog_client_script-Get OnChange Choices | GET | Obtém opções de escolha que mudam em tempo real para scripts de catálogo de serviços. |
| table-Modify a record | PUT | Atualiza um registro já existente na tabela. |
| servicecatalog-categories-Get Category Details | GET | Recupera detalhes de uma categoria. |
| servicecatalog-item-Delete Catalog Item Record | DELETE | Excluir registro de item do catálogo pelo ID fornecido. |
| servicecatalog-items-add_to_wishlist-Add Item to Wishlist | POST | Adicionar o item especificado à lista de desejos do usuário. |
| servicecatalog-items-Get Catalog Item Details | GET | Retorna os detalhes de um item de catálogo especificado. |
| servicecatalog-items-Get Catalog Items | GET | Obtem a lista de itens do catálogo. |
| servicecatalog-service_fulfillment-step-Delete Fulfillment Step | DELETE | Apaga um passo de fulfillment no catálogo de serviço. |
| servicecatalog-cart-Remove Item from Cart | DELETE | Remove um produto do carrinho de compras. |
| servicecatalog-variables-display_value-Get Variable Display Value | POST | Recupera o valor de exibição de uma variável específica do catálogo de serviço. |
| servicecatalog-wizard-Get Wizard Details | GET | Obter detalhes do wizard pelo ID. |
| attachment-file-Upload an attachment | POST | Carrega anexo no Service Now |
| attachment-file-Retrieve attachment metadata | GET | Retorna metadados do arquivo anexado. |
| attachment-file-Delete an attachment | DELETE | Exclui o anexo especificado pelo endpoint attachment/file |
| attachment-file-Retrieve attachment content | GET | Obtém o conteúdo do arquivo anexo especificado. |
| attachment-Retrieve first attachment content by file name | GET | Obtém o conteúdo do primeiro anexo pelo nome do arquivo. |
| servicecatalog-cart-Submit Order | POST | Enviar pedido ao carrinho do catálogo de serviços. |
| servicecatalog-catalogs-categories-Get Catalog Categories | GET | Obtém a lista de categorias de um catálogo específico. |
| servicecatalog-catalogs-Get Catalog Details | GET | Recupera os detalhes do catálogo. |
| servicecatalog-items-add_to_cart-Add Item to Cart | POST | Adiciona item do catálogo ao carrinho para checkout. |
| servicecatalog-items-order_now-Order Item Now | POST | Envia pedido imediato de um item de catálogo com ID informado. |
| servicecatalog-items-price-Calculate Item Price | POST | Calcula o preço total de um item pelo seu ID no catálogo de serviços. |
| servicecatalog-items-save_producer-Save Record Producer Draft | POST | Salva um rascunho do produtor de registro para o item especificado. |
| servicecatalog-items-submit_guide-Submit Order Guide | PUT | Submete a guia de pedido de um item do catálogo de serviços. |
| servicecatalog-items-variables-Get Item Variables | GET | Recupera variáveis de um item do catálogo. |
| table-Create a record | POST | Cria um novo registro na tabela. |
| servicecatalog-items-versioning-checkout-Checkout Item Version | POST | Realiza o checkout de uma versão de item no catálogo de serviços. |
| servicecatalog-items-delegation-Get Item Delegation | GET | Recupera a delegação configurada do item identificado por item_sys_id para o usuário especificado. |
| servicecatalog-producer-record-Get Producer Record | GET | Recupera os dados de um registro associado a um produtor pelo ID. |
| servicecatalog-record_id-wizard-Get Record Wizard | GET | Obtém detalhes do wizard de um registro no catálogo de serviços. |
| servicecatalog-template-duplicate-Duplicate Template | POST | Cria uma cópia de um template existente no catálogo de serviços. |
| servicecatalog-wishlist-Get Wishlist | GET | Exibe a wishlist de produtos e serviços no catálogo de serviços. |
| table-Delete a record | DELETE | Exclui um registro da tabela. |
| servicecatalog-variables-display_value-Get Variables Display Values | POST | Obtém os valores exibidos das variáveis do catálogo de serviços. |
| servicecatalog-catalog_builder-Validate Catalog Categories | GET | Valida e confirma categorias cadastradas no catálogo. |
| import-Retrieve an Import Set record | GET | Recupera o registro de importação especificado no conjunto. |
| import-Create a record in an Import Set staging table | POST | Adicionar registro à tabela de staging do Import Set. |
| servicecatalog-cart-Get Delivery Address | GET | Recupera o endereço de entrega configurado para o carrinho de compras. |
| servicecatalog-items-save_catalog_item-Save Catalog Item Draft | POST | Salva um rascunho de item de catálogo. |
| servicecatalog-question_designer-update_resource-Update Question Designer Resource | POST | Atualiza recurso de Question Designer no Catálogo de Serviços usando {action} e {sys_id}. |
| servicecatalog-service_fulfillment-generateStagePoolIds-Generate Stage Pool IDs | GET | Cria IDs de pool Stage conforme quantidade solicitada no catálogo de serviços. |
| servicecatalog-service_fulfillment-step-Create Fulfillment Step | POST | Cria um passo de fulfillment no catálogo de serviços. |
| table-Update a record | PATCH | Atualiza dados de um registro na tabela. |
| servicecatalog-wishlist-Get Wishlist Item Details | GET | Retorna detalhes do item na lista de desejos pelo identificador do carrinho. |
| servicecatalog-variableSetLayout-Get Variable Set Layout | POST | Recupera o layout de conjunto de variáveis do catálogo de serviços. |
| servicecatalog-service_fulfillment-step-Update Fulfillment Step | PUT | Atualiza a etapa de fulfillment identificada por sys_id no catálogo de serviços. |
| servicecatalog-question_designer-delete_resource-Delete Question Designer Resource | POST | Excluir recurso específico do Question Designer no catálogo de serviços. |
| servicecatalog-question_designer-create_resource-Create Question Designer Resource | POST | Cria um recurso no Question Designer conforme a ação especificada no caminho. |
| servicecatalog-items-get_invalid_delegated_users-Get Invalid Delegated Users | POST | Lista usuários delegados inválidos de um item. |
| servicecatalog-items-submit_producer-Submit Record Producer | POST | Submete o Record Producer ao item de catálogo identificado por sys_id. |
| servicecatalog-items-checkout_guide-Checkout Order Guide | POST | Finalize os itens de um guia de pedido. |
| servicecatalog-items-versioning-cancel_review-Cancel Version Review | PUT | Cancelar a revisão de versão de um item no serviço de catálogo. |
| servicecatalog-cart-Empty Cart | DELETE | Limpa o carrinho de serviços do catálogo. |
| servicecatalog-cart-Get Cart Details | GET | Obtenha os detalhes completos do carrinho de serviços do usuário. |
| servicecatalog-wizard-record_id-Process Wizard Record | POST | Processa registro de wizard no catálogo de serviços, identificando por sys_id e record_id. |
| servicecatalog-variables-Update Record Variable | PUT | Atualiza variável de registro em item de catálogo de serviço. |
| servicecatalog-variables-validate_regex-Validate Variable Regex | POST | Valida a expressão regular de uma variável no catálogo de serviços. |
| servicecatalog-variables-dynamic_value-Get Variable Dynamic Value | POST | Obtém o valor dinâmico de uma variável de catálogo utilizando seu sys_id. |

---  
  
## Documentação oficial

[Todas as APIs Service Now](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/api-rest.html)

[Rest API Explorer](https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/use-REST-API-Explorer.html)

[Attachment](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_AttachmentAPI.html)

[Service Catalog](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_ServiceCatalogAPI.html)

[Table](https://www.servicenow.com/docs/r/washingtondc/api-reference/rest-apis/c_TableAPI.html)

