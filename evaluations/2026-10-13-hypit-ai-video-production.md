# Avaliação: hypit-ai/hypit

- Data: 2026-10-13
- Fonte: https://github.com/hypit-ai/hypit
- Skill original: https://github.com/hypit-ai/hypit/blob/main/skills/hypit/SKILL.md
- README: https://github.com/hypit-ai/hypit/blob/main/README.md
- Licença: https://github.com/hypit-ai/hypit/blob/main/LICENSE
- Arsenal: `stacks/evaluate-and-import-skill/STACK.md`, `skills/skill-security-review/SKILL.md`, `skills/short-form-video-engineering/SKILL.md`
- Revisão: branch `main`, 13/10/2026 (sem fixação de commit na avaliação).
- Classificação: **D — ferramenta técnica com metodologia aproveitável**.
- Decisão: **registrar como integração externa opcional; não importar a skill original nem instalar runtime automaticamente**.

## O que faz

Hypit é um sistema de produção de vídeo por agentes, baseado em linguagem de composição SVML, runtime próprio e componentes reutilizáveis. Recebe referência ou briefing e permite construir composições com material existente, cenas programáticas, geração opcional de imagem/áudio/vídeo, legendas e efeitos sincronizados a palavras/eventos. Tem proposta de reutilizar uma composição para gerar múltiplas variantes. Os slogans sobre alcance de 100 milhões de views são alegações de marketing, não resultados garantidos.

## Onde agrega

- Variantes sistemáticas de anúncios e vídeos curtos: trocar hook, narrador, idioma, produto, CTA, B-roll, preservando a composição.
- Relacionar cenas, overlays, legendas e eventos à fala em vez de tempos absolutos frágeis.
- Separar brief, roteiro, componentes, timeline, mídia, render, testes e export.
- Declarar dependências/custos de modelos e manter o render reproduzível.

## Sobreposição e ownership

O Arsenal já possui `short-form-video-engineering`, `video-editing-pipeline`, `explainer-video-production`, `synthetic-presenter-video`, `watch-video` e a stack `social-growth-engine`. Elas são owners canônicos das metodologias editoriais e de QA. **Não criar duplicata `hypit`**. Para execução real via Hypit, considerar a skill oficial apenas em ambiente de coding agent com instalação, credenciais, serviços e runtime verificados; não supor que a skill instalada em Codex esteja disponível no ChatGPT. Uma integração futura deve possuir testes de render e documentação de custos.

## Portabilidade para ChatGPT

O ChatGPT pode analisar roteiro e referência fornecida, estruturar brief, mapa semântico de cenas, plano de versões, instruções de componentes, revisão editorial e critérios de QA. Pode escrever artefatos/configuração textual quando solicitado. Sem execução e validação do runtime Hypit não afirmar que criou um vídeo final via Hypit, renderizou ou aplicou `npx skills add`. Serviços de geração e componentes de mídia exigem capacidades e contas disponíveis no ambiente.

## Revisão de segurança e licença

**Veredito de segurança: CAUTION (revisão documental, não auditoria exaustiva do código).**

- Skill remete a instalação de executável, serviços, Providers, modelos, credenciais, downloads, geração e render; tudo isso amplia superfícies de rede, subprocessos, gastos e supply chain.
- Não executei instaladores nem código de terceiros; nenhum scanner automatizado foi executado nesta avaliação. Ausência de achados não comprova segurança.
- Recomendar isolamento do projeto e credenciais, least privilege, aprovação de gastos, orçamento, fixação de versão/commit, revisão dos pacotes e providers antes da instalação, inspeção de downloads, execução e outputs; evitar envio não autorizado de referências privadas a provedores externos.
- Direitos de terceiros sobre vídeos de referência, imagens, vozes, identidade e música precisam ser observados. Não clonar pessoas/vozes sem autorização; distinguir recriação formal de uso indevido da identidade.
- Licença **Apache-2.0 modificada com condições**, não Apache-2.0 pura: restrições a SaaS multi-tenant, redistribuição comercial de derivados e alteração de identificação nos locais previstos; exige avaliação jurídica para oferta de serviço a terceiros. O fornecedor informa que não reivindica propriedade dos outputs, sujeito a termos de serviços terceiros.
- Não adotar promessas de viralidade como evidência de performance.

## Checklist de aplicação

1. Definir consentimento, objetivos, formatos e autorização de fontes.
2. Identificar momentos semânticos e o que muda/permanecerá fixo em cada variante.
3. Produzir composição parametrizada, mapa de fala e regras de transições.
4. Escolher runtime: montagem manual, ferramenta atual disponível ou Hypit instalado e validado.
5. Verificar sincronização de legendas e áudio, safe areas, legibilidade, continuidade e qualidade final.
6. Medir variantes por métricas reais, sem inferir viralidade.
7. Registrar versão, dependências, custo, provedores e provenance.

## Limites da validação

Inspecionados README, skill original e licença via conector GitHub. Não houve instalação, execução, geração ou benchmark, nem varredura completa de todos os arquivos e dependências. Esta avaliação recomenda adaptação conceitual e revisão técnica aprofundada antes de operar Hypit em produção.
