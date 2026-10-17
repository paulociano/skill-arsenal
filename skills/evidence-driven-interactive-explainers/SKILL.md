---
name: evidence-driven-interactive-explainers
description: Construir explicações interativas de mecanismos biológicos, físicos ou mecânicos, com estrutura fiel, modelo computável, referências rastreáveis, limites científicos explícitos e QA visual/acessível.
---

# Evidence-driven Interactive Explainers

## Trigger
Quando o usuário pedir uma figura, simulação, mecanismo animado ou explicação interativa de funcionamento biológico, físico, técnico ou mecânico. Não acionar para ilustrações decorativas, dashboards de métricas ou diagramas estáticos simples.

## Objetivo
Fazer a interação explicar uma relação causal verificável, sem usar animação convincente como substituto de evidência.

## Workflow
1. **Escopo e classe do artefato.** Identificar mecanismo, público, formato (HTML/SVG/3D/vídeo), precisão exigida e se é ensino, concepção ou engenharia. Classificar como esquema qualitativo, modelo quantitativo ou simulação validada. Nunca promover um ao outro por estética.
2. **Grounding antes do desenho.** Identificar partes, topologia, relações causais, unidades, dimensões e parâmetros relevantes; levantar fontes confiáveis para medidas e claims. Deixar valores não verificados em branco ou explicitamente hipotéticos.
3. **Estrutura fiel.** Representar os componentes que fazem o mecanismo funcionar, conexões e dependências; em hardware, preferir escala real, juntas e sólidos plausíveis; em biologia, distinguir anatomia literal de metáfora etiquetada. Não inferir validade física ou biomédica só da geometria.
4. **Modelo único e pequeno.** Declarar entrada, estado, equações/regras, hipóteses e domínio válido. Animar movimento e atualizar leituras a partir da mesma função do modelo. Alteração no controle precisa produzir consequência causal, não apenas efeito visual.
5. **Evidência no artefato.** Vincular cada valor factual a fonte, condições e unidade. Separar consenso, hipótese, evidência pré-clínica e simplificações. Distinguir parâmetros ilustrativos de resultados medidos; expor fontes ao lado da figura.
6. **Interação orientada a entendimento.** Priorizar um controle primário, mecanismo visível, leitura legível, exploração de estados e opção de pausar. Modos de corte, explosão e raio X só se aumentarem a compreensão e se a representação técnica suportar.
7. **QA proporcional.** Conferir conservação/dimensões/limites plausíveis quando aplicáveis, consistência entre equação e render, topologia, interseções, teclado, foco, mobile, tema claro/escuro, redução de movimento e captura visual real quando o runtime permitir. Para vídeo, verificar primeiro frame e frames defeituosos.
8. **Entrega honesta.** Identificar o que foi construído e realmente testado. Se faltarem bibliotecas, browser, simulador ou validador, entregar protótipo/roteiro e explicar limites; não alegar validação numérica ou visual ausente.

## Gates de segurança
- Não converter mecanismo biomédico ou farmacológico em dose, prescrição, indicação clínica ou protocolo de uso.
- Não usar parâmetros inventados para alegar desempenho, segurança de máquina, certificação ou conformidade.
- Não executar scripts, installers ou dependências dos projetos-fonte sem revisão e autorização adequadas.
- Para artefatos críticos, exigir verificação externa, especialista e fontes primárias antes de decisão operacional.

## Aceitação
**Should trigger:** "mostre em HTML interativo como um turbofan funciona e como o empuxo muda com o throttle"; "compare os efeitos de dois ligantes num receptor, com fonte e controle". **Near miss:** "faça um pôster bonito de um motor"; "crie gráfico de vendas".

## Proveniência
Metodologia adaptada de:
- https://github.com/AirsupHQ/machine-skill (fidelidade geométrica, solver e legibilidade de mecanismo)
- https://github.com/Garinmckayl/anima (evidência, limites biomédicos, modelos explicativos e acessibilidade)

Não pressupõe Claude Code, kits JS originais, Three.js, navegador de captura, Chrome ou ffmpeg disponíveis no host.
