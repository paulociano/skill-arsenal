# Interfaces imersivas

Aplicar quando o briefing pede uma experiência expressiva, como narrativa cinematográfica ou portfolio interativo. Para landing pages, `landing-craft` organiza a narrativa; esta referência ajuda a selecionar e limitar os mecanismos visuais. “Premium” sozinho não determina uma lista de efeitos.

## Escolher mecanismos pelo objetivo

| Mecanismo | Quando pode ajudar | Condição para adoção |
|---|---|---|
| Estado de carregamento | Assets essenciais ainda não estão disponíveis | Exibir conteúdo útil cedo; não introduzir atraso teatral, percentual fictício ou bloqueio sem recuperação |
| Hero amplo | Um asset ou mensagem precisa estabelecer contexto | Altura compatível com conteúdo e viewport móvel, CTA acessível e alternativa para asset indisponível |
| Navegação reativa | A página precisa liberar espaço durante leitura | Não ocultar controle focado; navegação acessível por teclado e toque |
| Sequência por scroll | O progresso explica uma história ou transformação | Conteúdo também legível sem a animação, sem aprisionar scroll ou foco |
| Efeito de ponteiro | Feedback espacial agrega à exploração com mouse | Restringir a dispositivo compatível; fornecer feedback equivalente por foco e toque |
| Texto animado | Revelar um título reforça o significado | Preservar nome acessível, leitura e seleção; não expor cada letra isolada ao leitor de tela |
| Textura ou vidro | A superfície reforça a identidade | Conferir contraste e custo de renderização após composição real |

Escolha poucos mecanismos coerentes; nenhum deles é obrigatório. Botões móveis ou magnéticos não podem tornar o alvo difícil de atingir. Cursor customizado não deve eliminar a orientação nativa ou depender de um único tipo de ponteiro.

## Implementação proporcional

- Preserve bibliotecas do projeto e scroll nativo quando suficientes. Não instalar GSAP, Motion, Lenis ou WebGL em conjunto apenas para corresponder ao adjetivo “imersivo”.
- Se uma dependência for necessária, confira versão e documentação oficial antes de escolher pacote/imports. Nomes de pacotes e receitas upstream podem envelhecer.
- Prefira propriedades de animação adequadas ao efeito e meça o resultado. `transform` e `opacity` não garantem desempenho perfeito por si só; filtros, texturas grandes e camadas também têm custo.
- Use `will-change` apenas quando houver benefício identificado, com ciclo de vida limitado.
- Evite trabalho contínuo fora da viewport. Limpe listeners, observadores, timers e animações ao desmontar ou trocar de rota.
- Movimento reduzido deve conservar conteúdo, ordem e ações; não basta desligar a animação e deixar elementos transparentes ou deslocados.
- Fontes especiais e assets devem ter fallback e dimensões reservadas quando aplicável. Não tornar fontes pagas requisito estético.

## Aceitação

Verifique teclado, toque, resize e preferência de movimento reduzido, além da aparência. Inspecione o estado inicial antes dos assets carregarem e após falhas. Para sequências de scroll, confira entrada/saída, links por âncora e retorno à página. Relate métricas somente quando medidas; não prometa performance perfeita ou pontuação universal.

## Origem e alterações

Adaptada de [GitHub awesome-copilot · premium-frontend-ui](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/premium-frontend-ui/SKILL.md), de Utkarsh Patrikar, blob `35922e088cd4f02a4171ebd8534bbb3ec3f9101e`.

Modificação do Arsenal em 2026-09-20: efeitos obrigatórios convertidos em decisões condicionais, retirada a prescrição de scroll hijacking, preloaders, fontes premium e bibliotecas automáticas; acrescentados critérios verificáveis de interação e degradação. Nenhum código ou pacote executável importado. [Licença MIT da origem](licenses/awesome-copilot-MIT.txt).
