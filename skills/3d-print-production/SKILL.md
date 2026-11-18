---
name: 3d-print-production
description: Planejar e verificar a produção de peças por impressão 3D, do requisito e CAD até fatiamento, envio autorizado, acompanhamento e validação física, sem presumir impressora conectada.
---

# 3D Print Production

## Trigger
Use para peça que deve ser **fabricada por impressão 3D**: conceito, CAD, material, encaixe, fatiamento, envio à impressora ou análise do resultado. Para asset somente visual/game, use a skill de modelagem 3D correspondente.

## Contrato por objeto
Registrar função, dimensões/unidades, interfaces, tolerâncias, material, cargas, ambiente de uso, impressora/bico/filamento reais (se conhecidos), limites de tempo/custo e critério de aceitação. Identificar os desconhecidos sem inventar especificações.

## Etapas e saídas verificáveis
1. **Brief e referências:** confirmar objeto, função e restrições. Saída: especificação versionada com limites e medidas.
2. **Geometria mestre:** criar/revisar CAD paramétrico e vistas coerentes com a mesma fonte. Saída: geometria e inspeção dimensional; imagem isolada não demonstra precisão.
3. **Fabricabilidade:** checar malha, unidade, envelope, paredes, tolerâncias, pontes, inclinação, suportes, montagem, orientação e risco estrutural. Saída: versão exportável e pontos pendentes.
4. **Fatiamento:** comparar para o equipamento real material, layer height, bico, infill, suportes, tempo, massa, acabamento, adesão e custo estimado. Saída: pacote específico de impressão ou handoff manual documentado.
5. **Preflight físico:** checar máquina, placa, espaço de movimento, alimentação de filamento, versão do fatiamento e parâmetros de segurança. Saída: confirmação explícita do usuário para o envio exato; preparar projeto não autoriza iniciar impressão.
6. **Despacho/reconciliação:** se houver ferramenta real, distinguir preparado, enviado, aceito na fila, iniciado, terminado e aprovado fisicamente. Timeout ou resposta ambígua requer consulta do estado antes de reenviar. Saída: comprovante verificado ou status desconhecido.
7. **Feedback e revisão:** documentar medidas da peça, encaixes, empenamento, adesão, falhas e parâmetros alterados. Saída: comparação entre versão planejada e resultado físico, com próximos testes.

## Boundaries
- Se CAD, slicer, impressora, inventário ou controle físico não estiverem conectados, entregar especificação e procedimentos, nunca alegar impressão executada.
- Não desabilitar proteções de máquina. Para peças estruturais, médicas, elétricas, pressurizadas ou de segurança, exigir avaliação adequada e não tratar protótipo como certificação.
- Não assumir Bambu Lab, Bambuddy, PrintLab, Text-to-CAD, Studio, Windows/macOS Computer Use ou acesso local como instalados.
- Credenciais e permissões de LAN/cloud exigem justificativa, least privilege e aprovação; mudança de modo pode impactar aplicativos existentes.
- Reutilizar arquivos/projeto anterior quando identificados, em vez de criar cópia paralela.
- Registrar arquivos/versões e distinguir teste sintético, verificação no slicer e teste físico.

## Integração
Use `parametric-cad-drawing` para geometria, `agent-action-governance` para envio, `verify-before-claim` na confirmação e `concept-to-3d-asset` somente para referências visuais necessárias.

## Origem
Fluxo geral adaptado metodologicamente de https://github.com/AFangTeam/PrintLab (README e .agents/skills/printlab/SKILL.md, consulta em 2026-11-18). **Não foi instalado ou executado.** O software PrintLab tem licença PolyForm Noncommercial; esta skill é uma redação original e não distribui código/rotinas internas do aplicativo.
