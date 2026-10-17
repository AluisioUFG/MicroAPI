Prompt 1 - Modelo Pydantic
Contexto: API de tarefas em FastAPI para uso interno de equipe.
Objetivo: Gerar modelos TaskCreate, TaskUpdate e TaskOut com tipagem e validações.
Estilo: Pydantic v2, código limpo e docstrings curtas.
Resposta: Apenas código de app/models/task.py.

git add app/models/task.py
git commit -m "feat(models): adiciona contratos de criação, atualização e saída de tarefas"  
git push origin main



Prompt 2 - Repositorio inicial
Contexto: Preciso de persistência inicial enxuta para viabilizar a primeira release. 
Objetivo: Criar TaskRepository em memoria com create, list, get_by_id, update e delete. 
Estilo: Python tipado, sem dependências externas. 
Resposta: Código completo de app/repositories/task_repository.py.

git add app/repositories/task_repository.py
git commit -m "feat(repository): adiciona persistência de tarefas em memória"




Prompt 3 - PriorityAdvisor com fallback
Contexto: Quero rodar sem custo de API quando nao houver chave, um serviço de PriorityAdvisor, pára sugerir prioridade.
Objetivo: Implementar PriorityAdvisor com heuristica local e chamada opcional a LLM quando OPENAI_API_KEY existir. Encapsular chamada em "PriorityAdvisor". Ler credenciais de variáveis de ambiente. Tratar timeout e erro de provedor. Nunca quebrar fluxo principal do CRUD.
Estilo: Falha segura, timeout e fallback obrigatório. 
Resposta: Código de app/services/priority_advisor.py.




Prompt 4 - Service com regra de prioridade
Contexto: A prioridade da tarefa pode ser sugerida automaticamente. 
Objetivo: Criar TaskService que use TaskRepository e PriorityAdvisor. 
Estilo: Separar regra de negocio da camada de API. 
Resposta: Código de app/services/task_service.py.

git add .
git commit -m "feat(services): adiciona serviço de tarefas e sugestão de prioridade com fallback local"



Prompt 5 - Rotas CRUD
Contexto: FastAPI com TaskService pronto.
Objetivo: Criar rotas POST/GET/PUT/DELETE para tarefas com status HTTP corretos e tratamento de 404.
Estilo: Router separado em app/api/task_routes.py. 
Resposta: Apenas o código do arquivo.

git add app/api/task_routes.py
git commit -m "feat(api): adiciona rotas CRUD para tarefas"


Prompt 6 - Atualização de mermaid  e readme.md
COntexto: projeto atual
Objetivo: atualizar os arquivo docs\arquitetura.md, readme.md com as alterações efetuadas
Estilo: manter estilo atual
Resposta: arquivos docs\arquitetura.md e readme.md atualizados


Prompt 7 - Registrar o router de tarefas na aplicação e Adicionar validação e tratamento global de erros
Contexto: Tarefas da versão v0.2 listada no arquivo README.md estão pendentes. São elas "Registrar o router de tarefas na aplicação" e "Adicionar validação e tratamento global de erros".
Objetivo: Crie o código relativo as essas tarefas e atualize os arquivos docs\arquitetura.md e readme.md
Estilo: manter estilo atual
Resposta: router registrado; validação e tratamento global de erros adiconados; arquivos docs\arquitetura.md e readme.md atualizados;

git add .



Prompt 8 - Revisão técnica
Revise os arquivos do core da API e responda:
1) Quais pontos de acoplamento estão altos?
2) Onde faltam validações?
3) Quais 5 testes devo priorizar na próxima release? Resposta em checklist.


Resposta da IA:

1) Pontos de acoplamento altos

- [ ] `task_routes.py` instancia `TaskRepository` e `PriorityAdvisor` diretamente; dificulta trocar implementação e isolar testes.
- [ ] `TaskService` depende de classes concretas, não de protocolos/interfaces.
- [ ] `PriorityAdvisor` concentra regra local, leitura de ambiente, criação do cliente OpenAI e chamada externa.
- [ ] Sugestões de prioridade ficam em um segundo estado em memória no `TaskService`, separado do repositório.

2) Validações ausentes

- [ ] `TaskUpdate` aceita corpo vazio; deveria exigir ao menos um campo para atualizar.
- [ ] `title` aceita somente espaços; aplique `strip` e rejeite valor vazio.
- [ ] `description` não possui limite de tamanho.
- [ ] O conteúdo enviado ao advisor não possui limite antes de eventual chamada externa.
- [ ] Não há garantia explícita de que `created_at` seja sempre timezone-aware fora do repositório.

3) Cinco testes prioritários

- [ ] `GET /health` retorna `200`, `status: "ok"` e timestamp UTC válido.
- [ ] `POST /tasks` cria tarefa com UUID, `status=false` e `created_at` UTC.
- [ ] Payload inválido — título curto, vazio ou ausente — retorna `422` no formato global definido.
- [ ] Fluxo CRUD completo: criar, listar, consultar, atualizar e remover uma tarefa.
- [ ] Recurso inexistente retorna `404` para `GET`, `PUT` e `DELETE`; falha do `PriorityAdvisor` não impede a criação.




Prompt 9 - Backlog
Contexto: Arquivo docs/backlog.py. Os numeros de release em docs/backlog.py e readme.md não se correspondem.
Objetivo: Atualize o arquivo docs/backlog.py. Ajuste para que os numeros de release em docs/backlog.py e readme.md correspondam.
Estilo: manter estilo atual dos arquivos
Resposta: Arquivos atualizados


Prompt 10 - Backlog
Contexto: Arquivo docs/backlog.py foi atualizado com numero de versão corretos, mas as tarefas já executadas na versão v0.2 nao foram marcadas
Objetivo: Atualize o arquivo docs/backlog.py marcando o que foi de fato concluído
Estilo: manter estilo atual do arquivo
Resposta: Arquivo atualizado com tarefas concluidas devidamente marcadas


git add .   
git commit -m "docs: atualiza roadmap e backlog da versão v0.2"  