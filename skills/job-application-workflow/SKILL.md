---
name: job-application-workflow
description: "Avaliar aderência a vagas e preparar candidaturas personalizadas com currículo, carta, revisão independente e preparação para entrevistas, preservando fatos e aprovação humana."
---

# Job Application Workflow

## Objetivo
Conduzir uma candidatura de ponta a ponta, distinta de apenas monitorar vagas: decidir se vale aplicar, produzir materiais personalizados e preparar entrevistas sem criar experiência fictícia ou enviar candidaturas sem autorização.

## Quando usar
Quando o usuário trouxer uma vaga e currículo/perfil para avaliar fit, adaptar currículo, produzir carta ou preparar entrevista. Para alertas recorrentes de novas vagas, delegar a `job-opportunity-monitoring`.

## Workflow
1. **Grounding**: coletar vaga e descrição com URL/data, currículo real, projetos comprováveis, localização, elegibilidade, idioma, prioridades e restrições. Distinguir informação não verificada de dado confirmado.
2. **Gate de elegibilidade**: conferir requisitos obrigatórios, regime, localização, autorização para trabalhar, salário e disponibilidade. Informações ausentes ficam como `unknown`, nunca como confirmação.
3. **Score de fit**: separar requisitos obrigatórios, experiências equivalentes, evidência de resultados, lacunas e potencial de aprendizado. Justificar recomendação `apply / stretch / skip` sem prometer chance de contratação.
4. **Tailoring**: mapear requisito → evidência factual no histórico → seção do currículo. Reordenar e reescrever para clareza e ATS sem inventar cargo, competência, certificado, número ou data. Preparar carta específica com motivação sustentada por fatos; não copiar frases vagas do anúncio.
5. **Draft–review–revise**: primeira versão, revisão crítica independente quanto a precisão, relevância, exageros, consistência e formato, depois versão corrigida com mudanças visíveis. A revisão pode ocorrer em duas passagens no mesmo ChatGPT; não fingir segundo agente.
6. **Entrevista**: gerar perguntas a partir da descrição e lacunas, respostas STAR baseadas em exemplos reais, perguntas ao entrevistador e exercício prático de simulação.
7. **Entrega e controle**: fornecer materiais editáveis, matriz de evidências, dúvidas pendentes e checklist de envio. Candidatura, e-mail ou upload externos somente mediante ação autorizada pelo usuário; nunca executar envio em massa por padrão.
8. **Aprendizado**: registrar feedback de entrevista e resultados somente em local autorizado e reutilizar fatos validados, evitando reescrever histórico profissional a cada vaga.

## Integrações e limites
- Pode usar pesquisa na web para vagas, arquivos fornecidos pelo usuário, ferramentas de documentos e conectores quando disponíveis.
- Não requer Claude Code, Bun, LaTeX, Python ou automação de portais. Se uma saída LaTeX for solicitada, a compilação precisa de runtime real.
- Respeitar dados pessoais, confidencialidade dos empregadores, termos das fontes e confirmação humana antes de qualquer efeito externo.
- Não disponibilizar publicamente perfis profissionais, e-mails, contatos ou documentos privados.

## Aceitação
- **Should trigger**: "Adapte meu currículo a esta vaga e me prepare para a entrevista".
- **Near miss**: "Avise quando aparecer vaga de analista", coberto por `job-opportunity-monitoring`.
- Cada requisito prioritário tem evidência ou lacuna declarada; revisão identifica afirmações não comprovadas; saída não afirma envio sem confirmação.

## Proveniência
Adaptado de https://github.com/ai-job-search-dev/ai-job-search (README consultado em 2026-10-24). Preserva fit assessment, CV tailoring, fluxo drafter–reviewer e preparação de entrevistas. Exclui comandos `/setup`, `/scrape`, `/apply`, ferramentas locais e dependências específicas de Claude Code, portais dinamarqueses e compiladores LaTeX.
