# Revisao especializada

## Escrita técnica

Para documentação técnica, papers, READMEs, runbooks e textos analíticos, aplicar adicionalmente:

- não assumir conhecimento tácito do leitor;
- preferir termos concretos e específicos;
- remover palavras desnecessárias e jargão evitável;
- manter termos e abreviações consistentes;
- posicionar informação nova/importante com clareza;
- apoiar alegações factuais com citação ou evidência concreta quando a tarefa exigir;
- preservar a força epistemológica da fonte, sem superestimar ou suavizar indevidamente;
- tratar regras estilísticas como heurísticas com escape hatch: clareza e fidelidade vêm antes da obediência mecânica.

## Revisão de padrões genéricos

Em revisão de texto humano:

- preservar voz, vocabulário, cadência, humor, incerteza, imperfeições úteis e nível de polimento;
- fazer a **menor edição eficaz** em vez de reescrever tudo para consistência;
- usar o **portability test**: se uma frase genérica poderia ser movida intacta para outra pessoa/empresa/produto, inspecionar se é filler ou se precisa de fato/mecanismo específico;
- detectar padrões concretos como throat-clearing, faux-insight setups, binary contrasts, importance puffery, weasel attribution, synonym cycling, robotic rhythm, fake-profound endings e recap redundante;
- em modo Audit/Detect, citar o padrão e o trecho sem reescrever quando o usuário pediu apenas diagnóstico;
- nunca inferir autoria por IA a partir desses padrões. O que pode ser observado é o padrão textual, não quem escreveu;
- não transformar listas de palavras em proibições mecânicas. Contexto e voz vencem watchlists.

## Lint editorial opcional para inglês

Para copy em inglês, quando houver risco de prosa genérica ou quando o usuário quiser um gate repetível:

- usar um linter/pattern check como **sinal objetivo adicional**, nunca como juiz absoluto de qualidade;
- separar grupos de patterns: vocabulário genérico, construções repetitivas, cadência/pontuação, rhythm e proof claims;
- input vazio ou pipeline quebrado deve falhar, não passar silenciosamente;
- após qualquer rewrite automático, reexecutar o mesmo gate para detectar regressão;
- uma regra alterada precisa de regression tests próprios;
- claims numéricos/social proof devem ser tratados com alta sensibilidade: sem evidência, marcar como pendência em vez de inventar;
- um score perfeito no linter não prova boa copy. Especificidade, adequação ao leitor e verdade factual continuam sendo critérios superiores.

### Reviewer independente
Quando houver um revisor realmente independente, ele pode ser usado como segunda leitura para encontrar padrões que o autor não percebe. Diversidade de modelo/família é uma heurística de cobertura, não uma garantia de qualidade. Não exigir outro provider quando ele não estiver conectado e não enviar texto sensível a serviço externo sem autorização.

### Limites
O catálogo SlopMonster é explicitamente inglês. Não aplicar scores/listas inglesas a português ou outras línguas como se fossem válidos.
