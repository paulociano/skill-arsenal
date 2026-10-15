---
name: python-interactive-prototyping
description: "Construir protótipos Python interativos escolhendo entre demos de funções/modelos no estilo Gradio e notebooks reativos/reproduzíveis no estilo marimo, com contratos de estado, segurança e teste de runtime."
---

# Python Interactive Prototyping

## Objetivo
Escolher e implementar a menor interface Python útil, preservando estado, rastreabilidade, entradas/saídas e verificabilidade real.

## Quando usar
- Uma função/API/modelo precisa de demonstração, controles, upload e resultado imediato.
- Uma análise, experimento ou simulador exige controles, gráficos, SQL e cálculos dependentes que reajam consistentemente.
- Não ativar para SaaS complexo com autenticação, tenancy, pagamentos e workflows de produção; nesses casos usar stack de web app funcional.

## Escolha
**Gradio**: preferir para demo centrada em função ou modelo com contrato input → processamento → output, inclusive mídia, feedback e inferência. **marimo**: preferir quando dependências entre células, exploração reativa, SQL, reprodutibilidade e versionamento em Python são centrais. Ambas são opções de runtime externas, não ferramentas embutidas no chat.

## Workflow
1. Definir público, tarefa central, entradas/saídas, sensibilidade dos dados, latência e critérios de sucesso.
2. Selecionar modalidade: interface tipo Gradio, notebook reativo tipo marimo ou UI nativa já disponível; não instalar outra framework quando a existente satisfaz.
3. Separar função de domínio, ingestão, validação, estado e apresentação. Declarar schemas e valores ausentes/erro.
4. Para **Gradio**: construir mínimo viável com `Interface` para função simples ou `Blocks` para múltiplos estados e fluxos. Prever progresso, fila/concurrency, timeout, limites de upload, gerenciamento de sessão e callbacks sem efeitos implícitos.
5. Para **marimo**: explicitar grafo de dependências entre células, evitar estado oculto e mutação global; garantir recálculo ou estado stale honesto, parâmetros editáveis, execução como script quando necessário e fontes de SQL identificadas.
6. Quando houver dados sensíveis, revisar exposição de arquivo, link compartilhável, logs, PII, autenticação, execução de código e políticas de hospedagem. `launch()` local e link público são superfícies diferentes.
7. Usar exemplos reais não sensíveis ou fixtures sintéticas; validar entradas inválidas, múltiplos usuários, sessões, latência, saída e fallback.
8. Publicar ou afirmar aplicação funcional somente após rodar no runtime-alvo. Se não houver Gradio/marimo instalados, entregar código/plano de integração sem afirmar deploy.

## Verificações
- Comparar cálculo via função pura vs interface.
- Reexecutar entrada idêntica e inspecionar consistência.
- Testar fluxo de erro e limpeza de estado.
- Verificar importabilidade, versions/pins, inicialização real e comportamento no browser quando disponível.
- Documentar dependências de Python, serviços e modelos externos.

## Aceitação
Should-trigger: "Crie um playground web em Python para comparar resultados de dois modelos".
Near-miss: "Faça um CRM multiusuário com login, assinatura e permissões".
Entregar critério de escolha, protótipo mínimo, testes proporcionais, limites do runtime e evidência observável.

## Proveniência
Adaptada de https://github.com/gradio-app/gradio e https://github.com/marimo-team/marimo (2026-10-15). Não pressupõe instalações ou hospedagem já configuradas.
