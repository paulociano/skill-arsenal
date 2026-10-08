---
name: decision-analysis
description: "Estruturar decisões simples ou complexas com respostas tipadas, critérios, incerteza, trade-offs, reversibilidade e sensibilidade sem esconder julgamento humano em uma pontuação arbitrária."
---

# decision-analysis

## Objetivo

Ajudar a estruturar decisões com múltiplas alternativas e critérios, tornando explícitos objetivos, restrições, incerteza, trade-offs e sensibilidade. A skill informa a decisão; não substitui julgamento por uma fórmula opaca.

## Quando usar

- escolher entre alternativas de produto, projeto, fornecedor, ferramenta ou estratégia;
- decisões com critérios conflitantes;
- comparação de opções sob incerteza;
- quando uma matriz simples de prós/contras não é suficiente.

## Escolher a profundidade antes de analisar

Para triagem repetitiva com opções delimitadas e critérios observáveis, usar o [protocolo de decisões tipadas](references/typed-decisions.md). Resolver a pergunta mínima e registrar a evidência, sem criar uma matriz multicritério desnecessária.

Para decisões abertas, critérios conflitantes, alto custo do erro ou conclusão instável, seguir o workflow completo abaixo. A via curta não transforma ambiguidade em certeza nem autoriza ações externas.

## Workflow

1. Definir a decisão em uma frase e o horizonte relevante.
2. Separar:
   - objetivos;
   - critérios;
   - restrições duras;
   - preferências;
   - incertezas.
3. Listar alternativas reais, incluindo status quo quando relevante.
4. Eliminar opções que violam restrições duras.
5. Tornar critérios independentes o suficiente para evitar dupla contagem.
6. Definir direção de preferência e unidade/escala de cada critério.
7. Quando pesos forem úteis, tratá-los como preferências explícitas, não fatos.
8. Comparar alternativas por:
   - trade-offs qualitativos;
   - dominância;
   - cenários;
   - análise multicritério proporcional ao problema.
9. Executar sensibilidade: verificar se pequenas mudanças em pesos/assunções mudam a conclusão.
10. Destacar decisões reversíveis vs irreversíveis e custo do erro.
11. Entregar a estrutura, evidências e pontos de decisão sem fabricar certeza.

## Regras

- Não transformar qualquer decisão em ranking numérico.
- Scores compostos podem ocultar premissas; mostrar componentes.
- Peso não é probabilidade.
- Critério subjetivo continua subjetivo mesmo quando recebe número.
- Quando duas alternativas estiverem próximas e a conclusão for instável, reportar isso.
- Se informação adicional puder mudar materialmente a decisão, identificar seu valor antes de pesquisar tudo.
- Em temas políticos/eleitorais, esta skill não produz ranking, vencedor ou recomendação.

## Integração

structured-output-contract para o contrato técnico e runtime opcional; arsenal-router para seleção de recursos; prioritization-engine, scenario-forecasting, experiment-design, research-and-synthesize, project-complexity-management e to-spec.

## Origem metodológica

Adaptada de métodos MCDA observados em scikit-criteria e PyMCDM, preservando decomposição, pesos e sensibilidade sem tornar um método específico como TOPSIS/AHP uma regra universal.

## Stress test por lentes adversariais (opcional)

Para decisões estratégicas de alto impacto, após estruturar opções e evidências, simular perspectivas com mandatos distintos: finanças/unit economics, cliente, execução, ceticismo/contrarian e até dois especialistas de domínio quando úteis. As lentes são métodos de crítica, **não especialistas reais consultados**. Nunca inventar biografia, experiência ou autoridade factual.

1. Entregar o mesmo briefing factual e constraints a cada lente.
2. Cada lente aponta premissa frágil, maior risco subestimado, alternativa e evidência que poderia mudar a posição.
3. Sintetizar concordâncias, conflitos e critérios decisivos; não contar votos como prova.
4. Quando houver probabilidades, explicitar origem e incerteza. Apostas fictícias e percentuais inventados não são calibração.
5. Fechar com decisão reversível, experimento recomendado ou evidência pendente, preservando julgamento humano.

Near-miss: decisões triviais ou sem alternativas não justificam painel simulado. Provenance metodológica: https://github.com/zapier/wade-skills/tree/main/skills/war-council (absorção do stress test, sem personas com credenciais inventadas).
