# miuuyy/codex-chatgpt-web

Data: 2026-09-26. Fontes consultadas no GitHub nesta data; índice canônico e stack `evaluate-and-import-skill` lidos antes da seleção. Avaliação estática, sem instalar, executar ou baixar binários da fonte.

## Decisão

Classificação: **D — ferramenta técnica**.

Não importar como skill separada no Arsenal. O repositório implementa uma ponte local entre Codex e uma sessão autenticada do ChatGPT Web, usando launcher próprio, Electron/browser automation, Playwright, MCP e o `openai/tunnel-client`. O ganho está na arquitetura e na integração executável, não em uma metodologia textual reutilizável pelo ChatGPT.

A ação útil é registrar a avaliação e manter os padrões arquiteturais como referência para tarefas futuras de gateways, bridges MCP e integração de harnesses. Não há ganho suficiente para criar uma nova skill porque o Arsenal já cobre os aspectos metodológicos relevantes com `model-routing-gateway`, `system-design-engineering`, `skill-security-review`, `runtime-ui-verification` e `library-version-grounding`.

## O que faz de verdade

- injeta modelos ChatGPT Web no seletor nativo do Codex;
- encaminha turns do Codex para uma sessão web autenticada do ChatGPT;
- oferece modo browser-only e modo full harness com MCP;
- conecta ações do ChatGPT de volta às ferramentas do turn corrente do Codex;
- mantém estado de login em uma partição Electron privada;
- usa listener local em loopback e túnel outbound para o conector MCP;
- empacota runtime, launcher, diagnósticos, smoke tests e fluxos de atualização.

É portanto um produto/bridge local, não uma Agent Skill autônoma.

## Ganho incremental para o Arsenal

O repositório traz bons padrões que vale preservar como referência:

1. **capabilities por turn**: token aleatório escopado ao turn para ligar chamadas MCP ao contexto autorizado;
2. **fail closed**: drift de UI, modelo ausente, connector ausente ou tool ausente falham explicitamente;
3. **separação de modos**: browser-only, full harness e zero-risk com superfícies de permissão distintas;
4. **loopback + lifecycle control**: superfície Responses local separada de endpoints administrativos autenticados;
5. **isolamento de sessão**: tabs vinculadas a task/turn, limites de concorrência e perfil persistente privado;
6. **versionamento e invariantes**: runtime, catálogo, protocolo e conectores são tratados como contratos compatíveis, não como heurística silenciosa.

Esses padrões podem informar futuras implementações, mas não justificam duplicar skills existentes.

## Dependências e portabilidade

Dependências principais observadas: Bun 1.4.0, Electron/launcher empacotado, Playwright Core, MCP SDK, Chromium BiDi, tunnel-client e acesso a uma sessão ChatGPT autenticada.

A solução depende de automação de UI e de componentes executáveis específicos. Não existe equivalente textual que possa ser “adaptado” para funcionar dentro do ChatGPT sem esse runtime. Por isso, a parte operacional não é portátil para uma skill do Arsenal.

## Segurança

Veredito: **CAUTION** para uso da ferramenta; **APPROVE** para manter apenas esta avaliação textual no Arsenal.

Pontos positivos:
- listener principal em `127.0.0.1`;
- endpoints administrativos protegidos por bearer token local;
- credenciais/tokens descritos como armazenados em área privada do usuário;
- tunnel outbound, sem porta pública de entrada;
- checksums e manifestos são declarados para runtime e tunnel-client;
- aprovações automáticas de tools ficam desabilitadas por padrão;
- documentação reconhece UI drift e falha explicitamente em vez de trocar transporte/modelo silenciosamente.

Riscos relevantes:
- a partição persistente do Electron contém sessão autenticada do ChatGPT e deve ser tratada como credencial sensível;
- um processo sob o mesmo usuário local consegue atingir o endpoint Responses em loopback;
- Full mode pode expor tools de escrita/comando disponíveis no turn corrente do Codex;
- conteúdo de repositório e tool outputs podem carregar prompt injection;
- browser automation depende de DOM/labels do ChatGPT, portanto mudanças de UI podem interromper o fluxo;
- instaladores shell/PowerShell e binários de release não foram auditados nesta avaliação;
- dependências e cadeia completa de supply chain não foram revisadas arquivo a arquivo.

Não executei instaladores, binários, scripts ou smoke tests da fonte.

## Quando faria sentido usar

Como ferramenta externa, faz sentido apenas quando o objetivo explícito for operar Codex usando a sessão Web do ChatGPT e o usuário aceitar os riscos de automação de browser e credenciais locais. Não deve ser tratado como substituto da API oficial, nem como capability nativa do ChatGPT.

## Relação com skills existentes

- `model-routing-gateway`: cobre desenho de roteamento, fallback, orçamento e observabilidade;
- `system-design-engineering`: cobre arquitetura, falhas, componentes e evolução operacional;
- `skill-security-review`: cobre trust boundaries, credenciais, rede, execução e supply chain;
- `runtime-ui-verification`: útil para verificar consequências de mudanças em automação de UI;
- `library-version-grounding`: cobre decisões vinculadas às versões reais do stack.

Conclusão: **registrar, não importar**. Criar uma nova skill produziria sobreposição e esconderia o fato de que o valor real depende do runtime externo.

## Fontes

- https://github.com/miuuyy/codex-chatgpt-web
- https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md
- https://github.com/miuuyy/codex-chatgpt-web/blob/main/docs/architecture.md
- https://github.com/miuuyy/codex-chatgpt-web/blob/main/docs/security-model.md
- https://github.com/miuuyy/codex-chatgpt-web/blob/main/package.json

## Limites da validação

Avaliação estática do conteúdo público consultado em 2026-09-26. Não validei comportamento em runtime, autenticidade dos binários publicados, assinatura de releases, hashes de artefatos, comportamento do tunnel-client, conformidade operacional com termos de terceiros ou o conjunto completo de dependências transitivas.
