---
name: codebase-design
description: Projetar ou refatorar módulos profundos com interfaces pequenas, seams explícitos, alta alavancagem, locality e testabilidade, evitando abstrações rasas e pass-through.
---

# Codebase Design

## Objetivo
Melhorar a arquitetura de software projetando módulos profundos: muita capacidade atrás de uma interface pequena, colocada em um seam claro e testável.

## Vocabulário
- **Módulo**: unidade com interface e implementação.
- **Interface**: tudo que um caller precisa saber para usar o módulo corretamente, incluindo invariantes, erros e restrições.
- **Implementação**: comportamento interno escondido atrás da interface.
- **Depth**: alavancagem obtida por unidade de interface aprendida.
- **Seam**: ponto em que o comportamento pode variar sem editar o consumidor.
- **Adapter**: implementação concreta de uma interface em um seam.
- **Leverage**: capacidade obtida pelos callers por meio de uma interface pequena.
- **Locality**: concentração de mudança, bugs, conhecimento e testes em poucos lugares.

## Workflow
1. Identifique o comportamento que callers realmente precisam.
2. Localize onde a complexidade hoje vaza para múltiplos arquivos, chamadas ou testes.
3. Aplique o teste de deleção: se remover a abstração apenas espalha a complexidade pelos callers, ela provavelmente está ganhando profundidade; se a complexidade simplesmente desaparece, era provável pass-through.
4. Desenhe a menor interface que preserve o comportamento necessário.
5. Coloque detalhes voláteis atrás do seam.
6. Introduza adapters somente quando houver variação concreta ou benefício de teste relevante.
7. Faça os testes atravessarem a mesma interface usada pelos callers.
8. Compare alternativas quando houver mais de uma boa localização de seam.

## Heurísticas
- Prefira poucas operações expressivas a muitas operações finas.
- Aceite dependências em vez de criá-las internamente quando isso melhora testabilidade.
- Retorne resultados quando possível em vez de esconder comportamento em efeitos colaterais.
- Não crie uma seam hipotética sem necessidade real.
- Evite módulos que apenas encaminham chamadas sem concentrar conhecimento.
- Considere hot spots recentes do código antes de refatorar áreas estáveis sem evidência de dor.

## Saída
Entregue:
- módulos e seams relevantes;
- interface proposta;
- complexidade que ficará escondida;
- ganho esperado de locality, leverage e testabilidade;
- riscos e trade-offs da mudança.

## Origem adaptada
Metodologia inspirada em `mattpocock/skills`, especialmente `codebase-design` e `improve-codebase-architecture`, sem dependência de subagentes, Tailwind, Mermaid ou comandos locais específicos.
