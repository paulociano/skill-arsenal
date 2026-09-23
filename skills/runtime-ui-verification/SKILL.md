---
name: runtime-ui-verification
description: "Verificar mudanças de UI no app em execução por consequências de domínio, estado e rede além da aparência visual."
---

# runtime-ui-verification

## Objetivo

Verificar mudanças de UI/full-stack no aplicativo realmente em execução, declarando a consequência esperada antes da ação e usando evidência de runtime além da aparência visual.

## Quando usar

Verificar mudanças de UI no app em execução por consequências de domínio, estado e rede além da aparência visual.

## Princípio central

**Uma tela que parece correta não prova que a aplicação fez a coisa certa.**

## Workflow

1. Declarar a consequência esperada **antes** de agir.
2. Executar a ação no app real.
3. Observar, conforme disponível:
   - sinal/evento de domínio;
   - state/store;
   - request/response de rede;
   - console/runtime errors;
   - route;
   - DOM/rendered result.
4. Classificar como `pass`, `fail` ou `couldn't tell`.
5. Se falhar, localizar a camada causal e corrigir.
6. Reexecutar a **mesma expectativa**, sem enfraquecê-la para ficar verde.
7. Para fluxos críticos recorrentes, salvar/reutilizar um replay determinístico quando a ferramenta suportar.

## Força de evidência

Preferir, nesta ordem aproximada:

1. consequência de domínio explícita;
2. state real;
3. network effect;
4. elemento/render;
5. ausência de erro.

Ausência de erro sozinha pode passar com um botão morto.

## False-green gate

Um teste verde não prova o app quando:

- a assertion não consegue falhar;
- o teste usa mock mas o app usa outro caminho real;
- UI mudou e state não;
- request ocorreu mas resultado nunca foi consumido;
- o fluxo relevante nunca foi exercitado.

Quando confirmado, corrigir também o teste/oracle que deixou a regressão passar.

## Estratégia de evidência no navegador

Antes de verificar UI no browser, escolher a evidência adequada:

- DOM para structure/labels/state exposto;
- screenshot/vision para layout/clipping/visual;
- network/state quando consequência funcional importar;
- hybrid para fluxos onde visual e estado precisam concordar.

Permissões de page context devem ser task-scoped. History, tab sets, screenshots ou microphone não entram como contexto “por precaução”.

## Observe, act, extract

Em browser automation com LLM, separar responsabilidades reduz risco e ambiguidade:

- **observe**: localizar elementos/estado real e produzir targets verificáveis;
- **act**: executar a mutação mínima necessária;
- **extract**: retornar dados em schema validado quando a tarefa pede informação estruturada.

Credenciais, secrets e valores sensíveis devem preferir preenchimento determinístico fora do modelo quando a ferramenta permitir. O modelo pode escolher a ação sem precisar receber o segredo. Extração estruturada precisa validar schema e source state antes de ser tratada como dado confiável.

Esse padrão, observado em Stagehand, complementa a action-space dinâmica já descrita abaixo sem exigir sua SDK.

## Action space observada e guardas de frescor

Quando o navegador controlável expuser DOM/elementos acionáveis, prefira decisões sobre uma **action space derivada do estado observado**, não selectors, coordenadas ou JavaScript inventados pelo modelo.

1. Observar a página e construir uma lista pequena de operações realmente suportadas no estado atual.
2. Para cada operação, oferecer apenas targets compatíveis: por exemplo, click em elementos clicáveis e fill em campos editáveis.
3. Associar a decisão a um fingerprint, versão ou outro marcador de frescor da página quando a ferramenta permitir.
4. Antes da mutação, verificar se página e target continuam válidos; se ficaram stale, reobservar e decidir de novo.
5. Consumir a decisão uma única vez antes da mutação para que retry não produza double-click/double-submit.
6. Depois da ação, observar novamente e registrar a consequência antes de escolher o próximo passo.
7. Em loops, impor budget de ações/model calls e bloquear repetição quando várias ações seguidas não alteram estado útil.

Texto gerado para preencher um campo deve ficar restrito ao campo observado e ao objetivo atual. A saída textual nunca deve virar selector, código executável ou comando de sistema sem um contrato separado e autorização apropriada.

## Ferramentas e dependências

Para páginas web, usar o navegador controlável disponível e sua API documentada; separar inspeção de DOM, evidência visual e estado de aplicação. Controle de navegador não implica controle de aplicativos nativos ou dispositivos móveis. Usar testes de integração e logs disponíveis no projeto como evidência complementar. Não presumir Reticle, Playwright, Jev, Browser Harness ou acesso interno a rede/state sem instrumentação.

## Integração

- `tdd`: red → green no nível do app real;
- `verify-before-claim`: gate final;
- `web-design-engineer`: comportamento + visual;
- `diagnosing-bugs`: reproduzir a consequência antes de teorizar.

## Referências

Adaptada de reticlehq/reticle, especialmente `verify-ui-change`, `agentic-tdd`, `false-green-tests` e `replay-user-flows`.

Action-space e freshness guards adaptados de [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast), sem depender de Jev ou Browser Harness.

Separação observe/act/extract e isolamento de credenciais refinados a partir de https://github.com/browserbase/stagehand.

Origem local: [runtime-ui-verification.docx](../runtime-ui-verification.docx).
