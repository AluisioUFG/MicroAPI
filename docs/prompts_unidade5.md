Capitulo 5 - Prompts para Codex/Copilot

Prompt 1 - Dependencias
Contexto: Meu projeto Python usa FastAPI, Pydantic e outras bibliotecas.  
Objetivo: Atualize um arquivo requirements.txt com as versões exatas das dependências instaladas no meu ambiente virtual atual. Além disso, sugira um pyproject.toml básico para o mesmo conjunto de dependências, caso eu queira migrar para Poetry.
Resposta: Arquivo requirements.txt atualizado e arquivo pyproject.toml criado


Prompt 2 - .env.example e .env
Contexto:  projeto usa integração opcional de LLM e posteriormente irá migrar a persistência de "em memória" para um banco de dados MySQL.
Objetivo: Criar arquivo .env.example com variáveis necessárias e valores placeholder seguros. Crie também o arquivo .env mesmo que as variáveis não existam ainda. INclua-o no .igitignore, sem ainda não estiver lá listado.
Estilo: Minimalista.
Resposta: Arquivos ".env.example" e ".env"criado


Prompt 3 - Seção de IA no README:
Contexto: Meu projeto de API de tarefas foi desenvolvido com o auxílio de genAI. Usei OpenIA Codex e GitHub Copilot como agentes para criação, refatorações multiarquivo e para gerar testes unitários. Preciso adicionar os desafios e ganhos que obtive no uso da IA no desenvolviento deste projeto
Objetivo: Escreva uma seção bem sucinta para o README intitulada 'Como a IA Acelerou Este Projeto', destacando os ganhos de produtividade e as ferramentas utilizadas. 
Mencione a importânciada revisão humana."
Inclua também:" A IA auxiliou em diversos momentos: geração do boilerplate, auxílio em diversos comandos para criação do ambiente e para uso do git e com sugestões de arquitetura e alguma refatoração. Mas a parte de documentação e testes foi impactante. Em resumo, usei em todas as fases do SDLC.".
E também "O Uso com Provider/MOdelos locais não foi satisfatório, seja em termos de qualidade , quanto em velocidade. Eu me deparei com falha no uso de ambiente virtual após a troca agente/provider de Modelos. O novo agente/provider ignorou a existência de ambiente virtual e instalou as dependências em ambiente global. Além disso ignorou instruções de formatação arquivo (caracter de final de linha).
No inicio da criação do ambiente o provider/modelo local se mostrou incompetente para criar os artefatos e acesso áreas do meu perfil no computador que eu não esperava, levantando preocupações quanto ao acesso indiscriminado em arquivos diversos do computador."
Melhore a redação, se preciso.
Resposta: arquivo Readme atualizado com essa nova seção


Prompt 4 - Revisão de README (Parte 1)
Analise meu README e responda:
1) 0 que falta para ser reproduzivel em maquina limpa?
2) Quais secoes estão fracas para onboarding tecnico?
3) Como melhorar a secao de uso da IA? 
Resposta em checklist objetivoe 


Prompt 5 - Revisão de README (Parte 2)
Execute as melhorias que você sugeriu


Prompt 6 - Checklist de release
Contexto: Vou publicar a versão v1.0.0 no GitHub
Objetivo: Atualize o arquivo backlog.md com as ações já completadas. Gere checklist final com itens técnicos e de documentação para release. 
Estilo: Checkbox Markdown. 
Resposta: Arquivo docs/Checklist_Release_v1.0.0.md com a lista completa.


Prompt 7 - IMplementação final
Contexto: Vou publicar a versão v1.0.0 no GitHub
Objetivo: Verifique no arquivo backlog.md quais as tarefas faltantes e execute todas. Rode os testes após implemetação. Atualize o arquivo backlog.md com as ações já completadas
Estilo: Checkbox Markdown. 
Resposta: Codigo gerado. arquivo backlog.md atualizado.


Prompt 8 - IMplementação final
Contexto: Vou publicar a versão v1.0.0 no GitHub
Objetivo: Verifique no arquivo backlog.md quais as tarefas faltantes e execute todas. Rode os testes após implemetação. Atualize o arquivo backlog.md com as ações já completadas
Estilo: Checkbox Markdown. 
Resposta: Codigo gerado. arquivo backlog.md atualizado.


Prompt 9 - Checklist de Submissão Final
Contexto: Chegou a hora de fazer revisão final
Objetivo: verifique 
- Se o arquivo README.md tem todas asseções essenciais (descrição, instalação, uso,tecnologias, seçãodeIA, limitações)  e se a formatação está correta (Markdown renderizado)
- se o arquivo requirements.txt lista todas as bibliotecas necessárias com suas versões corretas
- Se os testes automatizados unitários e/ou de integração estão presentes, se eles passam com sucesso e se há instruções claras sobre comoexecutá-los
- se Uma Release ou Tag (ex: v1.0.0) foi criada no GitHub para marcar a versão final do projeto


Prompt 10 - Script de demo técnica
Contexto: Preciso apresentar o MVP em 5 minutos para stakeholders técnicos. 
Objetivo: Criar roteiro com tempos por bloco e comandos para mostrar no terminal
stilo: Direto, sem marketing. 
Resposta: Arquivo Roteiro em Markdown na pasta docsc. INcluir esse arquivo no .ignore. 



Prompt 4 - Demonstração
COntexto: Preciso incluir elementos visuais, como capturas de tela ou Graphics Interchange Format (GIFs) animados, para um arquivo README_PLUS muito mais engajante e fácil de entender
Objetivo: Gere exemplos de requisições curl para os endpoints/tasks (GET e POST) e /tasks/{id} (GET, PUT, DELETE) da minha API FastAPI de tarefas
Resultado: SUgestões de como posso fazer isso. Não gere o arquivo ainda










##################################################################################################################################################################################################################
PROMPTS FUTURO PARA MAKE



Prompt - Makefile (original mas não usado)
Contexto: Meu projeto Python tem um servidor FastAPI que roda com Uvicorn, testes com Pyteste, um formatador de código black, com comandos de instalar dependências, executar API e testes
Objetivo: Crie um Makefile que inclua os seguintes comandos (targets):
make install: Instala as dependências do requirements.txt.
make run: Inicia o servidor Uvicorn.
make test: Executa os testes Pytest.
make format: Formata o código com Black.
Estilo: Simples e portável.
Resposta: Forneça o conteúdo completo do Makefile.


 
Prompt - Makefile Alternativo
Contexto: Este projeto Python utiliza FastAPI, Uvicorn e pytest. As dependências estão declaradas em requirements.txt. Estou utilizando o VS Code com o GitHub Copilot no modo agente, que tem acesso ao código-fonte e à estrutura do repositório.
Objetivo: Criar um Makefile simples para automatizar as principais tarefas de desenvolvimento.
Targets necessários:
make install: instalar as dependências de requirements.txt.
make run: iniciar a API FastAPI com Uvicorn e recarga automática para desenvolvimento.
make test: executar os testes automatizados com pytest.

Instruções:
Inspecione o projeto para identificar a estrutura de diretórios, o ponto de entrada da API, a configuração do Python e a localização dos testes.
Utilize os caminhos e as configurações existentes, sem presumir nomes de módulos ou diretórios.
Declare os targets como .PHONY.
Mantenha o Makefile simples, legível e sem dependências desnecessárias.
Não adicione o Black nem targets além dos três solicitados.
Crie ou atualize o arquivo Makefile na raiz do projeto.
Ao concluir, informe brevemente o que foi criado e quais comandos posso executar para validar o resultado.



Prompt - Verificação do Make
Após criar o Makefile, valide sua implementação executando os targets install, run e test, sempre que o ambiente permitir.

    Verifique se cada comando é executado corretamente e se utiliza as configurações reais do projeto.
    Para o target install, execute a instalação das dependências somente no ambiente Python apropriado, respeitando o ambiente virtual e as configurações existentes.
    Para o target run, inicie a API e confirme que o servidor sobe corretamente. Encerre o processo após a validação, evitando deixar processos em execução.
    Para o target test, execute a suíte de testes e verifique o resultado.
    Se algum comando falhar, investigue a causa, corrija os problemas relacionados ao Makefile e repita a validação, quando possível.
    Não faça alterações desnecessárias no código da aplicação ou nas configurações do projeto para contornar falhas que não sejam causadas pelo Makefile.
    Não execute operações destrutivas nem altere dependências ou configurações globais sem necessidade.
    Se algum comando não puder ser executado devido a limitações do ambiente, permissões ou dependências ausentes, explique o motivo e indique como validá-lo manualmente.

Ao final, apresente um resumo dos comandos executados, seus resultados e eventuais problemas pendentes. Diferencie claramente as validações efetivamente realizadas daquelas que não puderam ser executadas. Não declare nenhuma validação como bem-sucedida sem evidências da execução.