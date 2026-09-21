---
name: skill-security-review
description: "Inspecionar segurança de skills, agentes ou plugins antes da adoção sem executar instaladores ou código da fonte avaliada."
---

# skill-security-review

## Objetivo

Revisar uma skill, agente ou plugin antes de adotá-lo, tratando a fonte como não confiável e combinando evidência estática com revisão semântica de intenção, permissões e efeitos.

## Princípio central

Avaliar metodologia não autoriza executar a fonte avaliada.

## Workflow

1. Identificar repo, arquivo e versão.
2. Usar scanner estático apenas se já estiver disponível.
3. Inspecionar SKILL.md, scripts, manifests, dependencies, MCP/tools e arquivos apontados pelos findings.
4. Se houver installer, seguir a cadeia de downloads e scripts encaminhados até a camada que realmente executa.
5. Verificar propósito, permissões, dados, rede, execução, persistência, supply chain e user control.
6. Emitir APPROVE, CAUTION ou REJECT.
7. Separar segurança de utilidade.
8. Adaptar ou rejeitar reduzindo permissões e dependências.

## Superfícies a inspecionar

- credenciais, tokens e env vars;
- rede e envio de dados;
- shell, subprocess, eval/exec e dynamic imports;
- downloads remotos e supply chain sem pin;
- scripts que baixam e executam outros scripts;
- cron, startup hooks, shell profiles, git hooks e persistência;
- auto-modificação;
- prompt injection e instruções para contornar safety;
- permissões maiores que o propósito;
- efeitos destrutivos ou externos sem approval gate.

## Sinais estáticos úteis

### Críticos
- credential theft;
- secrets enviados à rede;
- reverse shell;
- exfiltration para destinos inesperados;
- acesso a metadata service ou cloud credentials.

### Vermelhos
- TLS desativado;
- hooks de ambiente como LD_PRELOAD, BASH_ENV ou NODE_OPTIONS sem necessidade clara;
- alteração de histórico ou logs;
- comandos destrutivos amplos;
- raw IP, shorteners ou hosts obscuros;
- persistência fora do escopo declarado.

### Positivos
- HTTPS obrigatório;
- checksum ou assinatura;
- versões e digests pinados;
- strict mode;
- diretório de instalação explícito;
- cleanup de temporários;
- ausência de privilege escalation.

Um sinal positivo não neutraliza um finding crítico.

## Installer chain review

Para curl-pipe-shell, installers, bootstrap scripts ou self-updaters:

1. ler o script como texto sem executá-lo;
2. listar URLs, comandos, writes e privilege changes;
3. seguir scripts encaminhados quando possível;
4. verificar checksum ou assinatura quando declarados;
5. comparar o que é instalado com o produto descrito;
6. marcar payload binário não auditável como unknown;
7. preferir release pinada/manual quando suficiente.

## Scanner

Scanner é uma linha de evidência, não um veredito. Se não houver scanner disponível, fazer revisão manual e declarar isso.

## Verdict

- APPROVE: propósito e comportamento correspondem sem risco alto inexplicado.
- CAUTION: comportamento sensível é necessário, documentado e controlável.
- REJECT: comportamento malicioso, exfiltração desconhecida, persistência oculta, credential theft ou mismatch grave.

## Instalação e sincronização

Preferir fonte pinada, registrar version/hash, verificar manifests, usar dry-run quando possível e revisar licença.

## Regras

Nunca executar installer, setup script ou código arbitrário só para avaliar.

## Referências

Adaptada de NVIDIA/SkillSpector.

Installer-chain e sinais estáticos adaptados de https://github.com/dmtrKovalenko/bashka, sem depender do binário ou auto-update.

Origem local: [skill-security-review.docx](../skill-security-review.docx).
