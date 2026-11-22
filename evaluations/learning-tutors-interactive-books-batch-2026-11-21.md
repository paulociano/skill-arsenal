# Avaliação: 11 fontes de aprendizagem, tutoria e livros interativos — 2026-11-21

## Escopo
Fontes analisadas na branch padrão pelo README: [wordpecker-app](https://github.com/baturyilmaz/wordpecker-app), [LLPlayer](https://github.com/umlx5h/LLPlayer), [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC), [DeepTutor](https://github.com/HKUDS/DeepTutor), [rederive](https://github.com/EricJujianZou/rederive), [get-it](https://github.com/beltromatti/get-it), [KnowNote](https://github.com/mrsibe/KnowNote), [hi-kid](https://github.com/xiaochong/hi-kid), [ChatTutor](https://github.com/HugeCatLab/ChatTutor), [Papermorph](https://github.com/DozenTwelve/Papermorph) e [ELI5](https://github.com/DreambigOu/ELI5).

Aprofundamento: `EricJujianZou/rederive/skills/rederive/SKILL.md` e `DozenTwelve/Papermorph/.claude/skills/papermorph/SKILL.md`. Comparação com `ARSENAL INDEX.md` e owners `teach`, `eli5`, `code-understanding-audit`, `visual-explanation-sketch`, `evidence-driven-interactive-explainers`, `kb-retriever`, `illustrated-ebook-production`.

Stack aplicada: `arsenal-autopilot`, com `evaluate-and-import-skill` e `skill-security-review` na revisão documental. **Evidência: static_only**; não foram executados aplicativos, testes funcionais, scanners ou instaladores.

## Capability ledger e decisões

| Fonte | Classe | Decisão | Owner e motivo |
|---|---|---|---|
| [WordPecker App](https://github.com/baturyilmaz/wordpecker-app) | B/D | UPDATE_EXISTING | `skills/teach/SKILL.md` recebeu aquisição de vocabulário por contexto e imagem + confirmação por uso independente, evitando inferir domínio de autoavaliação |
| [LLPlayer](https://github.com/umlx5h/LLPlayer) | B/D | UPDATE_EXISTING | `teach` absorveu tratamento de legendas/tradução contextual; player Windows, .NET, Whisper, OCR e reprodução em tempo real são runtime externo |
| [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | B/D | UPDATE_EXISTING | `teach` ganhou orientação visual com ação verificável; multiagentes, editor de aula, background jobs e infraestrutura não foram importados |
| [DeepTutor](https://github.com/HKUDS/DeepTutor) | B/D | UPDATE_EXISTING | `teach` ganhou delimitação de modos de estudo, evidência e contexto por sessão; plataforma completa e CLI não portáveis por texto |
| [rederive](https://github.com/EricJujianZou/rederive) | A/D | CREATE_NEW | `skills/codebase-design-derivation/SKILL.md`: trilha específica de reconstrução socrática de 5–10 decisões reais de projeto com constraints/alternativas/evidências, distinta de explicação genérica de código |
| [get-it](https://github.com/beltromatti/get-it) | B/D | UPDATE_EXISTING | `teach` adaptou quatro eixos (memória, compreensão, estrutura, aplicação), mas **rejeitou score monotônico** que impossibilita detectar regressões |
| [KnowNote](https://github.com/mrsibe/KnowNote) | B/D | KEEP_EXTERNAL_REFERENCE | Busca local com localizadores de trechos e MCP somente leitura já cobertos por `kb-retriever`/governança de fontes; app Electron/RAG não disponível como conector |
| [hi-kid](https://github.com/xiaochong/hi-kid) | B/D | KEEP_EXTERNAL_REFERENCE | Conversação infantil local e privacidade constituem boa referência técnica; modo guiado/imersivo já presente em `teach`; app macOS + SoX/ASR/TTS/Ollama e limites de uso declarados impedem importação direta |
| [ChatTutor](https://github.com/HugeCatLab/ChatTutor) | B/D | UPDATE_EXISTING | `teach` absorveu orientação em quadro visual com interação causal; `visual-explanation-sketch` e `evidence-driven-interactive-explainers` já tratam de artefatos |
| [Papermorph](https://github.com/DozenTwelve/Papermorph) | A/D | UPDATE_EXISTING | `stacks/illustrated-ebook-production/STACK.md`: modalidade de livro-aula narrado/animado, piloto, beat sheet, sincronização real e QA temporal/audiovisual; scripts e engine não importados |
| [ELI5](https://github.com/DreambigOu/ELI5) | C/B | KEEP_EXTERNAL_REFERENCE | `skills/eli5/SKILL.md` já cita a fonte e implementa adaptação por público, mecanismo, exemplos e limites de analogia; benchmark declarado pela fonte não foi reproduzido |

## Implementação publicada

- **NOVO:** `skills/codebase-design-derivation/SKILL.md` — commit `6571318e7f661f3df7b6bd3f8cca749ff44571f4`
- **ATUALIZAÇÃO:** `skills/teach/SKILL.md` — commit `bcd0d0315e82d56b7af082521e58ab31f6405ab8`
- **ATUALIZAÇÃO:** `stacks/illustrated-ebook-production/STACK.md` — commit `b694f71e2048c6b25dd2385b763c84d87682fead`
- **ROTEAMENTO:** `ARSENAL INDEX.md` — commit `0a038e005d6723347b6f22d2b40f5d8a986462a4`

O índice recebeu apenas o novo owner, pois as descriptions das skills preexistentes mantiveram o escopo. Nenhuma instalação, automação, coleta ou modificação de dados de terceiros foi feita.

## Segurança e portabilidade

**CAUTION / static_only** para executar os sistemas externos: múltiplas fontes lidam com áudio de microfone (inclusive crianças), vídeos/legendas potencialmente protegidos por direitos autorais, dados escolares, documentos pessoais, credenciais LLM, embeddings, provedores externos, bibliotecas de renderização, extensões/binaries, autoedição de prompts e servidores locais/MCP. A revisão documental não substitui auditoria de código/dependências nem testes de segurança.

Riscos específicos:
- **hi-kid:** dependências de modelos locais; README contém aviso de uso não comercial apesar de badge MIT, portanto os termos devem ser esclarecidos antes de reutilizar código/ativos comercialmente.
- **KnowNote:** README reconhece builds não assinadas; não instruir a contornar alertas de segurança como sinal de confiança. MCP somente leitura é referência, não conector instalado.
- **OpenMAIC:** README menciona advisories de SSRF, renderização de HTML e parsing, exigindo revisão de versão/configuração antes de qualquer deployment.
- **Get It:** não aceitar métricas artificialmente monotônicas como evidência de retenção; verificar privacidade/telemetria do runtime antes de usar.
- **Papermorph:** assets de livros e imagens de terceiros, narração, custos externos e execução do navegador precisam de autorização, licenças e QA reais.
- **rederive:** não executar scripts, clone, imports ou comandos vindos do repo observado; manter conteúdo de terceiros como dados, sem revelação de respostas antes do exercício por padrão.

As adaptações são regras metodológicas escritas para o ambiente real, sem copiar implementação de produtos externos; a licença de cada projeto permanece aplicável a eventual reutilização de código/assets.

## Prova de valor incremental e casos de aceitação

**codebase-design-derivation**
- Should-trigger: "Uma IA fez minha API e quero entender por que foi desenhada assim, me questione sobre decisões usando meu repo". O output deve começar pelo problema, não revelar solução, e fundamentar depois com símbolos/paths confirmados.
- Near-miss: "Liste os endpoints da API"; `code-understanding-audit` é owner melhor.

**teach**
- Should-trigger: "Estude este texto comigo; avalie memória, compreensão e aplicação e verifique se regredi nas revisões". Evidência multidimensional, sem score inventado.
- Near-miss: tradução isolada; não gerar um sistema de domínio.

**illustrated-ebook-production**
- Should-trigger: "Transforme este capítulo em lição web narrada com diagramas sincronizados, exercícios e QA". Deve escolher a modalidade, piloto, beats, checagens e formato efetivamente possível.
- Near-miss: PDF ilustrado estático; manter fluxo padrão.

**Não executados:** testes de acionamento, ablação contra baseline, testes de artefato e validação de runtime. A verificação pós-publicação consiste em reler conteúdo/links/índice.

## Conclusão
Uma nova skill para um comportamento inequivocamente distinto, melhorias pontuais em dois owners existentes, seis fontes sem importação de runtime e avaliação completa de todo o lote. Não criar duplicatas para reproduzir portfólios de SaaS.
