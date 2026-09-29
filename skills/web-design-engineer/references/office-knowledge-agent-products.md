# Runtimes e produtos externos para projetos web

Consulta: 2026-09-28. Referências técnicas opcionais, não capacidades instaladas. Usar somente diante de necessidade concreta.

| Projeto | Considerar quando | Conferir antes de integrar |
| --- | --- | --- |
| [Univer](https://github.com/dream-num/univer) | Embutir edição de planilhas/documentos e fórmulas dentro de produto | Pacotes e Facade API da versão real; core Apache-2.0 versus Pro; import/export, colaboração, charts e pivots aparecem na camada comercial do README consultado. Testar fidelidade e persistência; UI não resolve backend. |
| [WeKnora](https://github.com/Tencent/WeKnora) | Aplicação de conhecimento com documentos, RAG e wiki | Modelos, banco/search/storage, ACL por workspace, citações, atualização de fontes e termos de terceiros. Usar retrieval-quality-engineering para evidência de qualidade. |
| [DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | CRM/atendimento WhatsApp com funil e automações | Docker/VPS, Supabase, provedor LLM, canal oficial Meta versus QR/WAHA; credenciais, backup, migrations e cron de atualização. Não instalar como efeito colateral de avaliação. |
| [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) | Visualização geográfica com camadas e cenas 3D | Feeds, freshness, custos/chaves e licença de dados/assets; separar dados observados, simulação e estimativa. |
| [qm](https://github.com/yc-software/qm) | Produto de agentes compartilhados por equipe em Slack/web | Identidade, grants por recurso, escopo de memória/credenciais e separação entre postura de compartilhamento e execução; Postgres para persistência. |

Escolher por requisito, não por popularidade. Um produto completo não é uma biblioteca de componentes. Comparar manutenção, operação e licenças antes de decidir reutilizar código, apenas a arquitetura ou só o padrão de interação.

Para qualquer integração:
- confirmar origem, versão e arquivos realmente utilizados;
- registrar dependências externas e o que ficará a cargo do operador;
- aproveitar sistema visual existente e incorporar o menor módulo viável;
- validar o fluxo real com dados de teste, permissões e estados de falha;
- não prometer serviços, conectores, memória persistente ou agentes porque a referência os documenta.

Avaliação completa e demais runtimes: [lote de referências](../../../evaluations/2026-09-28-agent-tools-office-knowledge-batch.md).
