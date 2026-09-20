---
name: code-review
description: "Revisar mudanças de código e feedback de PR separando conformidade com padrões, fidelidade à spec e impacto real."
---

# code-review

## Objetivo

Revisar mudanças de código separando dois eixos que não devem se contaminar: conformidade com padrões e fidelidade à especificação.

## Quando usar

Revisar mudanças de código e feedback de PR separando conformidade com padrões, fidelidade à spec e impacto real.

## Workflow

1. Ler a spec, o diff e os padrões do repositório.
2. Revisar separadamente os eixos Standards e Spec.
3. Verificar o fluxo afetado e sustentar cada finding com evidência.
4. Aplicar os critérios de simplificação e impacto abaixo; usar a referência de revisão independente apenas quando esse modo contribuir.
5. Entregar findings acionáveis e limites da validação.

## Dois eixos

1. **Standards** — padrões documentados do repositório + smells relevantes.
2. **Spec** — requisitos ausentes, parciais, incorretos ou escopo extra em relação à origem da mudança.

## Princípio

Manter os relatórios separados: código pode obedecer aos padrões e implementar a coisa errada, ou implementar a coisa certa violando os padrões.

## Revisão da implementação

- revisar a experiência/contrato real do usuário e o fluxo completo, não apenas o diff local;
- buscar causa raiz antes de adicionar branches, flags, wrappers ou special cases;
- preferir o sistema coerente mais simples ao menor patch quando a fundação estiver errada;
- remover escopo, abstração e compatibilidade não justificadas;
- isolar legado necessário numa borda removível com condição de aposentadoria;
- repetir passes de simplificação até que uma rodada completa não encontre problema material ou simplificação relevante.

## Antes de criar abstrações

Antes de aceitar nova abstração/código:

1. isso precisa existir?
2. já existe no codebase?
3. stdlib resolve?
4. plataforma nativa resolve?
5. dependência já instalada resolve?
6. só então escrever o mínimo necessário.

Não simplificar segurança, validação em trust boundary, prevenção de perda de dados, acessibilidade ou requisito explícito. Preferir root-cause + remoção de código a wrappers e scaffolding especulativo.

## Valor, custo e impacto

Além de standards e spec, para findings ou mudanças materiais perguntar:

- **Value:** qual problema real resolve, para quem, com que frequência e consequência?
- **Cost:** custo de implementar, verificar, entender e manter no futuro.
- **Impact:** comportamento/módulos afetados, acoplamento criado/removido e restrições futuras.

Usar esse eixo para calibrar severidade e evitar recomendar correções caras para problemas marginais. Julgamentos precisam de evidência da revisão alvo, não apenas preferência de reviewer.

## Referências

[revisao-independente-e-pr](references/revisao-independente-e-pr.md) — Consultar ao organizar revisão independente, devolver findings ou corrigir feedback de PR.

[GitHub · mattpocock/skills · code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review)

Origem local: [code-review.docx](../code-review.docx).
