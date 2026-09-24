# Jev e custo de tarefas no Codex

Data: 2026-09-24. Fontes consultadas no GitHub nesta data; índice canônico e stack `evaluate-and-import-skill` lidos antes da seleção. Avaliação estática, sem instalar ou executar código das fontes.

## Decisão

Criar `codex-cost-efficiency` como fluxo acionado por pedido explícito de economia em projeto Codex. Ele combina medição por tarefa aceita com redução de leitura, saída e contexto, sem impor um modo global. Jev permanece uma integração opcional: nenhum piloto pago ou economia real foi medido aqui. `handoff`, `llm-observability-evaluation` e `model-routing-gateway` já cobrem respectivamente transferência de contexto, avaliação de compressão e roteamento de aplicação; não duplicá-los.

| Fonte | Categoria | Função e ganho incremental | Decisão |
| --- | --- | --- | --- |
| [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | A | Skill oficial para desenhar aplicações com decisões tipadas Jev; não troca o motor interno do Codex | Referência upstream; não importar cópia |
| [FrancoisChastel/jev-code](https://github.com/FrancoisChastel/jev-code) | D | CLI/MCP e skill para chamar classify, check, score e rank no Codex | Candidata de integração futura; não instalar sem projeto, chave e benchmark |
| [n23eos/jev-skills](https://github.com/n23eos/jev-skills) | D | Seletores delimitados de skill, modelo, contexto, testes, bugs e planos; opt-in | Candidata de piloto; o autor não prova economia total |
| [WanLanglin/jev-skills](https://github.com/WanLanglin/jev-skills) | D | Scripts para shortlist, triagem e logs; publica curva e casos negativos | Candidata para corpus grande; números do autor não são economia transferível |
| [zhangyiling108-code/codex-token-optimizer](https://github.com/zhangyiling108-code/codex-token-optimizer/blob/main/SKILL.md) | B | Método de escopo, leitura, saída, MCP e handoff seletivos | Adaptar princípios, sem copiar checklist sempre ativo |
| [luziyezz/codex-skills/token-efficient-workflow](https://github.com/luziyezz/codex-skills/blob/main/token-efficient-workflow/SKILL.md) | B | Investigar a partir de evidência estreita e expandir quando necessário | Consolidar sem instalar segunda skill redundante |
| [robertiuoras/Codex-skill-model-reasoning-router](https://github.com/robertiuoras/Codex-skill-model-reasoning-router) | B/D | Política de modelo/esforço; piloto público reporta mais tokens que baseline | Não importar como promessa de economia; escolher modelo só se a interface permitir e medir |

## Segurança e portabilidade

**APPROVE** para a síntese textual criada: não executa scripts, configurações nem transmite dados. **CAUTION** para integrações Jev: exigem chave de outro serviço, enviam os itens/contexto selecionados à API TypeSafe e podem modificar configuração MCP ou diretórios de skills durante setup. A cadeia completa de dependências e o código dos instaladores não foram auditados; nenhum foi executado. Usar apenas em projeto autorizado, com escopo dos dados revisto, dry-run se disponível, revisão de código/versão fixada e comparação controlada antes de automatizar decisões. Não inserir chaves em chat ou arquivos versionados.

Jev devolve julgamentos tipados, não texto de implementação. Uma recomendação de modelo não altera o modelo de uma conversa Codex já em andamento. A medição de uma chamada Jev isolada exclui custo de preparar candidatos, ferramentas, revisão, reexecução e Codex. Métricas de assinatura/quota não são equivalentes a fatura de API. Não adotar configurações não oficiais de outros harnesses como ajustes do Codex.

## Verificação e limites

Conferir frontmatter e índice, diff e publicação Git. Nenhum benchmark de projeto, chamada paga, instalação MCP, teste de precisão ou economia observada foi realizado. Teste futuro apropriado: mesmo conjunto de tarefas, baseline sem Jev, variante com Jev apenas em triagens repetitivas, aceite e custo total por tarefa, erros omitidos e revisão manual. A falta de chave/projeto de referência impede afirmar redução para o usuário.
