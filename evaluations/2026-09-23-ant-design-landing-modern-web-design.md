# Avaliação: Ant Design Landing + tópico modern-web-design

Data: 2026-09-23. Método: `evaluate-and-import-skill` + `skill-security-review`.

Fontes avaliadas:

- https://github.com/ant-design/ant-design-landing
- https://github.com/topics/modern-web-design?l=css

## Decisão

**Nenhuma nova skill, stack ou atualização de owner canônico.**

O valor das duas fontes é principalmente como referência visual e de composição. Os padrões úteis já estão cobertos por `web-design-engineer`, `landing-craft`, `design-system-governance`, `gsap-animation` e `ui-ux-catalog`.

## 1. Ant Design Landing

Revisão observada: `54f4360f0df75dd53e2febcd90b1b095801efb41` (2022-05-24).

### O que faz de verdade

O projeto fornece:

- templates de landing page;
- módulos configuráveis;
- editor visual;
- layouts responsivos;
- integração histórica com Ant Motion;
- scaffolds/exemplos para ecossistema Ant Design/Umi/DVA.

A metodologia implícita é modular: compor uma landing a partir de blocos reutilizáveis, com responsividade e motion definidos dentro do sistema.

### Comparação com o Arsenal

Esse valor já está coberto:

- `landing-craft`: storyboard, ritmo, assets, clímax visual, CTA e responsividade;
- `web-design-engineer`: estrutura antes do tema, fingerprint estrutural, motion com propósito, QA de interface;
- `design-system-governance`: contratos, tokens, componentes e autoridade do sistema;
- `gsap-animation`: implementação especializada quando motion complexo é realmente necessário.

O Ant Design Landing não acrescenta hoje um processo de decisão mais forte do que os owners existentes.

### Limitação temporal

O último commit observado é de 2022. Portanto:

- padrões visuais podem continuar úteis como referência histórica;
- dependências, scaffolds e decisões técnicas não devem ser tratadas como stack moderna sem nova validação;
- não congelar Umi/DVA/Ant Motion como dependência do Arsenal.

**Classificação:** B/D — boa referência de composição modular, produto técnico datado.

**Decisão:** não importar nem alterar `landing-craft`.

## 2. Tópico GitHub: modern-web-design, linguagem CSS

O tópico foi consultado via busca GitHub `topic:modern-web-design language:css`.

A amostra retornou projetos como:

- `anuswarrrao/freelink-bio`;
- `developer-junaid/Glass-Website-CSS`;
- `owais-khan-zai/Rejouice-Web-Project`;
- `dangvannhang/modern-responsive-demo-web`;
- `amjustankush/gpt3modern`;
- outros showcases e clones de landing pages.

### Padrões observados

Nos exemplos revisados aparecem:

- design responsivo;
- CSS variables e media queries;
- glassmorphism e superfícies translúcidas;
- dark/light mode;
- scroll animations;
- GSAP;
- Lenis/smooth scrolling;
- sliders;
- microinterações;
- PWA/offline;
- icon systems;
- portfolios e clones de sites de referência.

### Valor metodológico

Esses padrões são **técnicas e estilos**, não um workflow robusto de design.

O Arsenal já evita exatamente o erro de transformar tendência em regra universal:

- `web-design-engineer` exige contexto, marca, estrutura, produto e finalidade antes da estética;
- `landing-craft` organiza a narrativa da página;
- `gsap-animation` trata motion quando ele tem função real;
- `ui-ux-catalog` pode fornecer referências de paleta, tipografia e padrões quando isso agrega valor;
- `runtime-ui-verification` cobre verificação no app em execução.

Glassmorphism, smooth scrolling, gradients, cards ou animação de entrada não devem virar presets canônicos apenas porque aparecem em vários repositórios.

### Qualidade da fonte

O tópico é útil para **discovery visual**, mas mistura:

- projetos recentes e antigos;
- demos educacionais;
- clones;
- portfolios pessoais;
- projetos com README mínimo;
- implementações cuja qualidade visual não implica qualidade de acessibilidade, performance ou arquitetura.

Por isso, o tópico não deve ser usado como autoridade nem benchmark automático de “design moderno”.

**Classificação:** B como radar de referências; C quando tratado como metodologia.

## Segurança e execução

A revisão foi read-only.

Não foram executados:

- builds;
- npm installs;
- scripts;
- demos;
- dependências externas;
- bibliotecas de animação.

Nenhum projeto do tópico foi adotado como dependência.

## Resultado para o Arsenal

- nenhuma nova skill;
- nenhuma nova stack;
- nenhuma alteração no `ARSENAL INDEX.md`;
- nenhuma alteração em `web-design-engineer` ou `landing-craft`;
- Ant Design Landing registrado como referência histórica de composição modular;
- tópico `modern-web-design` registrado como fonte de descoberta visual, não como owner de metodologia.

A regra operacional permanece: referências visuais servem para ampliar o vocabulário; decisões canônicas devem continuar ancoradas no produto, na marca, no contexto e na verificação em runtime.
