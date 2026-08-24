# Zoop

## Contexto

A Zoop é uma plataforma brasileira de pagamentos como serviço (PaaS) voltada para marketplaces e subadquirentes. Ela permite que empresas criem e gerenciem seus próprios ecossistemas de pagamentos, com suporte a múltiplos meios de pagamento e participantes (vendedores, compradores, parceiros).

Principais domínios e conceitos:

- **Marketplace**: entidade central da plataforma. Todos os recursos são organizados sob um `marketplace_id`.
- **Sellers (Vendedores)**: participantes que recebem pagamentos. Podem ser pessoas físicas (individuals) ou jurídicas (businesses). Precisam ser credenciados e documentados antes de receber créditos.
- **Buyers (Compradores)**: clientes finais que realizam pagamentos. Podem ter cartões e contas bancárias associados.
- **Transactions**: operações de cobrança. Suportam cartão não presente (V1 e V2), boleto e terminais POS. Permitem captura e estorno.
- **Split Rules**: divisão automática do valor de uma transação entre múltiplos sellers.
- **Boletos**: geração e envio de cobranças por boleto bancário.
- **Recebíveis (Receivables)**: parcelas futuras a receber, resultantes de transações parceladas. Suportam antecipação (Prepayments).
- **Transfers**: transferências de saldo entre contas, incluindo P2P e para contas bancárias externas.
- **Invoices**: faturas avulsas ou vinculadas a assinaturas recorrentes.
- **Recurring Plans & Subscriptions**: planos de cobrança recorrente vinculados a clientes via assinaturas.
- **Sales Plans**: planos de taxas e políticas de crédito de recebíveis para sellers (diferente dos planos de cobrança recorrente).
- **Prepaid Cards**: cartões pré-pagos associados a estabelecimentos dentro do ecossistema do marketplace.
- **Bank Accounts & Cards/Tokens**: dados bancários e cartões tokenizados de sellers e buyers.
- **Events & Webhooks**: notificações de eventos da plataforma com suporte a redisparo.
- **API Keys & Users**: gerenciamento de credenciais e permissões de acesso à API.

---

## Autenticação

**Tipo:** Autenticação básica (HTTP Basic)

**Configuração da conta conectada:**

| Variável | Valor |
| -------- | ----- |
| Host | `https://api.zoop.ws` |
| Porta | 443 |
| username | {{marketplace_id}} |
| password | {{publishable_key}} |

> **Nota:** o `username` é o identificador do marketplace (ex.: `820a6bda73c546a8b2f12a5ebcae7732`) e o `password` é a chave publicável (ZPK) do marketplace (ex.: `zpk_test_...`). Ambos são obtidos no painel da Zoop.

---

## Operações

| Nome da Operação | Método | Descrição da Função |
| :--------------- | :----- | :------------------ |
| **Sellers - Criar vendedor individual** | POST | Cria um novo vendedor do tipo pessoa física no marketplace informado. |
| **Sellers - Alterar vendedor individual** | PUT | Atualiza os dados de um vendedor do tipo pessoa física pelo seu identificador. |
| **Sellers - Criar vendedor empresa** | POST | Cria um novo vendedor do tipo pessoa jurídica no marketplace informado. |
| **Sellers - Alterar vendedor empresa** | PUT | Atualiza os dados de um vendedor do tipo pessoa jurídica pelo seu identificador. |
| **Sellers - Enviar documento de cadastro** | POST | Faz upload de um documento de cadastro para o vendedor informado (multipart/form-data). |
| **Sellers - Listar documentos de vendedor** | GET | Lista todos os documentos de cadastro de um vendedor específico. |
| **Sellers - Download de documento** | GET | Realiza o download do arquivo de um documento de vendedor pelo identificador do documento. |
| **Sellers - Recuperar detalhes de vendedor** | GET | Recupera os detalhes de um vendedor específico pelo seu identificador. |
| **Sellers - Remover vendedor** | DELETE | Remove um vendedor do marketplace pelo seu identificador. |
| **Sellers - Listar vendedores** | GET | Lista todos os vendedores cadastrados no marketplace. |
| **Sellers - Buscar vendedor por CPF/CNPJ** | GET | Busca um vendedor no marketplace pelo CPF (pessoa física) ou CNPJ (pessoa jurídica). |
| **Sellers - Listar MCCs** | GET | Lista os Merchant Category Codes (MCCs) disponíveis na plataforma. |
| **Buyers - Criar comprador** | POST | Cria um novo comprador no marketplace informado. |
| **Buyers - Listar compradores** | GET | Lista todos os compradores cadastrados no marketplace. |
| **Buyers - Alterar comprador** | PUT | Atualiza os dados de um comprador específico pelo seu identificador. |
| **Buyers - Recuperar detalhes de comprador** | GET | Recupera os detalhes de um comprador específico pelo seu identificador. |
| **Buyers - Remover comprador** | DELETE | Remove um comprador do marketplace pelo seu identificador. |
| **Buyers - Buscar comprador por CPF/CNPJ** | GET | Busca um comprador no marketplace pelo CPF ou CNPJ informado. |
| **Bank Accounts - Criar token de conta bancária** | POST | Cria um token para uma conta bancária, permitindo associá-la a um comprador ou vendedor. |
| **Bank Accounts - Listar contas bancárias** | GET | Lista todas as contas bancárias associadas ao marketplace. |
| **Bank Accounts - Associar conta bancária** | POST | Associa uma conta bancária a um customer (seller ou buyer) no marketplace. |
| **Bank Accounts - Listar contas por seller** | GET | Lista todas as contas bancárias associadas a um seller específico. |
| **Bank Accounts - Recuperar detalhes de conta bancária** | GET | Recupera os detalhes de uma conta bancária específica pelo seu identificador. |
| **Bank Accounts - Remover conta bancária** | DELETE | Remove uma conta bancária específica do marketplace pelo seu identificador. |
| **Cards & Tokens - Criar token de cartão** | POST | Cria um token para um cartão de crédito/débito, permitindo associá-lo a um comprador. |
| **Cards & Tokens - Recuperar detalhes de token** | GET | Recupera os detalhes de um token de cartão ou conta bancária pelo seu identificador. |
| **Cards & Tokens - Associar cartão com comprador** | POST | Associa um token de cartão a um comprador no marketplace. |
| **Cards & Tokens - Recuperar detalhes de cartão** | GET | Recupera os detalhes de um cartão associado a um comprador pelo seu identificador. |
| **Cards & Tokens - Remover cartão** | DELETE | Remove um cartão associado a um comprador pelo seu identificador. |
| **Boletos - Recuperar detalhes de boleto** | GET | Recupera os detalhes de um boleto específico pelo seu identificador. |
| **V1 - Enviar cobrança de boleto por email** | POST | Envia a cobrança de um boleto para o endereço de e-mail informado. |
| **Payment Sources - Criar source para utilização transação** | POST | Cria um objeto source que permite aceitar uma variedade de formas de pagamento em transações. |
| **Payment Sources - Recuperar detalhes de source pelo identificador** | GET | Recupera os detalhes de uma source de pagamento específica pelo seu identificador. |
| **Payment Sources - Remover source pelo identificador** | DELETE | Remove uma source de pagamento específica pelo seu identificador. |
| **Transactions - Listar transaçoes do marketplace** | GET | Lista todas as transações realizadas no marketplace, com suporte a filtros por tipo de pagamento e referência. |
| **Transactions - Criar transação de cartão** | POST | Cria uma nova transação de cartão no marketplace informado. |
| **Transactions - Recuperar detalhes de transação pelo identificador** | GET | Recupera os detalhes de uma transação específica pelo seu identificador. |
| **Transactions - Alterar detalhes de transação pelo identificador** | PUT | Atualiza os dados de uma transação específica pelo seu identificador. |
| **V1 - Capturar transação cartão não presente** | POST | Captura uma transação de cartão não presente previamente autorizada. |
| **V1 - Estornar transação cartão não presente** | POST | Realiza o estorno de uma transação de cartão não presente previamente capturada. |
| **V1 - Parear terminal POS** | POST | Realiza o pareamento de um terminal POS ao marketplace informado. |
| **Transactions V2 - Listar transaçoes do marketplace** | GET | Lista todas as transações realizadas no marketplace. |
| **Transactions V2 - Criar transação Cartão Não Presente** | POST | Cria uma nova transação do tipo Cartão Não Presente no marketplace. |
| **V2 - Capturar transação cartão não presente** | POST | Captura uma transação de Cartão Não Presente previamente autorizada, efetivando a cobrança. |
| **V2 - Estornar transação cartão não presente** | POST | Estorna uma transação de Cartão Não Presente, cancelando a cobrança e revertendo o valor ao portador do cartão. |
| **Split Rules - Recuperar detalhes de regra de divisão por transação** | GET | Recupera os detalhes das regras de divisão associadas a uma transação específica. |
| **Split Rules - Criar regra de divisão por transação** | POST | Cria uma nova regra de divisão de valores para uma transação específica. |
| **Split Rules - Recupera detalhes de regra de divisão por transação** | GET | Recupera os detalhes de uma regra de divisão específica associada a uma transação. |
| **Split Rules - Alterar regra de divisão por transação** | PUT | Atualiza os dados de uma regra de divisão específica associada a uma transação. |
| **Split Rules - Remover regra de divisão por transação** | DELETE | Remove uma regra de divisão específica associada a uma transação. |
| **Receipts - Recuperar detalhes do recibo** | GET | Recupera os detalhes de um recibo específico pelo seu identificador. |
| **Receipts - Alterar detalhes do recibo** | PUT | Atualiza os dados de um recibo específico pelo seu identificador. |
| **V1 - Enviar recibo por email** | POST | Envia um recibo para o endereço de e-mail informado. |
| **V1 - Enviar recibo por sms.email** | POST | Envia um recibo via SMS e/ou e-mail para o destinatário informado. |
| **V1 - Enviar recibo por SMS** | POST | Envia um recibo por SMS para o número de telefone informado. |
| **Receivables - Recuperar detalhes de recebível** | GET | Recupera os detalhes de um recebível específico pelo seu identificador. |
| **Receivables - Listar recebíveis por seller** | GET | Lista todas as parcelas de recebimento associadas a um seller específico. |
| **Receivables - Listar transaçoes por vendedor** | GET | Lista todas as transações associadas a um vendedor específico no marketplace. |
| **V1 - Listar recebíveis por transação** | GET | Lista todas as parcelas de recebimento associadas a uma transação específica. |
| **Balances - Lista contas por buyer** | GET | Lista todas as contas de saldo associadas a um comprador no marketplace. |
| **Balances - Recuperar saldo de conta por seller** | GET | Recupera o saldo corrente e o saldo total da conta do seller. |
| **V1 - Listar histórico de lançamentos pelo identificador da conta** | GET | Lista o histórico de lançamentos financeiros de uma conta a partir do seu identificador único. |
| **V1 - Listar histórico de lançamentos de conta por buyer** | GET | Lista o histórico de lançamentos da conta principal de um comprador no marketplace. |
| **V1 - Listar histórico de lançamentos de conta por seller** | GET | Lista o histórico de lançamentos da conta principal do seller. |
| **Prepayments - Listagem de antecipações do Marketplace** | GET | Lista todas as antecipações sob demanda solicitadas pelo Marketplace. |
| **Prepayments - Criação de novo pedido de antecipação** | POST | Cria um novo pedido de antecipação, que será posteriormente simulado e terá aprovação financeira para realizar a antecipação de fato. |
| **Prepayments - Detalhe de antecipação** | GET | Busca os detalhes de uma antecipação solicitada. |
| **V1 - Atualização de status da antecipação** | POST | Atualiza uma antecipação simulada para pronta. |
| **Prepayments - Listagem de antecipações do Seller** | GET | Lista as antecipações sob demanda solicitadas pelo Marketplace para o Seller. |
| **V1 - Recupera informações da agenda futura do Seller** | GET | Recupera informações da agenda futura do Seller. |
| **Prepayments V2 - Listagem paginada de antecipações do Seller** | GET | Lista as antecipações sob demanda solicitadas pelo Marketplace para o Seller, com suporte a parâmetros de paginação. |
| **Adjustments - Listar ajustes de cobrança por marketplace** | GET | Lista os ajustes de cobrança associados ao marketplace. |
| **Adjustments - Recuperar detalhes de ajuste de cobrança** | GET | Recupera os detalhes de um ajuste de cobrança específico. |
| **Adjustments - Cancelar ajuste de cobrança agendado anteriormente à data prevista para efetivação** | DELETE | Cancela um ajuste de cobrança agendado antes da data prevista para efetivação. |
| **Adjustments - Criar ajuste de cobrança informando somente pagador** | POST | Cria um ajuste de cobrança do valor informado, debitando da conta do pagador e creditando na conta Master do Marketplace. |
| **V1 - Criar ajuste de cobrança informando pagador e recebedor** | POST | Cria um ajuste de cobrança do valor informado, debitando da conta do pagador e creditando na conta do recebedor. |
| **Transfers - Criar transferência para conta bancária** | POST | Cria uma transferência para uma conta bancária cadastrada. |
| **Transfers - Listar transferências por seller** | GET | Lista as transferências associadas ao seller. |
| **Transfers - Listar transferências por marketplace** | GET | Lista as transferências associadas ao marketplace. |
| **Transfers - Recuperar detalhes de transferência** | GET | Recupera os detalhes de uma transferência específica. |
| **Transfers - Cancelar transferência agendada anteriormente à data prevista para efetivação** | DELETE | Cancela uma transferência agendada antes da data prevista para efetivação. |
| **Transfers - Listar lançamentos futuros por seller** | GET | Lista os lançamentos futuros associados ao seller. |
| **V2 - Criar transferência P2P** | POST | Cria uma transferência P2P entre contas. |
| **Receiving Policy - Recuperar política de recebimento por seller** | GET | Recupera a política de recebimento configurada para o seller. |
| **Receiving Policy - Alterar política de recebimento por seller** | POST | Altera a política de recebimento configurada para o seller. |
| **Invoices - Recuperar todas as faturas de um marketplace** | GET | Recupera todas as faturas associadas a um marketplace específico. |
| **Invoices - Criar uma fatura avulsa** | POST | Cria uma fatura avulsa vinculada diretamente ao cliente, sem necessidade de assinatura. |
| **Invoices - Recuperar os detalhes de uma fatura pelo identificador** | GET | Recupera os detalhes completos de uma fatura específica a partir do seu identificador único. |
| **Invoices - Alterar detalhes de uma fatura pelo identificador** | PUT | Altera os detalhes de uma fatura existente a partir do seu identificador único. |
| **Invoices - Remover uma fatura pelo identificador** | DELETE | Remove uma fatura existente a partir do seu identificador único. |
| **Invoices - Recuperar faturas associadas a um vendedor pelo identificador** | GET | Recupera os detalhes de todas as faturas associadas a um vendedor específico. |
| **V2 - Aprovar fatura pendente** | POST | Aprova manualmente uma fatura que está com status pendente, sem acionar a cobrança ao cobrador. |
| **V2 - Estornar e reembolsar fatura** | POST | Estorna uma fatura paga, processando o reembolso conforme a forma de cobrança associada ao pagamento original. |
| **Recurring Plans - Listar planos por marketplace** | GET | Lista todos os planos de recorrência cadastrados para o marketplace informado. |
| **Recurring Plans - Criar um plano** | POST | Cria um novo plano de recorrência no marketplace para ser vinculado a assinaturas de clientes. |
| **Recurring Plans - Recupera um plano pelo identificador** | GET | Recupera os detalhes de um plano de recorrência específico a partir do seu identificador único. |
| **Recurring Plans - Alterar plano pelo identificador** | PUT | Altera os detalhes de um plano de recorrência existente a partir do seu identificador único. |
| **Recurring Plans - Deletar um plano pelo identificador** | DELETE | Remove permanentemente um plano de recorrência a partir do seu identificador único. |
| **Subscriptions - Recuperar todas as assinatura de um marketplace** | GET | Recupera a lista de todas as assinaturas cadastradas em um marketplace. |
| **Subscriptions - Criar uma assinatura entre um comprador e um plano** | POST | Cria uma nova assinatura vinculando um comprador a um plano de recorrência no marketplace. |
| **Subscriptions - Recuperar os detalhes de uma assinatura pelo identificador** | GET | Recupera os detalhes de uma assinatura específica a partir do seu identificador único. |
| **Subscriptions - Alterar os detalhes de uma assinatura pelo identificador** | PUT | Altera os detalhes de uma assinatura existente a partir do seu identificador único. |
| **Subscriptions - Remover uma assinatura pelo identificador** | DELETE | Remove uma assinatura, que representa o contrato de recorrência entre um plano e um cliente. |
| **V2 - Reativa uma assinatura pelo identificador** | POST | Reativa uma assinatura suspensa pelo seu identificador, fazendo com que ela volte a gerar faturas normalmente. |
| **V2 - Suspender uma assinatura pelo identificador** | POST | Suspende uma assinatura ativa pelo seu identificador, interrompendo a geração de novas faturas. |
| **Sales Plans - Criar plano de vendas** | POST | Cria um plano de vendas com taxas e políticas para crédito de recebíveis. |
| **Sales Plans - Listar planos de vendas** | GET | Lista todos os planos de vendas cadastrados no marketplace. |
| **Sales Plans - Recuperar detalhes de plano de vendas** | GET | Recupera os detalhes de um plano de vendas específico pelo seu identificador. |
| **Sales Plans - Remover plano de vendas** | DELETE | Remove um plano de vendas do marketplace pelo seu identificador. |
| **Sales Plans - Associar assinatura de plano de vendas** | POST | Associa um comprador a um plano de vendas criando uma assinatura. |
| **Sales Plans - Listar assinaturas de plano de vendas** | GET | Lista todas as assinaturas de planos de vendas no marketplace. |
| **Sales Plans - Recuperar detalhes de assinatura de plano de vendas** | GET | Recupera os detalhes de uma assinatura de plano de vendas pelo seu identificador. |
| **Sales Plans - Remover assinatura de plano de vendas** | DELETE | Desassocia uma assinatura de plano de vendas pelo seu identificador. |
| **Sales Plans - Listar assinaturas por seller** | GET | Recupera as assinaturas de plano de vendas associadas a um seller específico. |
| **Sales Plans - Listar assinaturas por comprador** | GET | Recupera as assinaturas de plano de vendas associadas a um comprador específico. |
| **Prepaid Cards - Lista de cartões pré-pagos associados pelo marketplace** | GET | Lista todos os cartões pré-pagos associados ao marketplace, incluindo os vinculados a qualquer estabelecimento da rede. |
| **Prepaid Cards - Adicionando cartão pré-pago a um estabelecimento.** | POST | Permite ao marketplace adicionar cartões pré-pagos de sua rede aos respectivos estabelecimentos. |
| **Prepaid Cards - Excluir um cartão associado** | DELETE | Exclui um cartão pré-pago associado a um estabelecimento, bloqueando e desassociando o cartão para sua devida exclusão. |
| **Prepaid Cards - Procura um cartão pelo ID** | GET | Retorna os detalhes de um cartão pré-pago associado a um estabelecimento, buscando pelo ID informado. |
| **Prepaid Cards - Lista de cartões pré-pagos de um estabelecimento** | GET | Lista todos os cartões pré-pagos associados a um estabelecimento específico. |
| **Marketplaces - Habilita um cartão pré-pago** | PUT | Habilita um cartão pré-pago; durante a ativação, uma URL é retornada para redirecionamento à operadora. |
| **Marketplaces - Bloqueia um cartão pré-pago** | PUT | Bloqueia permanentemente um cartão pré-pago associado a um estabelecimento. |
| **Marketplaces - Bloqueia um cartão pré-pago temporariamente** | PUT | Bloqueia temporariamente um cartão pré-pago associado a um estabelecimento. |
| **Marketplaces - Desbloqueia um cartão pré-pago** | PUT | Desbloqueia um cartão pré-pago previamente bloqueado de forma temporária. |
| **Marketplace - Criar novo marketplace** | POST | Cria um novo marketplace na plataforma. |
| **Marketplace - Recuperar detalhes do marketplace** | GET | Recupera os detalhes do marketplace informado. |
| **API Keys - Listar chaves de API por marketplace** | GET | Lista todas as chaves de API associadas ao marketplace informado. |
| **API Keys - Criar nova API Key por marketplace** | POST | Cria uma nova chave de API vinculada ao marketplace informado. |
| **API Keys - Recuperar detalhes de um API Key** | GET | Recupera os detalhes de uma chave de API específica pelo seu identificador. |
| **API Keys - Remover API Key** | DELETE | Remove uma chave de API específica do marketplace pelo seu identificador. |
| **Events - Listar eventos por marketplace** | GET | Lista todos os eventos associados ao marketplace informado. |
| **Events - Recuperar detalhes de evento pelo identificador** | GET | Recupera os detalhes de um evento específico pelo seu identificador. |
| **V1 - Redisparo de eventos** | POST | Solicita o reenvio de eventos; notifica no máximo os 100 primeiros eventos encontrados no filtro. |
| **Webhooks - Listar webhooks por marketplace** | GET | Lista todos os webhooks associados ao marketplace informado. |
| **Webhooks - Criar webhook por marketplace** | POST | Cria um novo webhook vinculado ao marketplace informado. |
| **Webhooks - Recuperar detalhes de webhook** | GET | Recupera os detalhes de um webhook específico pelo seu identificador. |
| **Webhooks - Remover webhook** | DELETE | Remove um webhook específico do marketplace pelo seu identificador. |
| **Users - Criar novo usuário de API** | POST | Cria um novo usuário de API na plataforma. |
| **Users - Recuperar detalhes de usuário** | GET | Recupera os detalhes de um usuário específico pelo seu identificador. |
| **Users - Alterar detalhes de usuário** | PUT | Atualiza os detalhes de um usuário específico pelo seu identificador. |
| **Users - Remover usuário** | DELETE | Remove um usuário específico da plataforma pelo seu identificador. |
| **V1 - Relizar login por usuário/senha** | POST | Realiza a autenticação de um usuário na plataforma usando credenciais de usuário e senha. |
| **Users - Criar novo usuário de API por marketplace** | POST | Cria um novo usuário de API vinculado ao marketplace informado. |
| **Users - Permissão do usuário** | GET | Busca todas as permissões que o usuário possui pelo user_id. |
| **Users - Criar permissão para usuário** | POST | Cria uma nova permissão para o usuário, podendo vinculá-la a um marketplace, seller ou grupo. |
| **Users - Permissão do usuário por permission_id** | GET | Recupera as permissões que o usuário possui pelo permission_id. |
| **Users - deleta uma permissão** | DELETE | Remove uma permissão do usuário pelo permission_id. |
| **Dashboard - Conceder acesso ao Minha Conta** | POST | Concede acesso ao portal Minha Conta da Zoop para um seller, enviando um convite de acesso. |

---

## Documentação oficial

https://docs.zoop.co/reference/introducao
