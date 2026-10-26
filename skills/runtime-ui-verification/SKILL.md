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
- quando screenshot for a evidência, registrar viewport, escala/DPR, color scheme, alvo/selector e condição de espera suficientes para tornar a captura reproduzível; não tratar uma imagem sem metadata de captura como prova determinística;
- network/state quando consequência funcional importar;
- hybrid para fluxos onde visual e estado precisam concordar.

Permissões de page context devem ser task-scoped. History, tab sets, screenshots ou microphone não entram como contexto “por precaução”.

## Component state coverage

Quando a mudança afeta componente reutilizável ou design system, verificar estados relevantes além do happy path:
- default;
- loading;
- empty;
- error;
- disabled/read-only;
- overflow/long content;
- narrow/wide viewport;
- permission/role states quando existirem;
- focus/keyboard/reduced-motion quando material.

Ferramentas de component workshop podem ajudar, mas o contrato é cobertura de estados, não Storybook em si.

## Visual baseline governance

Visual regression é útil quando a aparência é parte do contrato:
1. fixar viewport, DPR, font/assets e estado;
2. capturar referência aprovada;
3. comparar candidate;
4. revisar diferenças;
5. atualizar baseline somente quando a mudança é esperada e aprovada.

Nunca atualizar baseline apenas para tornar o teste verde. Mudança observada não é sinônimo de mudança desejada.

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
8. Para ações com efeito material, declarar postcondition antes de executar e retornar expected, actual e evidence; mensagem de sucesso/toast não substitui a mudança de estado esperada.
9. Se um workflow verificado for reutilizado, cada replay deve revalidar suas postconditions e usar recovery limitado; batch success é reconciliado contra estado final, não contra número de tentativas.

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

Component-state coverage e governança de visual baselines foram reforçadas a partir de Storybook, BackstopJS e ferramentas de visual regression, sem exigir qualquer runner específico.

Origem local: [runtime-ui-verification.docx](../runtime-ui-verification.docx).

## Matriz responsiva sincronizada (Responsively)

Quando a mudança depender de breakpoints, criar uma **matriz de casos com pelo menos um viewport estreito, um intermediário e um largo**, acrescida de devices específicos do produto quando necessário. Para cada rota e fluxo crítico: repetir as mesmas ações e verificar navegação, entrada de texto, scroll, overlay, foco, touch, conteúdo cortado, containers com overflow e estados carregando/erro. Se o navegador suportar, executar a ação sincronizada em múltiplos viewports; caso contrário, reproduzir sequencialmente com dados/condições equivalentes. Capturas devem identificar device, viewport, zoom, estado, URL e passo. Uma captura bonita em desktop não certifica a versão mobile; cada dispositivo recebe PASS/FAIL/UNKNOWN e uma regressão descoberta volta para o mesmo caso após correção. O aplicativo Responsively e seu MCP são **ferramentas locais opcionais**, não recursos automaticamente disponíveis no ChatGPT. Fonte: https://github.com/responsively-org/responsively-app (2026-10-17).

## Comparação visual com referência aprovada e evidência local

Quando screenshots forem critério de aceite:
1. Registrar a **referência aprovada** como alvo, distinguindo-a de um baseline histórico que pode estar errado.
2. Fixar viewport, DPR, tema, rota, dados, estado, fontes, assets, timestamp/câmera quando relevantes. Capturas incomparáveis não permitem score de regressão.
3. Comparar primeiro landmarks locais: recorte, texto, bordas, sombras, vazamento de efeitos, detalhes nas quatro direções e componentes adjacentes.
4. Usar diffs de pixels, MAE/RMSE, heatmaps de bordas ou densidade somente como telemetria para localizar diferenças. Um score melhor não prova que o design está correto; imagens vazias podem gerar métricas enganosas.
5. Classificar cada divergência como candidato melhor, baseline melhor, ambos incorretos ou evidência insuficiente; não aceitar apenas por semelhança global.
6. Nunca ocultar detalhes, trocar crop ou atualizar a referência para forçar um teste verde. Documentar divergências aprovadas pelo usuário.
7. Repetir inspeção visual após a correção, combinando com verificações de interação, rede e estado quando aplicáveis.

**Origem (A/B, adaptado):** https://github.com/dzhng/skills/blob/main/skills/visual/compare-screenshots/SKILL.md. Não pressupõe subagentes nem executa pacotes `pixelmatch` de terceiros.

## Laboratórios temporários de componentes (jakubkrehel/skills, 2026-10-26)

Ao examinar um componente isolado, escolher um dos dois protocolos:

**State-machine:** ler branches e hooks reais; enumerar loading, empty, error, populated, disabled e permissions apenas quando alcançáveis pelo código. Criar rota temporária que importe o componente real e injete fixtures plausíveis no ponto de entrada dos dados, sem produção. Permitir trocar estados por seletor sem timers artificiais. Revalidar todos após cada alteração. Estados esperados mas ausentes são lacunas, não estados inventados.

**Break:** ler props, slots e containers para escolher apenas eixos aplicáveis, como conteúdo vazio, strings longas e inquebráveis, listas extensas, tradução, largura reduzida e estados. Renderizar cada caso rotulado na mesma página temporária, usando componente, providers e tokens originais. Registrar somente falhas observadas, com viewport, condição e evidência; nunca tratar previsão como resultado.

Não usar credenciais, dados ou serviços de produção nas fixtures. Sem navegador ou execução, classificar como UNKNOWN e fornecer procedimento de reprodução, não alegar que viu o resultado. Evitar dependência obrigatória de Storybook, Playwright e Claude. Quando corrigir, repetir o cenário idêntico. Manter a rota enquanto fizer parte de um relatório visual solicitado e removê-la, com fixtures e imports, quando for concluída a exploração e solicitada limpeza.

Fonte: https://github.com/jakubkrehel/skills/tree/main/skills/break e https://github.com/jakubkrehel/skills/tree/main/skills/state-machine .
