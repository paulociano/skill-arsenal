---
name: design-direction
description: "Transformar um briefing visual vago em uma direção de design explícita, específica ao produto e reutilizável antes da implementação."
---

# design-direction

## Objetivo

Resolver a direção visual antes da construção: estabelecer uma tese coerente sobre hierarquia, tipografia, cor, densidade, superfícies, composição, motion e elementos assinatura, sem inventar uma segunda identidade quando já existe sistema de marca.

## Quando usar

- briefing visual aberto ou contraditório;
- produto novo sem direção consolidada;
- redesign que precisa escolher o grau de mudança antes de codar;
- quando referências visuais existem, mas ainda não foram traduzidas em decisões;
- antes de web-design-engineer quando a estética é parte central do pedido.

## Workflow

1. Ler assets, brand guide, screenshots, design system e código existente antes de propor estilo.
2. Classificar o contexto como existing-system, partial-system ou greenfield.
3. Pesquisar referências atuais quando o pedido depende de linguagem contemporânea ou marcas específicas.
4. Extrair de 2–5 referências apenas relações úteis: estrutura, ritmo, type roles, contraste, densidade, motion, assets e elementos assinatura.
5. Escrever uma visual thesis em uma frase.
6. Definir os dials: energia, densidade, variância visual, fidelidade de marca, dependência de assets e intensidade de motion.
7. Declarar decisões concretas de tipografia, cor, grid/spacing, radius/depth, composição, motion e 1–3 signature elements.
8. Registrar o que é observed, derived e proposed.
9. Quando houver escolha real entre direções, mostrar poucas alternativas estruturalmente diferentes; não criar variantes que só trocam cor.
10. Entregar a direção para web-design-engineer, landing-craft ou design-system-governance.

## Saída mínima

- visual thesis;
- público e tarefa principal;
- dials;
- palette logic;
- type roles;
- layout grammar;
- motion stance;
- signature elements;
- anti-patterns específicos do contexto;
- provenance das decisões.

## Regras

- Não reabrir identidade aprovada sem pedido.
- Não impor listas universais de fontes, cores ou estilos proibidos.
- Referência visual é evidência, não licença para copiar marca.
- Se a mesma direção servir a qualquer produto após trocar o nome, ela ainda está genérica.
- Perguntas só são necessárias quando uma ambiguidade muda materialmente a direção; caso contrário, faça uma proposta explícita e verificável.

## Integração

Usar antes de web-design-engineer ou landing-craft quando a direção não estiver resolvida. Usar design-system-extraction antes quando um sistema já existe e precisa ser documentado.

## Origem metodológica

Síntese adaptada de dawitlabs/ui-skills, travisjneuman/.claude, Firzus/agent-skills, nolly-studio/agent-skills e AgentsORG/DESIGN, sem dependências de Claude Code, slash commands ou instaladores.
