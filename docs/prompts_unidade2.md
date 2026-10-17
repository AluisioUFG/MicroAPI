Prompt 1 - Escopo MVP
Contexto: MVP de micro-API de tarefas para uso de equipe interna.
Objetivo: Gerar documento de escopo com objetivo, requisitos funcionais, nao funcionais e fora de escopo.
Estilo: Linguagem técnica, direta, em Markdown.
Resposta: Forneça o conteúdo completo de docs/escopo-mvp.md.

Prompt 2 - Backlog por releases
Contexto: O produto sera entregue em 3 releases: core, qualidade e entrega final.
Objetivo: Criar backlog minimo com IDs RF/RT e critérios de aceite.
Estilo: Checklist Markdown.
Resposta: Conteúdo de docs/backlog.md.

Prompt 3 - Arquitetura Mermaid
Contexto: FastAPI com camadas API, Service, Repository. Fluxo base: Cliente -> API -> Service -> Repository -> Storoge
Objetivo: Gerar diagrama Mermaid de componentes e fluxo de dados. Estilo: Simples, legivel e versionavel. 
Resposta: Salve no arquivo docs/arquitetura.md.

Prompt 4 - Conventional Commits
Contexto: Adicionei docs/escopo-mvp.md, docs/arquitetura.md e docs/backlog.md. 
Objetivo: Sugerir 3 mensagens de commit no padrão Conventional Commits. 
Resposta: Apenas as 3 linhas de commit.

docs(escopo-mvp.md): adiciona escopo inicial do MVP
docs(arquitetura.md): documenta arquitetura em camadas da API
docs(backlog.md): adiciona backlog de releases e critérios de aceite


(Comandos git executados manualmente)


Contexto: ao executar git add docs\escopo-mvp.md  recebi a msg : "warning: in the working copy of 'docs/escopo-mvp.md', LF will be replaced by CRLF the next time Git touches it"
Objetivo: explique e dê uma solução para isso


É apenas um aviso, não um erro. O arquivo foi adicionado normalmente.
Ele informa que o arquivo está com finais de linha LF e que, pela configuração atual do Git no Windows, poderá ser convertido para CRLF na cópia local.
Você pode continuar com o commit. 
Para padronizar finais de linha no projeto futuramente, podemos adicionar um arquivo .gitattributes com LF para arquivos .py e .md.


Objetivo: Crie o arquivo .gitattributes
Resposta: arquivo criado


(Comandos git executados manualmente)
git add .gitattributes
git commit -m "docs(escopo-mvp.md): adiciona escopo inicial do MVP e chore(.gitattributes): adiciona regras de normalização de finais de linha"
git add docs\arquitetura.md 
git commit -m "docs(arquitetura.md): documenta arquitetura em camadas da API"  
git add docs\backlog.md
git commit -m "docs(backlog.md): adiciona backlog de releases e critérios de aceite"
git push origin main   



Prompt 5 - Revisão de planejamento
Analise este escopo e backlog e responda:
1) O que esta grande demais para a release inicial?
2) O que esta faltando para testabilidade?
3) Quais 3 riscos técnicos devo mitigar antes da implementação? 
Resposta em bullets curtos.


Reposta da IA

**1) Grande demais para a release inicial**

- CRUD completo com quatro camadas já é o limite; considere adiar `PUT` e `DELETE` se o prazo for curto.
- Não deixe testes apenas na Release 2: ao menos os fluxos críticos do Core devem nascer testados.
- Logs de inicialização e tratamento global de erros podem ficar para a Release 2.

**2) Faltando para testabilidade**

- Definir framework e dependências de teste: `pytest`, `httpx` e `TestClient`.
- Criar estratégia para isolar/resetar o repositório em memória entre testes.
- Definir interfaces/injeção de dependência para `Repository`, relógio e geração de UUID.
- Especificar contratos de resposta de sucesso e erro para testes de API.

**3) Três riscos técnicos a mitigar**

- Arquivos atuais apresentam problemas de codificação (`GestÃ£o`, `atualizaÃ§Ã£o`); padronize UTF-8 antes de novos commits.
- Repositório em memória perde todos os dados ao reiniciar e pode ter problemas de concorrência.
- Regras de atualização estão ambíguas: defina se será `PUT` completo ou atualização parcial, campos imutáveis e respostas de erro.