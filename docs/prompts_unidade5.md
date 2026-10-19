# Capítulo 5: Prompts para Codex/Copilot

## Prompts utilizados

### Prompt 1: Dependências
**Contexto:** Meu projeto Python usa FastAPI, Pydantic e outras bibliotecas.

**Objetivo:** Atualize um arquivo `requirements.txt` com as versões exatas das dependências instaladas no meu ambiente virtual atual. Além disso, sugira um `pyproject.toml` básico para o mesmo conjunto de dependências, caso eu queira migrar para Poetry.

**Resposta:** Arquivo `requirements.txt` atualizado e arquivo `pyproject.toml` criado


### Prompt 2: `.env.example` e `.env`
**Contexto:** O projeto usa integração opcional de LLM e posteriormente irá migrar a persistência de "em memória" para um banco de dados MySQL.

**Objetivo:** Criar arquivo `.env.example` com variáveis necessárias e valores placeholder seguros. Crie também o arquivo `.env` mesmo que as variáveis não existam ainda. Inclua-o no `.gitignore`, se ainda não estiver listado.

**Estilo:** Minimalista.

**Resposta:** Arquivos `.env.example` e `.env` criados.


### Prompt 3: Seção de IA no README
**Contexto:** Meu projeto de API de tarefas foi desenvolvido com o auxílio de genAI. Usei OpenIA Codex e GitHub Copilot como agentes para criação, refatorações multiarquivo e para gerar testes unitários. Preciso adicionar os desafios e ganhos que obtive no uso da IA no desenvolvimento deste projeto.

**Objetivo:** Escreva uma seção bem sucinta para o README intitulada "Como a IA Acelerou Este Projeto", destacando os ganhos de produtividade e as ferramentas utilizadas.

Mencione a importânciada revisão humana."
Inclua também:" A IA auxiliou em diversos momentos: geração do boilerplate, auxílio em diversos comandos para criação do ambiente e para uso do git e com sugestões de arquitetura e alguma refatoração. Mas a parte de documentação e testes foi impactante. Em resumo, usei em todas as fases do SDLC.".
E também "O Uso com Provider/MOdelos locais não foi satisfatório, seja em termos de qualidade , quanto em velocidade. Eu me deparei com falha no uso de ambiente virtual após a troca agente/provider de Modelos. O novo agente/provider ignorou a existência de ambiente virtual e instalou as dependências em ambiente global. Além disso ignorou instruções de formatação arquivo (caracter de final de linha).
No inicio da criação do ambiente o provider/modelo local se mostrou incompetente para criar os artefatos e acesso áreas do meu perfil no computador que eu não esperava, levantando preocupações quanto ao acesso indiscriminado em arquivos diversos do computador."
Melhore a redação, se preciso.
**Resposta:** Arquivo README atualizado com essa nova seção.


### Prompt 4: Revisão de README (Parte 1)
Analise meu README e responda:
1. O que falta para ser reproduzível em máquina limpa?
2. Quais seções estão fracas para onboarding técnico?
3. Como melhorar a seção de uso da IA?

**Resposta:** Em checklist objetivo.


### Prompt 5: Revisão de README (Parte 2)
Execute as melhorias que você sugeriu.


### Prompt 6: Checklist de release
**Contexto:** Vou publicar a versão `v1.0.0` no GitHub.
**Objetivo:** Atualize o arquivo `backlog.md` com as ações já completadas. Gere checklist final com itens técnicos e de documentação para release.
**Estilo:** Checkbox Markdown.
**Resposta:** Arquivo `docs/Checklist_Release_v1.0.0.md` com a lista completa.


### Prompt 7: Implementação final
**Contexto:** Vou publicar a versão `v1.0.0` no GitHub.
**Objetivo:** Verifique no arquivo `backlog.md` quais as tarefas faltantes e execute todas. Rode os testes após implementação. Atualize o arquivo `backlog.md` com as ações já completadas.
**Estilo:** Checkbox Markdown.
**Resposta:** Código gerado. Arquivo `backlog.md` atualizado.


### Prompt 8: Implementação final
**Contexto:** Vou publicar a versão `v1.0.0` no GitHub.
**Objetivo:** Verifique no arquivo `backlog.md` quais as tarefas faltantes e execute todas. Rode os testes após implementação. Atualize o arquivo `backlog.md` com as ações já completadas.
**Estilo:** Checkbox Markdown.
**Resposta:** Código gerado. Arquivo `backlog.md` atualizado.


### Prompt 9: Checklist de submissão final
**Contexto:** Chegou a hora de fazer revisão final.

**Objetivo:** Verifique:

- Se o arquivo `README.md` tem todas as seções essenciais (descrição, instalação, uso, tecnologias, seção de IA e limitações) e se a formatação está correta (Markdown renderizado).
- Se o arquivo `requirements.txt` lista todas as bibliotecas necessárias com suas versões corretas.
- Se os testes automatizados unitários e/ou de integração estão presentes, se passam com sucesso e se há instruções claras sobre como executá-los.
- Se uma Release ou Tag (ex.: `v1.0.0`) foi criada no GitHub para marcar a versão final do projeto.


### Prompt 10: Script de demo técnica
**Contexto:** Preciso apresentar o MVP em 5 minutos para stakeholders técnicos.
**Objetivo:** Criar roteiro com tempos por bloco e comandos para mostrar no terminal.
**Estilo:** Direto, sem marketing.
**Resposta:** Arquivo roteiro em Markdown na pasta `docs`. Incluir esse arquivo no `.gitignore`.


### Prompt 11: Demonstração do README_PLUS
**Contexto:** Preciso incluir elementos visuais, como capturas de tela ou Graphics Interchange Format (GIFs) animados, para um arquivo `README_PLUS` muito mais engajante e fácil de entender.
**Objetivo:** Gere exemplos de requisições `curl` para os endpoints `/tasks` (GET e POST) e `/tasks/{id}` (GET, PUT, DELETE) da minha API FastAPI de tarefas.
**Resultado:** Sugestões de como posso fazer isso. Não gere o arquivo ainda.


## Prompts futuros para Makefile

### Prompt: Makefile (original, mas não usado)
**Contexto:** Meu projeto Python tem um servidor FastAPI que roda com Uvicorn, testes com pytest, um formatador de código Black, com comandos de instalar dependências, executar API e testes.
**Objetivo:** Crie um Makefile que inclua os seguintes comandos (targets):

- `make install`: instala as dependências do `requirements.txt`.
- `make run`: inicia o servidor Uvicorn.
- `make test`: executa os testes pytest.
- `make format`: formata o código com Black.

**Estilo:** Simples e portátil.
**Resposta:** Forneça o conteúdo completo do Makefile.


### Prompt: Makefile alternativo
**Contexto:** Este projeto Python utiliza FastAPI, Uvicorn e pytest. As dependências estão declaradas em `requirements.txt`. Estou utilizando o VS Code com o GitHub Copilot no modo agente, que tem acesso ao código-fonte e à estrutura do repositório.
**Objetivo:** Criar um Makefile simples para automatizar as principais tarefas de desenvolvimento.

**Targets necessários:**

- `make install`: instalar as dependências de `requirements.txt`.
- `make run`: iniciar a API FastAPI com Uvicorn e recarga automática para desenvolvimento.
- `make test`: executar os testes automatizados com pytest.

**Instruções:**

1. Inspecione o projeto para identificar a estrutura de diretórios, o ponto de entrada da API, a configuração do Python e a localização dos testes.
2. Utilize os caminhos e as configurações existentes, sem presumir nomes de módulos ou diretórios.
3. Declare os targets como `.PHONY`.
4. Mantenha o Makefile simples, legível e sem dependências desnecessárias.
5. Não adicione o Black nem targets além dos três solicitados.
6. Crie ou atualize o arquivo Makefile na raiz do projeto.
7. Ao concluir, informe brevemente o que foi criado e quais comandos posso executar para validar o resultado.


### Prompt: Verificação do Makefile
Após criar o Makefile, valide sua implementação executando os targets `install`, `run` e `test`, sempre que o ambiente permitir.

1. Verifique se cada comando é executado corretamente e se utiliza as configurações reais do projeto.
2. Para o target `install`, execute a instalação das dependências somente no ambiente Python apropriado, respeitando o ambiente virtual e as configurações existentes.
3. Para o target `run`, inicie a API e confirme que o servidor sobe corretamente. Encerre o processo após a validação, evitando deixar processos em execução.
4. Para o target `test`, execute a suíte de testes e verifique o resultado.
5. Se algum comando falhar, investigue a causa, corrija os problemas relacionados ao Makefile e repita a validação, quando possível.
6. Não faça alterações desnecessárias no código da aplicação ou nas configurações do projeto para contornar falhas que não sejam causadas pelo Makefile.
7. Não execute operações destrutivas nem altere dependências ou configurações globais sem necessidade.
8. Se algum comando não puder ser executado devido a limitações do ambiente, permissões ou dependências ausentes, explique o motivo e indique como validá-lo manualmente.

Ao final, apresente um resumo dos comandos executados, seus resultados e eventuais problemas pendentes. Diferencie claramente as validações efetivamente realizadas daquelas que não puderam ser executadas. Não declare nenhuma validação como bem-sucedida sem evidências da execução.


## Prompts de testes e qualidade

### Prompt 1: Testes do service
**Contexto:** Tenho `TaskService` com CRUD de tarefas.
**Objetivo:** Gerar suite pytest cobrindo criação, listagem, atualização, exclusão e caso de erro por ID inexistente.
**Estilo:** Testes claros, nomes descritivos e fixtures simples.
**Resposta:** Código completo de `tests/test_task_service.py`.

> **Problema com o limite do Codex:**
>
> You've hit your usage limit. Upgrade your plan to continue, or try again at Nov 13, 2026, 10:27 PM.
> You're out of Codex messages.
> Your rate limit resets at Nov 13, 2026, 10:27 PM. To continue using Codex, start your free trial of Plus today.


### Prompt 2: Testes do PriorityAdvisor
**Contexto:** `PriorityAdvisor` possui heurística local e fallback quando chamada externa falha.
**Objetivo:** Gerar testes para os três níveis de prioridade e para fallback.
**Estilo:** Usar `monkeypatch` quando necessário.
**Resposta:** Código de `tests/test_priority_advisor.py`.

### Prompt 3: Testes de API
**Contexto:** API FastAPI com endpoints CRUD de `/tasks`.
**Objetivo:** Criar testes de rota com `TestClient` para status 201, 200, 204 e 404.
**Estilo:** Isolar dependência de repositório para evitar estado global entre testes.
**Resposta:** Código de `tests/test_task_routes.py`.


### Prompt 4: Refatoração DRY/SRP
Analise os arquivos `app/services/task_service.py` e `app/repositories/task_repository`.
**Objetivo:** Sugerir refatoração com foco em DRY e SRP sem mudar comportamento externo.
**Resposta:**

1. Lista de mudanças propostas.
2. Patch sugerido por arquivo.

### Prompt 5: README final técnico
**Contexto:** MVP de micro-API de tarefas com prioridade assistida por IA.
**Objetivo:** Gerar README completo com instalação, execução, testes, arquitetura, uso da IA, limitações e próximos passos.
**Estilo:** Markdown profissional e objetivo.
**Resposta:** README inteiro.

### Prompt 6: Revisão final de qualidade
Com base no código e nos testes atuais, gere um checklist com:

- Riscos técnicos restantes.
- Gaps de cobertura de teste.
- Melhorias prioritárias para a próxima release.

Resposta em bullets curtos.

### Prompt 7: Execução dos testes
**Contexto:** Temos bastantes testes que podemos executar para verificar se está tudo correto.
**Objetivo:** Executar todos os testes, gerando arquivo de relatório de resultado e sugestões de correções.
**Estilo:** Markdown profissional e objetivo.
**Resposta:** Arquivo `tests/test_results.md` com relatório de resultado e sugestões de correções, informando no arquivo a data e hora da execução do teste.
