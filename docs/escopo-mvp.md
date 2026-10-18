# Escopo do MVP — Micro-API de Tarefas

## Objetivo

Disponibilizar uma API RESTful interna para gerenciar tarefas, permitindo seu cadastro, consulta, atualização, conclusão e remoção.

A aplicação seguirá separação em camadas:

- API: rotas e contratos HTTP.
- Service: regras de negócio.
- Repository: persistência.
- Models: validação e serialização de dados.

## Requisitos funcionais

### RF01 — Health check

A API deve disponibilizar `GET /health`, retornando:

- Status da aplicação.
- Timestamp UTC da resposta.

### RF02 — Criar tarefa

A API deve permitir criar uma tarefa com:

- `title`: obrigatório, entre 3 e 100 caracteres.
- `description`: opcional.
- `status`: opcional, com valor padrão `false`.
- `created_at`: preenchido automaticamente em UTC.
- `id`: UUID gerado pela aplicação.

### RF03 — Listar tarefas

A API deve listar todas as tarefas cadastradas.

### RF04 — Consultar tarefa

A API deve retornar uma tarefa específica a partir de seu UUID.

### RF05 — Atualizar tarefa

A API deve permitir atualizar o título, a descrição e o status de uma tarefa existente.

### RF06 — Remover tarefa

A API deve permitir remover uma tarefa a partir de seu UUID.

### RF07 — Validação e erros

A API deve:

- Retornar `422 Unprocessable Entity` para dados inválidos.
- Retornar `404 Not Found` quando uma tarefa não existir.
- Retornar respostas JSON padronizadas.

### RF08 — Documentação interativa

A API deve disponibilizar a documentação OpenAPI do FastAPI em `/docs`.

## Funcionalidade auxiliar entregue

O `PriorityAdvisor` calcula uma sugestão interna de prioridade durante a criação ou atualização da tarefa. Por padrão, usa uma heurística local; opcionalmente, pode consultar a OpenAI quando o SDK e `OPENAI_API_KEY` estiverem configurados. A sugestão não é persistida nem exposta no contrato público da API, e falhas do provedor não interrompem o fluxo CRUD.

## Requisitos não funcionais

### RNF01 — Tecnologia

- Python 3.12.
- FastAPI.
- Pydantic.
- Uvicorn.

### RNF02 — Comunicação

- API RESTful.
- Dados de entrada e saída em JSON.
- Identificadores no formato UUID.
- Datas e horários no padrão ISO 8601 em UTC.

### RNF03 — Organização

- Código organizado nas camadas `api`, `services`, `repositories` e `models`.
- Tipagem estática nas funções e modelos.
- Documentação mínima de módulos e endpoints.

### RNF04 — Qualidade

- Testes automatizados para health check e operações principais de tarefas.
- Validação de dados por meio de modelos Pydantic.
- Arquivos locais, ambiente virtual e configurações de editor ignorados pelo Git.

### RNF05 — Operação

- Execução local por Uvicorn.
- Endpoint de health check para monitoramento básico.
- Logs básicos de inicialização e erros.

## Fora de escopo

- Autenticação e autorização de usuários.
- Controle de perfis, permissões ou equipes.
- Interface web ou aplicativo móvel.
- Notificações por e-mail, chat ou push.
- Anexos em tarefas.
- Comentários, etiquetas, prioridade como campo público da tarefa ou datas de vencimento.
- Paginação, filtros avançados e ordenação.
- Auditoria completa de alterações.
- Integrações externas obrigatórias ou além da consulta opcional à OpenAI descrita acima.
- Deploy em produção, containerização e pipeline CI/CD.
- Banco de dados distribuído, cache ou mensageria.
