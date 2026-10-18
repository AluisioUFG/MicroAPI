# Checklist de Release v1.0.0

## Qualidade técnica

- [x] Python 3.12 está definido como versão-alvo.
- [x] Dependências base estão fixadas em `requirements.txt`.
- [x] `python -m pip check` não encontrou dependências incompatíveis (18/10/2026).
- [x] Suíte atual passou: 15 testes, 0 falhas (18/10/2026, Windows/Python 3.12).
- [x] Endpoints CRUD, validação Pydantic e handlers de erro `404`, `422` e `500` estão implementados.
- [x] `.env` está no `.gitignore`; `.env.example` contém apenas placeholders.
- [ ] Adicionar testes para `GET /health`, limites de título, UUID inválido e respostas `422`.
- [ ] Adicionar teste para garantir que erros `500` não exponham detalhes internos.
- [ ] Implementar log de inicialização ou revisar esse critério de observabilidade no escopo.
- [ ] Criar ambiente virtual limpo, instalar `requirements.txt`, executar testes e iniciar a API.
- [ ] Fazer smoke test de `/health`, CRUD, `/docs` e `/openapi.json` com a API em execução.
- [ ] Validar em cada sistema operacional que o README declara suportar (Windows, Linux e macOS), ou restringir o suporte documentado.
- [ ] Validar o caminho opcional da OpenAI com a versão `openai==3.35.1`, sem registrar ou expor credenciais.
- [ ] Revisar dependências e riscos de segurança antes de publicar.

## Documentação

- [x] README documenta instalação, execução, testes, API, arquitetura, limitações e configuração opcional da LLM.
- [x] README informa que `.env` não é carregado automaticamente e que as variáveis MySQL ainda são placeholders.
- [x] Documentação OpenAPI está disponível em `/docs`.
- [ ] Alinhar `docs/escopo-mvp.md` ao comportamento entregue: a sugestão de prioridade e a integração opcional OpenAI aparecem atualmente como fora de escopo.
- [ ] Revisar o backlog e concluir ou adiar formalmente os critérios pendentes de testes e observabilidade.
- [ ] Decidir se Poetry fará parte desta release; se sim, gerar/versionar `poetry.lock` e validar a instalação com Poetry.
- [ ] Preparar notas da release com funcionalidades, limitações conhecidas e instruções de instalação.
- [ ] Revisar renderização de Markdown, links e exemplos de comandos antes da publicação.

## Versionamento e publicação

- [x] Repositório remoto `origin` está configurado.
- [ ] Atualizar a versão do projeto em `pyproject.toml` para `1.0.0`.
- [ ] Confirmar que `main` está sincronizada com `origin` e que o working tree está limpo.
- [ ] Criar a tag anotada `v1.0.0` no commit aprovado.
- [ ] Enviar a branch e a tag para o GitHub.
- [ ] Criar a GitHub Release `v1.0.0` com as notas revisadas.
- [ ] Conferir a página da release e validar o procedimento de instalação a partir do commit/tag publicado.