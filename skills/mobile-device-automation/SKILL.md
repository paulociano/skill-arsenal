---
name: mobile-device-automation
description: "Executar e verificar tarefas em dispositivos móveis somente com controle real disponível, por ações pequenas e observação de estado."
---

# mobile-device-automation

## Objetivo

Controlar e verificar tarefas em um dispositivo móvel real ou virtual quando houver uma ferramenta de automação compatível, usando observação barata, ações pequenas, verificação explícita e consentimento para efeitos externos.

## Quando usar

Executar e verificar tarefas em dispositivos móveis somente com controle real disponível, por ações pequenas e observação de estado.

## Princípio central

Em automação mobile, um tap que não gera erro pode ser um no-op silencioso. **Nomeie o que deve mudar antes de agir e verifique depois.**

## Workflow

1. **Observe** — preferir tree/OCR/semântica barata quando disponível; screenshot quando a decisão for visual.
2. **Expect** — declarar qual mudança observável provará sucesso.
3. **Act** — fazer uma ação pequena.
4. **Verify** — checar exatamente a mudança esperada.
5. **Adapt** — se falhar, isolar a ação, formular uma hipótese e testá-la.
6. **Batch** — só agrupar sequências já observadas funcionando; manter um check barato no final.
7. **Persist** — guardar helpers/checks reutilizáveis quando o ambiente permitir.

## Hierarquia de observação

- accessibility tree / labels / OCR estruturado;
- checks específicos de app/text/state disponíveis;
- screenshot/visão para ícones, imagens e layout;
- coordenadas brutas apenas como escape hatch, recalculadas quando a janela/tela puder mover.

## Regras de segurança e consentimento

Antes de ações externas ou difíceis de reverter, verificar se a autorização vigente cobre a ação; pedir aprovação apenas quando faltar. Exemplos:

- enviar mensagem;
- publicar;
- comprar/pagar;
- excluir conteúdo;
- alterar configuração relevante;
- conceder permissão sensível.

Conexão, desbloqueio, pairing, PIN, biometria e confirmações físicas pertencem ao usuário. Nunca tentar adivinhar ou digitar PIN/senha do dispositivo sem autorização explícita e suporte seguro do ambiente.

## Regras operacionais

- não retry-loop quando a conexão depende de ação física do usuário;
- depois de falha silenciosa, verificar foco/estado antes de inventar outra teoria;
- não reutilizar coordenadas antigas quando bounds podem mudar;
- preferir seleção por texto/semântica a posições fixas;
- batch não verificado é pior que uma sequência lenta: perde o ponto exato da falha;
- quando uma tela não oferece DOM/estado interno, o próprio conteúdo observado é o oracle.

## Ferramentas e dependências

Neste ambiente, o controle exposto é de navegador; as APIs de aplicativos nativos estão desabilitadas e não há controle móvel confirmado. Só executar ações no dispositivo se um harness real for disponibilizado e verificado. Caso contrário, entregar plano ou teste executável pelo usuário, sem alegar taps ou verificações realizadas.

## Integração

- `verify-before-claim` para o claim final;
- `loop-engineering` para polling/esperas limitadas;
- `runtime-ui-verification` quando a tarefa for validar um app mobile em execução.

## Referências

Adaptada de ShawnPana/phone-harness.

Origem local: [mobile-device-automation.docx](../mobile-device-automation.docx).
