---
name: decision-analysis
description: "Estruturar decisões complexas com alternativas, critérios, incerteza, trade-offs, reversibilidade e sensibilidade sem esconder julgamento humano em uma pontuação arbitrária."
---

# decision-analysis

## Objetivo

Ajudar a estruturar decisões com múltiplas alternativas e critérios, tornando explícitos objetivos, restrições, incerteza, trade-offs e sensibilidade. A skill informa a decisão; não substitui julgamento por uma fórmula opaca.

## Quando usar

- escolher entre alternativas de produto, projeto, fornecedor, ferramenta ou estratégia;
- decisões com critérios conflitantes;
- comparação de opções sob incerteza;
- quando uma matriz simples de prós/contras não é suficiente.

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

prioritization-engine, scenario-forecasting, experiment-design, research-and-synthesize, project-complexity-management e to-spec.

## Origem metodológica

Adaptada de métodos MCDA observados em scikit-criteria e PyMCDM, preservando decomposição, pesos e sensibilidade sem tornar um método específico como TOPSIS/AHP uma regra universal.
