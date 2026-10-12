---
name: generative-ui-engineering
description: "Projetar e validar interfaces geradas por modelos como saída estruturada ou sandboxed runtime, com component allowlists, streaming, bridges restritas, fallback, acessibilidade e limites claros entre UI gerada e capacidades reais."
---

# Generative UI Engineering

## Objetivo

Projetar experiências em que um modelo produz interface, não apenas texto, sem transformar HTML/JS gerado em uma superfície irrestrita de execução.

## Quando usar

Use quando:
- a resposta do agente precisa virar componentes, widgets, dashboards, diagramas ou controles interativos;
- o modelo deve escolher entre componentes previamente autorizados;
- a UI precisa aparecer progressivamente durante streaming;
- HTML/SVG/Canvas/Three.js gerado precisa rodar isolado;
- produto e agente compartilham estado ou ações por uma bridge explícita.

Para uma UI convencional construída por humanos/agente de código, use `web-design-engineer`.
Para diagramas interativos com topologia já conhecida, use `interactive-system-diagram`.

## Roteamento orientado à tarefa

Antes de gerar uma UI, escolha a menor representação que resolve a intenção:
- **Entender:** texto para resposta direta; explicação visual ou stepper quando uma relação ou variável realmente melhorar a compreensão.
- **Comparar:** tabela/componente nativo para critérios simples; gráfico ou controles de pesos quando houver decisão multivariável.
- **Criar uma ferramenta:** calculadora, simulador ou planejador com entradas validadas, resultados verificáveis, unidades e reset.

Não converter toda resposta em dashboard. Distinguir dados reais, dados do usuário e exemplos ilustrativos. Um renderer não fornece evidência nem acesso a dados ao vivo.

## Dois modos

### 1. Component grammar

Preferir quando o produto possui biblioteca de componentes confiável.

1. definir componentes e props permitidos;
2. derivar um schema/linguagem compacta;
3. instruir o modelo usando apenas esse vocabulário;
4. validar o stream antes de renderizar;
5. desconhecido ou inválido vira erro/fallback, não execução improvisada.

Vantagens:
- superfície menor;
- acessibilidade e design system reutilizáveis;
- output mais barato e verificável;
- ações podem ser ligadas a contratos explícitos.

### 2. Sandboxed document

Use somente quando o valor depende de liberdade visual real, como:
- explainer interativo;
- simulação;
- SVG complexo;
- Canvas/WebGL;
- protótipo visual não coberto pelo component set.

Nesse modo:
- isolar em iframe/sandbox equivalente;
- não conceder acesso direto ao DOM host, cookies, storage, filesystem ou credenciais;
- comunicação com host ocorre por bridge allowlisted e validada;
- links, prompts e ações externas passam por handlers do host;
- código gerado não recebe capacidades apenas porque consegue descrevê-las.

## Workflow

1. **Intent contract**
   - o que a UI precisa comunicar ou permitir;
   - quais ações reais existem;
   - quais dados são confiáveis;
   - o que deve continuar possível em fallback textual/estático.

2. **Choose representation**
   - component grammar por padrão;
   - sandbox livre somente quando o ganho visual/interativo justificar risco e custo.

3. **Capability boundary**
   - separar render de ação;
   - listar funções que a UI pode pedir ao host;
   - validar argumentos com schema;
   - manter autorização no host, nunca no código gerado.

4. **Streaming**
   - definir unidade incremental parseável;
   - preservar estado já válido;
   - evitar reexecutar efeitos colaterais em cada chunk;
   - somente ativar JS final quando o documento/contrato estiver completo quando necessário.

5. **State & follow-ups**
   - filtros, sliders, cálculos e ordenação simples devem operar localmente, sem chamar o agente a cada movimento;
   - follow-up ao agente somente por ação explícita do usuário, incluindo seleções atuais validadas;
   - outputs anteriores são snapshots independentes até que um contrato de estado/patch cross-call seja realmente implementado;
   - não presumir persistência de sessão, memória compartilhada nem sincronização do estado de iframe com o agente.

6. **Design system**
   - componentes permitidos carregam tokens, responsividade, foco e reduced motion;
   - UI gerada não redefine silenciosamente identidade global;
   - temas precisam de contraste verificável.

7. **Interaction**
   - ações essenciais têm label e estado;
   - loading, success, failure e retry são distinguíveis;
   - controles gerados não fingem capacidades inexistentes.

8. **Security**
   - sanitize/parse antes de render;
   - sandbox sem permissões desnecessárias;
   - scripts/imports/network precisam de política explícita;
   - segredo nunca é interpolado no documento gerado;
   - conteúdo remoto e mensagens da UI são dados não confiáveis.

9. **Verify**
   - schema/parser;
   - render desktop/mobile;
   - keyboard/focus;
   - reduced motion;
   - bridge calls válidas e inválidas;
   - fallback quando stream quebra;
   - ausência de capability escalation.

## Output contract

Registrar:
- modo escolhido;
- component set ou sandbox permissions;
- schema/grammar;
- bridge disponível;
- fallback;
- verificações executadas;
- capacidades deliberadamente negadas.

## Regras

- UI gerada não é autorização.
- Renderizar um botão não cria a ação que ele representa.
- Structured generation é preferível quando resolve o problema.
- Raw HTML/JS é exceção, não default.
- Uma resposta visual bonita sem contrato de ação pode ser apenas uma ilustração.
- Não confundir component library com prompt library: o runtime deve validar o que o modelo produz.

## Integração

Combina com:
- `structured-output-contract`;
- `web-design-engineer`;
- `runtime-ui-verification`;
- `creative-web-effects`;
- `interaction-polish`;
- `secure-code-privacy-review`.

## Implementação de referência opcional

O [CopilotKit/OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) mostra um exemplo concreto em Next.js/React, CopilotKit/AG-UI, FastAPI/LangGraph e Websandbox. Seu `generateSandboxedUi` usa campos ordenados (`initialHeight`, `placeholderMessages`, `css`, `html`, `jsFunctions`, `jsExpressions`) e uma bridge própria para `sendPrompt` e `openLink`. **Esse contrato é específico daquele runtime**, não uma API universal nem uma ferramenta automaticamente disponível no ChatGPT. O projeto demanda infraestrutura, dependências e credenciais de provedores; use seus padrões conceituais aqui, não comandos ou integrações fictícias.

Para execução independente, auditar separadamente isolamento de iframe, CSP/rede/imports, validação da bridge, segredos, logs/tracing, versões das dependências, smoke test com provedores reais e durabilidade do checkpoint. O exemplo documenta checkpoint em memória, inadequado por si só para memória compartilhada persistente em produção.

## Provenance

Consolidada principalmente de [thesysdev/openui](https://github.com/thesysdev/openui), [CopilotKit/OpenGenerativeUI](https://github.com/CopilotKit/OpenGenerativeUI) [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) e [CopilotKit/OpenIntelligentUI](https://github.com/CopilotKit/OpenIntelligentUI) (README, architecture, master-playbook e advanced-visualization consultados em 2026-10-11). Preserva component grammars, streaming render, sandboxed documents e host bridges, sem exigir OpenUI Lang, AG-UI, CopilotKit, LangChain ou MCP.
