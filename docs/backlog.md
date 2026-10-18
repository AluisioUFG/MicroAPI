# Backlog do MVP

## v0.1 — Estrutura inicial

- [x] **RT00 — Preparação do projeto**
  - Critérios de aceite:
    - [x] Repositório Git inicializado.
    - [x] Camadas `api`, `services`, `repositories` e `models` criadas.
    - [x] Modelos Pydantic iniciais e `.gitignore` configurados.

## v0.2 — API básica

- [x] **RF01 — Health check**
  - Critérios de aceite:
    - [x] `GET /health` retorna `200 OK`.
    - [x] A resposta contém `status: "ok"`.
    - [x] A resposta contém `timestamp` em UTC e formato ISO 8601.

- [x] **RF02 — Criar tarefa**
  - Critérios de aceite:
    - [x] `POST /tasks` cria uma tarefa com UUID.
    - [x] `title` é obrigatório e aceita entre 3 e 100 caracteres.
    - [x] `description` é opcional.
    - [x] `status` assume `false` quando não informado.
    - [x] `created_at` é gerado em UTC.

- [x] **RF03 — Listar tarefas**
  - Critérios de aceite:
    - [x] `GET /tasks` retorna `200 OK`.
    - [x] A resposta retorna uma lista de tarefas.

- [x] **RF04 — Consultar tarefa por ID**
  - Critérios de aceite:
    - [x] `GET /tasks/{task_id}` retorna a tarefa existente.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RF05 — Atualizar tarefa**
  - Critérios de aceite:
    - [x] `PUT /tasks/{task_id}` atualiza título, descrição e status.
    - [x] Retorna a tarefa atualizada.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RF06 — Remover tarefa**
  - Critérios de aceite:
    - [x] `DELETE /tasks/{task_id}` remove uma tarefa existente.
    - [x] Retorna `204 No Content`.
    - [x] Retorna `404 Not Found` para UUID inexistente.

- [x] **RT01 — Repositório em memória**
  - Critérios de aceite:
    - [x] Operações de persistência ficam isoladas na camada `repositories`.
    - [x] A camada de API não acessa a estrutura de dados diretamente.

## v0.3 — Persistência e qualidade

- [x] **RT02 — Validação e tratamento de erros**
  - Critérios de aceite:
    - [x] Dados inválidos retornam `422 Unprocessable Entity`.
    - [x] Recursos inexistentes retornam `404 Not Found`.
    - [x] Respostas de erro seguem formato JSON consistente.

- [x] **RT03 — Testes automatizados**
  - Critérios de aceite:
    - [x] Existem testes de rota para criar, listar, consultar, atualizar e remover tarefas.
    - [x] Existem testes para recurso inexistente.
    - [x] Existe teste para `GET /health`, incluindo status, payload e timestamp UTC.
    - [x] Existem testes HTTP para título inválido e UUID malformado (`422`).
    - [x] Erros inesperados retornam `500` sem expor detalhes e são registrados em log.
    - [x] Os 21 testes passam localmente (verificação em 18/10/2026).

- [x] **RT04 — Tipagem e organização**
  - Critérios de aceite:
    - [x] Funções públicas possuem tipagem estática.
    - [x] Regras de negócio ficam na camada `services`.
    - [x] Rotas ficam na camada `api`.
    - [x] Modelos Pydantic ficam na camada `models`.

- [x] **RT05 — Observabilidade básica**
  - Critérios de aceite:
    - [x] A aplicação registra eventos de inicialização.
    - [x] Erros inesperados são registrados em log.

## v1.0 — MVP publicado

- [x] **RT06 — Documentação da API**
  - Critérios de aceite:
    - [x] Documentação OpenAPI está disponível em `/docs`.
    - [x] Rotas possuem docstrings usadas na documentação OpenAPI.
    - [x] README contém instruções atualizadas para execução local.

- [x] **RT07 — Revisão de escopo**
  - Critérios de aceite:
    - [x] Todos os itens planejados das releases anteriores estão concluídos.
    - [x] A sugestão interna de prioridade e a integração OpenAI opcional estão delimitadas no escopo.
    - [x] O documento `docs/escopo-mvp.md` está alinhado ao comportamento entregue.

- [x] **RT08 — Publicação da versão MVP**
  - Critérios de aceite:
    - [x] Código da branch `main` está enviado ao repositório remoto.
    - [x] Dependências base estão registradas em `requirements.txt`.
    - [x] A instalação limpa e a inicialização com `python -m uvicorn app.main:app --reload` foram verificadas.
    - [x] Metadados de versão estão atualizados para `1.0.0`.
    - [x] Tag `v1.0.0` e release do GitHub foram criadas.
