Prompt 1 - Testes do service
Contexto: Tenho TaskService com CRUD de tarefas.
Objetivo: Gerar suite Pytest cobrindo criação, listagem, atualização, exclusão e caso de erro por ID inexistente.
Estilo: Testes claros, nomes descritivos e fixtures simples. 
Resposta: Código completo de tests/test_task_service.py.


Problemas com o limit do codex:
	You've hit your usage limit. Upgrade your plan to continue, or try again at Nov 13, 2026, 10:27 PM.
	You're out of Codex messages
	Your rate limit resets on Nov 13, 2026, 10:27 PM. To continue using Codex, start your free trial of Plus today.



Prompt 2 - Testes do PriorityAdvisor
Contexto: PriorityAdvisor possui heuristica local e fallback quando chamada externa falha.
Objetivo: Gerar testes para os tres niveis de prioridade e para fallback. 
Estilo: Usar monkeypatch quando necessário. 
Resposta: Código de tests/test_priority_advisor.py.

Prompt 3 - Testes de API
Contexto: API FastAPI com endpoints CRUD de /tasks.
Objetivo: Criar testes de rota com Testclient para status 201, 200, 204 e 404. 
Estilo: Isolar dependencia de repositorio para evitar estado global entre testes. 
Resposta: Codigo de tests/test_task_routes.py.


Prompt 4 - Refatoracao DRY/SRP
Analise os arquivos app/services/task_service.py e app/repositories/task_repository 
Objetivo: Sugerir refatoracao com foco em DRY e SRP sem mudar comportamento externo. 
Resposta: 1) lista de mudanças propostas 2) patch sugerido por arquivo.

Prompt 5 - README final técnico
Contexto: MVP de micro-API de tarefas com prioridade assistida por IA.
Objetivo: Gerar README completo com instalação, execução, testes, arquitetura, uso da IA, limitações e próximos passos
Estilo: Markdown profissional e objetivo. 
Resposta: README inteiro.

Prompt 6 - Revisão final de qualidade
Com base no código e nos testes atuais, gere um checklist com:
- Riscos técnicos restantes
- Gaps de cobertura de teste
- Melhorias prioritárias para a próxima release 
Resposta em bullets curtos.

Prompt 7 - Execução dos teste
Contexto: Temos bastantes testes que podemos executar para verificar se está tudo correto.
Objetivo: Executar todos os teste, gerando arquivo de relatório de resultado e sugestões de correções.
Estilo: Markdown profissional e objetivo.
Resposta: arquivo tests/test_results.md com relatório de resultado e sugestões de correções, informando no arquivo a data e hora da execução do teste.