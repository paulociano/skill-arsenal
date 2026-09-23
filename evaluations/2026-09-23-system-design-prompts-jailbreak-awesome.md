# Avaliação em lote: System Design Primer e coleções ChatGPT

Data: 2026-09-23. Método: `evaluate-and-import-skill` + `skill-security-review`.

Fontes avaliadas:

- https://github.com/donnemartin/system-design-primer
- https://github.com/rockbenben/ChatGPT-Shortcut
- https://github.com/alphatrait/100000-ai-prompts-by-contentifyai
- https://github.com/Batlez/ChatGPT-Jailbreak-Pro
- https://github.com/mikaelvesavuori/chatgpt-architecture-coach
- https://github.com/taishi-i/awesome-ChatGPT-repositories

## Decisão resumida

Nenhuma nova skill ou stack foi criada.

O único repositório com metodologia claramente forte para um owner existente, `donnemartin/system-design-primer`, **já é a referência explícita de `system-design-engineering`**. Os demais são principalmente catálogos de prompts, um conjunto de priming prompts de arquitetura, um diretório de descoberta e um userscript voltado a jailbreak. O Arsenal já possui owners melhores para prompt engineering, arquitetura, segurança e descoberta.

## Classificação

| Fonte | Classe | Decisão |
|---|---|---|
| donnemartin/system-design-primer | B | já absorvido por `system-design-engineering`; não duplicar |
| rockbenben/ChatGPT-Shortcut | D/C | ferramenta de gestão + corpus de prompts; não importar como skill |
| alphatrait/100000-ai-prompts-by-contentifyai | C | grande prompt dump sem metodologia de avaliação suficiente |
| Batlez/ChatGPT-Jailbreak-Pro | D/C | não importar comportamento de bypass; manter apenas como exemplo de superfície de segurança |
| mikaelvesavuori/chatgpt-architecture-coach | C/B | bons priming prompts, mas owners existentes já cobrem o processo |
| taishi-i/awesome-ChatGPT-repositories | B | índice de descoberta útil, não workflow operacional |

## 1. System Design Primer

Revisão observada: `ae9bbd7b02d90b9866215de185217d33f39ab733` (2026-03-20).

O repositório organiza conceitos de escalabilidade, disponibilidade, consistência, cache, filas, bancos, comunicação e exercícios de system design. Seu processo central é:

1. requisitos, casos de uso, constraints e assumptions;
2. high-level design;
3. desenho dos core components;
4. scale, bottlenecks e trade-offs;
5. back-of-the-envelope estimates quando necessários.

Esse processo **já foi adaptado** em `skills/system-design-engineering/SKILL.md`, que inclusive registra o System Design Primer como referência e adiciona SLOs, failure modes, operações, evolução e grounding em documentação atual.

**Decisão:** nenhum delta material nesta revisão. Não alterar `system-design-engineering`.

## 2. ChatGPT Shortcut / AiShort

Revisão observada: `1db7679dc07c2633188990442c48d1e9c3bcfd52` (2026-08-29).

O projeto é uma aplicação de gerenciamento e descoberta de prompts, com:

- milhares de prompts;
- tags e busca;
- coleções pessoais;
- prompts customizados;
- votação/comunidade;
- export JSON;
- extensão de navegador;
- opções de self-hosting e edição offline.

O ganho é principalmente **UX de catálogo**, não metodologia de prompting. O Arsenal já possui `empirical-prompt-tuning`, que exige cenários, baseline, critérios, holdout e comparação empírica. Um prompt popular ou fácil de copiar não recebe status de “bom” sem teste.

**Classificação:** D como produto, C como fonte metodológica.

**Segurança:** CAUTION para instalar extensão/userscript ou self-host sem revisão adicional. Nenhuma instalação foi executada.

## 3. 100000 AI Prompts by Contentify

Revisão observada: `427259a963a7bd73e90d37cedcc62277b5a5780a` (2023-11-23).

É um corpus massivo de prompts e listas auxiliares. O README descreve categorias amplas, mas não oferece processo forte de:

- seleção por tarefa;
- versionamento de modelos;
- avaliação de qualidade;
- regressão;
- baseline;
- holdout;
- segurança de prompts.

Quantidade não substitui qualidade. O corpus pode ser usado como inspiração ou dataset em uma avaliação explícita, mas não deve virar owner canônico.

**Classificação:** C — prompt library.

**Decisão:** não importar.

## 4. ChatGPT Jailbreak Pro

Revisão observada: `b810b9b98bf150b00971025ccdff569ad2e9cf8d` (2025-06-30).

O repositório contém um userscript Tampermonkey que injeta uma interface sobre `chatgpt.com`, mantém prompts/configuração em `localStorage` e oferece categorias de prompts. Uma seção “advanced” inclui padrões desenhados para contornar comportamento normal por reformulação hipotética/persona.

### Segurança

**Verdict para incorporar comportamento: REJECT.**

Motivo: prompts ou instruções destinados a contornar controles/safety não devem entrar no Arsenal como comportamento operacional.

**Verdict para estudo estático como amostra de segurança: APPROVE com escopo restrito.**

Ele pode servir como exemplo de superfície para `skill-security-review`: userscripts, browser injection, prompts de bypass, alteração de UI e persistência local precisam ser tratados como código não confiável.

O userscript não foi executado e nenhuma extensão foi instalada. A leitura foi estática e parcial; isso não é certificação do script completo.

Nenhuma atualização em `skill-security-review` foi necessária, porque a skill já cobre prompt injection, instruções para contornar safety, persistência e execução de código externo.

## 5. ChatGPT Architecture Coach

Revisão observada: `b5e4c0a07da4d41b0707a543b7d5b1ca83cc768e` (2023-11-24).

O repositório reúne priming prompts para:

- cloud architecture coaching;
- avaliação de diagramas;
- code review orientado por policy;
- geração de diagramas a partir de sketches;
- análise de DORA/software delivery;
- technical debt prioritization;
- testes a partir de API schemas.

Há boas heurísticas: pedir contexto, responder com ações concretas, discutir trade-offs, adaptar a audiência e combinar fatores técnicos/culturais.

Mas o Arsenal já separa essas responsabilidades em owners mais verificáveis:

- `system-design-engineering`;
- `architecture-visualization`;
- `code-review`;
- `project-complexity-management`;
- `deep-grill` / `to-questionnaire`;
- `tdd`.

O padrão “act as a world-class architect” é persona, não metodologia suficiente por si só.

**Classificação:** C/B.  
**Decisão:** não criar skill e não alterar os owners existentes.

## 6. Awesome ChatGPT Repositories

Revisão observada: `6065e1583f39be02de35f2654c2ce1b8a1862810` (2026-09-18).

É um índice amplo de repositórios, dividido em categorias como applications, prompts e recursos. O valor é **discovery**, não execução.

Esse tipo de lista pode ser consultado para encontrar candidatos, mas cada candidato precisa de avaliação própria e fonte primária. O índice não deve ser tratado como autoridade sobre qualidade, segurança ou atualidade de cada projeto listado.

**Classificação:** B como fonte de descoberta.  
**Decisão:** não importar como skill.

## Segurança e limites

A revisão foi read-only. Nenhum installer, extensão, userscript, pacote, binário ou aplicação foi executado.

Foram consultados README, arquivos específicos do Architecture Coach, o início do userscript Jailbreak Pro, estrutura de repositórios e commits recentes observados.

Não foi feita auditoria completa de todos os arquivos das grandes coleções de prompts ou do userscript. Portanto:

- não há claim de segurança total;
- não há claim de qualidade individual dos prompts;
- nenhuma coleção foi promovida apenas por volume, estrelas ou popularidade.

## Resultado para o Arsenal

- nenhuma nova skill;
- nenhuma nova stack;
- nenhuma alteração no `ARSENAL INDEX.md`;
- `system-design-engineering` confirmado como owner correto para o System Design Primer;
- `empirical-prompt-tuning` confirmado como owner correto para avaliação de prompts;
- `skill-security-review` já cobre o tipo de risco observado no Jailbreak Pro;
- este registro evita reavaliação redundante dessas seis fontes.
