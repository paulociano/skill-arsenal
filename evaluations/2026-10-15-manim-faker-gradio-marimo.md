# Avaliação: ManimGL, Faker.js, Gradio, marimo

Data: 2026-10-15
Fluxo: arsenal-autopilot, skill-security-review (leitura estática documental).
Fontes:
- https://github.com/3b1b/manim
- https://github.com/faker-js/faker
- https://github.com/gradio-app/gradio
- https://github.com/marimo-team/marimo

## Capability ledger e decisões
| Fonte | Classe | Decisão | Owner |
|---|---|---|---|
| 3b1b/manim (ManimGL) | B/D | KEEP_EXTERNAL_REFERENCE | teach, arquitetura de explicações, composição de vídeo |
| faker-js/faker | A/D | CREATE_NEW (método portátil) | synthetic-test-data-engineering |
| gradio-app/gradio | A/D | CREATE_NEW (com marimo) | python-interactive-prototyping |
| marimo-team/marimo | A/D | ABSORB_METHOD_ONLY (com Gradio) | python-interactive-prototyping |

## Análise
**Manim** é motor Python de animação matemática programática. O repo 3b1b corresponde ao ManimGL (`manimgl`) e não ao Manim Community (`manim`), que difere em APIs e requisitos. Motiva storyboard lógico, encadeamento de transformações e relação causal entre fórmula, gráfico e explicação. Como depende de Python, OpenGL, FFmpeg e possivelmente LaTeX, não faz sentido declarar geração de vídeo disponível apenas por instrução textual. Seu ganho no Arsenal atual é referência de runtime; se houver pedido efetivo de vídeo matemático com esse motor, avaliar ambiente antes de implementar.

**Faker.js** oferece geração de dados sintéticos localizados e coerentes, mas nomes/emails realistas podem coincidir com pessoas reais. O valor incremental está em contrato de schemas, seed e relógio, relações de entidades, distribuições e cenários negativos, indispensáveis em aplicações e testes. Nova skill agnóstica ao gerador. A branch padrão `next` não deve ser confundida com documentação da API estável.

**Gradio** é framework Python para demos de funções e modelos, com widgets e execução web. **marimo** é notebook Python reativo, versionável e executável como script/app. O valor para o Arsenal é um *chooser* orientado à forma do problema e guardrails de estado, contratos e runtime; consolidado em uma única skill, não duas dependências obrigatórias.

## Segurança / portabilidade
Revisão apenas estática dos READMEs e metadados, não scanner completo de dependências ou código. Não houve instalação/execução de ManimGL, Faker, Gradio ou marimo, nem deploy, upload ou publicação de apps. Todos são runtimes externos: nenhuma compatibilidade com o ChatGPT é presumida. Classificação de adoção documental: CAUTION para qualquer instalação/deploy, condicionada a revisão de dependências, versões, permissões, logs, dados sensíveis e supply chain.

Riscos principais:
- ManimGL: dependências de renderização e diferentes variantes/APIs.
- Faker: contatos simulados aparentemente válidos, risco de disparar mensagens/requisições reais e confusão entre dados simulados e evidência.
- Gradio: `share` ou hospedagem pode expor modelos, dados e endpoints; validação de inputs/uploads e concorrência.
- marimo: execução de Python/SQL e acesso a dados; implicações de estado reativo, permissões e deployment.

## Prova de valor
- Nova massa fictícia CRM com 5 mil registros, seed repetível, integridade referencial e zero comunicações externas → synthetic-test-data-engineering.
- Playground Python de modelos versus investigação reativa com SQL/células → python-interactive-prototyping escolhe Gradio ou marimo de acordo com contrato.
- Pedido de vídeo animado por ManimGL → manter referência externa, verificar dependência e necessidade antes de qualquer instalação.
Near-misses: métricas reais não são Faker; produto SaaS completo não é demo Python; diagrama simples não exige ManimGL.

Não alegar que executamos ou testamos as bibliotecas. Alterações documentais devem ser verificadas na branch canônica após publicação.
