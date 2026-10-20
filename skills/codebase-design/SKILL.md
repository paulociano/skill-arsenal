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

## Composição de interfaces React (Vercel, 2026-10-19)

Quando a API de um componente React acumular props booleanas e combinações inválidas, avaliar uma refatoração para variantes explícitas e compound components. O critério é reduzir o número de estados implícitos e a complexidade que vaza para callers, não eliminar booleanos sempre.

- Definir primeiro estados permitidos, slots, ownership do estado e contrato acessível.
- Usar compound components/contexto quando subcomponentes realmente compartilham contrato e ciclo de vida; não criar provider para componente trivial.
- Isolar provider/interface de estado e ações para que consumidores não dependam dos detalhes da implementação, quando houver valor concreto de testabilidade ou reutilização.
- Preferir children/composição ou variantes explícitas quando render props ou muitos switches escondem o comportamento; preservar ergonomia de tipagem e depuração.
- Validar versão React antes de recomendar APIs 19+ e migração de `forwardRef`/contexto; não tratar heurística de versão futura como obrigação universal.
- Testar combinações válidas, accessibility names/roles, rerenders e regressões dos consumers antes de declarar melhoria.

**Fonte:** https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns . Owner é arquitetura de código; não criar skill paralela específica de composição.

## Tipos de props React aderentes aos callers reais (HumanLayer, 2026-10)

Ao refatorar componentes React com props opcionais excessivas, estados artificiais e callbacks inertes:

1. Mapear **call sites reais de produção** e consumidores de APIs públicas; separar rotas/componentes efetivos de stories, fixtures e mocks. Verificar usos dinâmicos e consumidores externos antes de concluir que uma prop é desnecessária.
2. Classificar props pelo contrato: obrigatória nos estados válidos de produção; opcional quando ausência é legítima; removível apenas quando compatibilidade permitir. **Nullable não é sinônimo de optional.**
3. Se uma ação sempre é exibida, evitar callback opcional que deixe a affordance inerte. Restringir uniões para impedir estados impossíveis sem inventar obrigatoriedade em componentes intencionalmente reutilizáveis.
4. Fazer stories, mocks e testes respeitarem o contrato em vez de relaxar a API para facilitar exemplos. Usar builders/fixtures quando necessário.
5. Atualizar filhos e variantes compartilhadas; executar typecheck no pacote e **nos consumidores reais**, revisar compatibilidade pública e testar comportamento/acessibilidade. Não eliminar fallbacks de estados legítimos.

**Critério:** um tipo mais estrito deve representar melhor o comportamento suportado, não apenas diminuir a quantidade de parâmetros opcionais.

**Origem adaptada:** [HumanLayer / narrow-react-prop-types](https://github.com/humanlayer/skills/blob/main/plugins/narrow-react-prop-types/skills/narrow-react-prop-types/SKILL.md). Método incorporado sem instalar CI, alterar frameworks ou assumir Bun/Storybook.
