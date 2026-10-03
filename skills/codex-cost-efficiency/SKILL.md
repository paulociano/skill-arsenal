---
name: codex-cost-efficiency
description: Reduzir tokens e gasto em tarefas de desenvolvimento no Codex por medição, leitura seletiva, controle de saída e comparação de tarefas concluídas. Usar quando o usuário pedir economia de contexto, quota ou custo em um projeto Codex.
---

# Eficiência de custo no Codex

## Objetivo

Diminuir o custo por tarefa concluída sem perder correção, evidência necessária ou validação.

## Procedimento

1. Identificar o modo de cobrança (assinatura, API ou outro), o limite relevante e a métrica disponível. Distinguir tokens, quota e valor faturado; não converter um no outro sem a tarifa e o uso reais.
2. Escolher tarefas representativas e registrar baseline: resultado aceito, modelo/configuração, tokens de entrada e saída quando expostos, tempo, tentativas, chamadas de ferramenta e custo cobrado quando disponível.
3. Localizar desperdício dominante: instruções sempre carregadas, histórico antigo, leitura de arquivos, saída de comandos, ferramentas/MCP expostos, repetições ou roteamento de modelo. Não presumir que todos os itens são controláveis na superfície atual.
4. Fazer a menor mudança plausível e medir de novo com tarefas equivalentes. Priorizar:
   - delimitar objetivo e critérios de aceite;
   - procurar caminhos e ocorrências antes de abrir arquivos inteiros; ler trechos e ampliar quando a evidência exigir;
   - resumir logs extensos com linhas de erro e caminho para o original; manter falhas raras e números exatos recuperáveis;
   - retirar instruções duplicadas ou globais que não ajudam a tarefa; carregar referências sob demanda;
   - iniciar uma sessão nova ou preparar `handoff` quando o histórico deixou de ser relevante;
   - agrupar reconnaissance e probes de ambiente independentes em uma única passagem quando isso reduz round-trips sem esconder falhas;
   - para leitura exploratória, começar por trechos pequenos e expandir sob demanda; nunca truncar silenciosamente dados que serão transformados;
   - tratar polling como custo: esperar em intervalos proporcionais ao job em vez de consultar loops longos agressivamente;
   - usar modelo mais leve apenas para trabalho delimitado e verificável, se a interface permitir escolha real;
   - fundir edit/write + validação previsível em um único passo quando isso reduzir round-trips sem esconder o resultado da validação;
   - transformar observações grandes e repetidas em handles estáveis com recall paginado/exato, preservando o original;
   - resumir logs extensos em receipts somente se cada quote/line retida continuar verificável contra a fonte arquivada;
   - compactar contexto preferencialmente após subtarefas concluídas, condicionando a pressão de janela e o custo esperado, nunca no meio de uma evidência ainda necessária.
5. Quando houver delegação, separar:
   - whole-task usage observado;
   - delegated-only usage;
   - reviewer usage;
   - cobertura parcial/ausente;
   - requested model/effort de runtime-confirmed values.
   Uma comparação de preço com o mesmo número de tokens é **reprecificação**, não prova de economia real, porque outro modelo pode consumir outro número de tokens, retries ou tempo.
6. Comparar custo **por tarefa aceita**, qualidade, retrabalho e latência. Reverter uma economia aparente que aumente falhas ou iterações. Conservar testes obrigatórios e verificação proporcional ao risco.

## Jev e outros classificadores

Usar um decision engine tipado somente para triagem repetitiva com opções explícitas (por exemplo, ordenar muitos caminhos ou classificar várias falhas) e quando a integração real estiver disponível. Medir custo do serviço externo **mais** custo do Codex, acertos, itens omitidos, revisão manual e retries. Probabilidade não garante acerto; casos incertos voltam ao agente. Uma skill que recomenda modelo não muda o modelo da conversa por si só. Não enviar código, logs ou dados privados a outro provedor sem o controle adequado.

## Limites

- Não declarar porcentagem de economia a partir de bytes filtrados, de uma chamada isolada ou de benchmarks do autor.
- Não assumir comandos, variáveis de ambiente, hooks ou preços de terceiros como controles oficiais do Codex. Confirmar na documentação vigente antes de recomendar configuração concreta.
- Não instalar wrappers, MCPs ou skills de terceiros por padrão. Revisar cadeia de instalação, permissões, dados enviados e credenciais antes de integrar.
- Para avaliação instrumental de compressão, usar `llm-observability-evaluation`; para continuidade entre sessões, usar `handoff`.

## Fontes da adaptação

- [codex-token-optimizer](https://github.com/zhangyiling108-code/codex-token-optimizer) e [token-efficient-workflow](https://github.com/luziyezz/codex-skills/tree/main/token-efficient-workflow): escopo, leitura e saída seletivos.
- [Jev Skills](https://github.com/n23eos/jev-skills) e [jev-code](https://github.com/FrancoisChastel/jev-code): limites de decisões tipadas e integração opcional.
- NVlabs/SoL-Pi: action fusion, observation handles, evidence-preserving reduction e compaction em pontos de conclusão, absorvidos como metodologia sem depender do runtime Pi.
- DannyMac180/astra-advisor: cost receipts com cobertura explícita e distinção entre same-token repricing e economia real; model/effort snapshots específicos não são tratados como capacidades permanentes.
