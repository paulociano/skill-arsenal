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

- quando o diff for grande ou ruidoso, organizar a revisão por mudanças semânticas relevantes, não por volume bruto de linhas;
- manter um decision log quando decisões do agente/implementador não estiverem diretamente impostas pela spec: decisão, evidência, impacto, reversibilidade e alternativa considerada;
- quando uma visualização ou diagrama ajudar, ligar cada elemento relevante ao arquivo/símbolo/trecho correspondente para que o artefato seja navegável de volta ao código;
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

## Visual blast-radius review

Quando o diff atravessar múltiplos módulos:
- mapear módulos tocados e vizinhos relevantes;
- mostrar novos/removidos/alterados separadamente;
- data-flow e payload changes ajudam a revisar contratos;
- usar a visualização para descobrir perguntas, não como prova automática de impacto;
- verificar no código cada edge/claim material antes de transformar em finding;
- correction metadata deve sobreviver a rerenders, evitando editar artefato gerado manualmente.

## Valor, custo e impacto

Além de standards e spec, para findings ou mudanças materiais perguntar:

- **Value:** qual problema real resolve, para quem, com que frequência e consequência?
- **Cost:** custo de implementar, verificar, entender e manter no futuro.
- **Impact:** comportamento/módulos afetados, acoplamento criado/removido e restrições futuras.

Usar esse eixo para calibrar severidade e evitar recomendar correções caras para problemas marginais. Julgamentos precisam de evidência da revisão alvo, não apenas preferência de reviewer.

## Referências

[revisao-independente-e-pr](references/revisao-independente-e-pr.md) — Consultar ao organizar revisão independente, devolver findings ou corrigir feedback de PR.

[GitHub · mattpocock/skills · code-review](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review)

Decision log, semantic diff e ligação entre visualização e código adaptados de [devdotfast/whiteboard](https://github.com/devdotfast/whiteboard). coldteadotai/pr-lens reforçou blast-radius/data-flow review e visualização de adições/alterações/remoções. Nenhum renderer ou GitHub App é requisito.

Origem local: [code-review.docx](../code-review.docx).

## Cobertura e localização verificáveis

Em revisões com múltiplos arquivos, construir inventário a partir do diff/escopo real: revisado, excluído com motivo e pendente. Não apresentar revisão parcial como completa. Agrupar arquivos relacionados quando o contrato atravessar arquivos, como traduções, schema e consumidor; aplicar apenas regras relevantes àquela unidade.

Separar julgamento do finding de sua localização: confirmar caminho, símbolo, lado/revisão do diff e trecho atual antes de entregar. Reabrir a fonte para tentar refutar o defeito e verificar consequência; remover duplicatas e observações sem impacto sustentado. Ausência de findings não prova ausência de defeitos.

Método refinado a partir de [alibaba/open-code-review](https://github.com/alibaba/open-code-review). Não exige CLI, subagentes ou envio de código a provedor externo; alegações de custo/precisão da fonte precisam de avaliação no workload real.

## Controle explícito de scope creep (2026-10-19)

Em PRs/diffs maiores que o objetivo declarado, acrescentar inspeção de **escopo**, separada de qualidade do código:

1. Congelar uma frase de intenção do usuário/issue/PR antes de classificar arquivos.
2. Inventariar subsistemas tocados, dependências novas, API pública renomeada, alterações em config/CI/build, hunks grandes e formatação incidental.
3. Tratar correspondência de palavras entre paths e intenção como triagem fraca, não prova de pertinência; examinar a relação semântica com o comportamento solicitado.
4. Para cada item suspeito, decidir **KEEP** (necessário), **SPLIT** (independente) ou **JUSTIFY** (mudança transversal exigida por invariante). Nomear arquivo, trecho, risco e destino.
5. Não reverter, editar, reestagiar nem dividir commits apenas para satisfazer a auditoria. Escopo correto não prova correção, segurança ou testes suficientes.

Fonte: https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/scope-creep-detector . Método adaptado sem executar o script `scope_creep.py` ou assumir Git local disponível.

## Triagem adversarial e quality gate por evidência (2026-10-19)

Para revisões de alto risco, executar uma segunda passagem tentando **refutar** cada achado material antes de publicá-lo:

1. Definir inventário do escopo e fronteiras de confiança; registrar arquivos/fluxos inspecionados, excluídos e pendentes.
2. Formular hipótese de falha e caminho de execução ou entrada que a alcança; separar possibilidade teórica de caminho demonstrado.
3. Procurar controles compensatórios, validações em callers, testes, permissões e condições que invalidem a hipótese.
4. Quando viável e autorizado, propor teste mínimo de reprodução; não declarar execução ou exploração sem evidência real.
5. Deduplicar por causa raiz e graduar P0–P3 por impacto, explorabilidade/probabilidade e alcance, sem inflar severidade por padrão de estilo.
6. Entregar finding com **alvo e versão/commit, localizador, evidência, condição de disparo, impacto, confiança, correção mínima, teste de regressão e status de verificação**.
7. Aplicar gate: **confirmado**, **provável**, **não verificado** ou **refutado**; não apresentar suspeita como vulnerabilidade comprovada. Registrar ausência de cobertura explicitamente.

Em codebases com dívida técnica, procurar sinais estruturais além de lint: responsabilidades misturadas, acoplamento crescente, abstrações sem benefício, invariantes implícitas e caminhos de mudança com alto blast radius. Cada recomendação de refatoração precisa indicar custo de manutenção observado e teste de preservação de comportamento; não prescrever reescrita baseada apenas em preferência arquitetural.

**Proveniência e limites:** metodologia inspirada em [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) (auditoria em fases e verificação independente) e [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) (diagnóstico de deterioração de engenharia). Apenas princípios portáveis foram absorvidos; nenhum instalador, scanner, agente externo ou modo auto-fix é assumido disponível. A descrição dos projetos foi verificada no GitHub em 2026-10-19; esta adaptação não equivale a benchmark ou validação experimental das ferramentas originais.
