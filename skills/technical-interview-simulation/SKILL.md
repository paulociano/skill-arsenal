---
name: technical-interview-simulation
description: "Simular entrevistas técnicas de programação, estruturas de dados e system design com perguntas progressivas, testes executáveis quando disponíveis e avaliação baseada em evidências."
---

# Technical Interview Simulation

## Objetivo

Simular rodadas técnicas de contratação sem confundir treino e avaliação com dados secretos reais do processo seletivo. Adaptada de [nishant-Tiwari24/cracked](https://github.com/nishant-Tiwari24/cracked), sobretudo `mock-interview`, com instrumentos nativos de chat, leitura de arquivos e execução de código disponíveis neste ambiente, sem instalar o catálogo inteiro.

## Quando usar

- O usuário quer treinar para entrevista técnica, DSA/LeetCode, coding assessment ou discussão de arquitetura.
- Precisa de avaliação prática, exemplos adversariais, contraprovas e plano de melhoria.

Não acionar para entrevista de descoberta de clientes, entrevistas de contratação conduzidas pelo empregador ou avaliação genérica de currículos.

## Contrato da sessão

1. Usar idioma, senioridade, empresa, tema, duração e modalidade já informados. Defaults quando faltarem: uma questão intermediária, 45 minutos, modo texto, simulação genérica.
2. Não prometer sessão cronometrada de forma autônoma: o relógio e feedback só são verificados quando o usuário interage. Nunca alegar observação contínua de silêncio ou código não acessado.
3. Se houver empresa-alvo, pesquisar fontes públicas recentes para calibrar estilo, **sem** tratar relatos de candidatos como perguntas oficiais, inevitáveis ou vazadas.
4. Informar previamente se testes de código poderão ser executados. Sem runtime ou acesso a arquivo, limitar avaliação a revisão e dry-run manual.
5. Não coletar dados sensíveis de candidatura nem criar perfil persistente sem pedido do usuário.

## Entrevista DSA

1. Escolher problema com solução de referência conhecida e edge cases planejados; adaptar dificuldade ao nível e evitar repetição quando histórico fornecido permitir.
2. Apresentar enunciado e exemplo inicial, incentivando perguntas de clarificação sobre restrições e casos extremos.
3. Solicitar abordagem e complexidade temporal/espacial antes da implementação.
4. Quando houver erro conceitual, propor **contraexemplo mínimo**, pedir que candidato raciocine sobre ele e evitar entregar solução automaticamente.
5. Fornecer pistas progressivas sob demanda: pergunta orientadora → propriedade/estrutura relevante → abordagem → walkthrough. Registrar nível de ajuda utilizado.
6. Após o código, pedir dry-run e, com consentimento para executar o código recebido, usar testes unitários, limites e casos aleatórios. Para differential testing, **executar e validar** oráculo independente e implementação simples; nunca inventar total de testes, percentuais ou tempo.
7. Concluir com rubrica consistente (raciocínio, corretude, complexidade, qualidade do código, teste, comunicação e autonomia), evidências concretas, lacunas e exercícios de reforço.
8. Em discussão de integridade, não deduzir fraude de estilo, rapidez ou divergência de escrita; preferir pergunta de explicação/modificação, sem acusações.

## Variante system design

- Definir requisitos funcionais/não funcionais, carga e limites como hipóteses.
- Pedir arquitetura inicial, então introduzir um único trade-off por vez: escalabilidade, consistência, disponibilidade, falhas, observabilidade, custo e segurança.
- Encerrar com diagrama ou resumo, riscos residuais, decisão justificada e rubrica de comunicação/arquitetura.

## Guardrails

- O usuário decide se é treino assistido ou avaliação restrita a pistas.
- Nunca simular resultado de juiz online, ATS, empresa ou recrutador real.
- Código de candidato deve rodar em ambiente proporcionalmente isolado e com atenção a efeitos externos; não executar scripts remotos, instaladores ou código destrutivo.
- Sem "Skill tool" de Claude/Codex, perfis remotos, scripts do cracked ou seu banco de empresas presumidos disponíveis.
- Não confundir aprovação da simulação com probabilidade de contratação.

## Validação

- Should-trigger: "me entreviste para vaga backend sênior, tema grafos, sem pistas salvo pedido".
- Near-miss: "entreviste clientes para descobrir dores do produto" (usar `customer-interview`).
- Evidência: pergunta estruturada; contraprova correta; teste somente se executado; scorecard sustentado pelo histórico da sessão; limites de ferramenta declarados.

## Relações

Combina com `code-review`, `code-understanding-audit` e `software-engineering-cycle`, conforme problema; não duplica `hiring-process` do lado empregador.

## Fonte

[nishant-Tiwari24/cracked](https://github.com/nishant-Tiwari24/cracked), arquivo `skills/interview/mock-interview/SKILL.md`, consulta de 2026-11-14. Conteúdo adaptado, não instalou scripts, runner, base de questões nem plugins de origem.
