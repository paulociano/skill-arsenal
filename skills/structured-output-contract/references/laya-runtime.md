# Laya: execução opcional e medição real

Usar quando o usuário pedir instalação/velocidade ou quando existir runtime verificado. Não é dependência obrigatória do Arsenal e não altera o modelo que gera as respostas do ChatGPT.

## Instalação isolada

Pré-requisitos: Python 3.10+, espaço para dependências e pesos, acesso autorizado a PyPI/Hugging Face e hardware suficiente. Criar ambiente virtual no destino autorizado. Não instalar servidores, extensões MCP ou serviços externos sem necessidade.

```bash
python -m venv .venv-laya
.venv-laya/bin/python -m pip install laya==0.3.20
.venv-laya/bin/python -m pip check
.venv-laya/bin/python skills/structured-output-contract/scripts/laya_decisions.py
```

No Windows, usar `.venv-laya\Scripts\python.exe` em lugar de `.venv-laya/bin/python`. Em ambientes que usam proxy SOCKS, pode ser necessário instalar `socksio` no mesmo ambiente. Usar o proxy configurado; não contornar restrições de rede.

Para CPU, uma distribuição PyTorch CPU compatível pode reduzir o volume de instalação; escolher a distribuição pela documentação oficial do PyTorch, não presumir GPU. Registrar versões realmente resolvidas. O pacote PyPI 0.3.20 observado não aceita `revision` em `laya.load`, embora o GitHub atual aceite: o script baixa um snapshot por revisão imutável via Hugging Face e passa o diretório local a `load`.

O script fixa `convaiinnovations/laya-multilingual` na revisão `e4e9ddf21a7b1903b7acffd8814ad4307bf63a67`, adequada para testar pedidos em português sem depender de detecção de idioma de frases curtas. Se trocar `--model`, trocar também `--revision`. Não confundir revisão de código com revisão dos pesos.

## Uso real e modelo residente

Para uma decisão, fornecer arquivo JSON com `state` e `questions`, no formato nativo Laya:

```json
{
  "state": "Cliente pediu retorno na terça às 10h.",
  "questions": {
    "horario_explicito": {
      "type": "noul",
      "instructions": "O texto contém um horário explícito para retorno?"
    }
  }
}
```

```bash
.venv-laya/bin/python skills/structured-output-contract/scripts/laya_decisions.py --request pedido.json
.venv-laya/bin/python skills/structured-output-contract/scripts/laya_decisions.py --jsonl
```

O modo JSONL mantém o modelo em memória e lê um pedido JSON por linha da entrada padrão; cada saída contém o resultado real e tempo medido. A mensagem de prontidão sai em stderr. Encerrar a entrada termina o processo. Não há servidor público, execução de ações, cache de respostas nem ferramentas externas acionadas pelo resultado.

Reiniciar o processo para cada decisão inclui novamente o custo de carregamento. Persistência do processo e do ambiente deve ser verificada em cada sessão; um ambiente temporário de conversa não é instalação permanente em outros computadores.

## Benchmark

Sem `--request` ou `--jsonl`, o script executa três casos sintéticos de roteamento, aquecimento e repetições:
- `--iterations 5 --warmup 2 --threads 4 --device cpu` é o padrão;
- registrar mediana, p95, amostras brutas, acertos nas repetições, versões e configuração;
- separar carregamento/imports/downloads da latência com modelo aquecido;
- registrar uma pergunta por request e batch size 1;
- sincronizar GPU antes e depois da medição quando esse dispositivo existir.

Os três casos são smoke tests, não avaliação representativa de qualidade. Comparar acurácia e calibração com dados revisados/holdout antes de confiar em roteamento automático. Repetir três frases não aumenta o número de casos independentes.

Os tempos em milissegundos do projeto dependem de hardware, comprimento, número de perguntas, batching, dtype e aquecimento. Não transferir números de GPU para CPU, nem confundir velocidade de detecção de idioma com inferência. Não prometer que uma classificação rápida acelera geração longa de texto pelo ChatGPT.

## Limites e falhas

- Resultado tipado pode estar errado; interpretar `noul`, `confidence` e distribuições conforme a versão, sem equipará-los a autorização.
- O script retorna saídas nativas; validar o contrato final no consumidor, sobretudo campos ausentes e projeções.
- Usar textos curtos: `max_len` pode truncar entradas; para documentos longos, verificar cobertura explicitamente antes de decidir. Não assumir que um trecho representa o documento inteiro.
- Falhas de instalação/download/inferência devem ser reportadas como falhas, sem substituir por fixture e declarar benchmark real.
- Se runtime estiver indisponível, usar o protocolo metodológico ou encaminhar para análise; não alegar que Laya foi executado.
- Conservar dados sensíveis fora de logs e benchmarks versionados. O benchmark incluído usa apenas frases sintéticas.
- Esta integração fornece decisões; a aplicação/assistente conserva controle de autorização, elegibilidade, revisão, fallback e rollback.

## Fontes

[Laya no GitHub](https://github.com/NandhaKishorM/laya), revisão de código `4066d5d5fbf08b66c6757ddeedbd797bd7655bc0`; README, pyproject.toml, laya/agent.py, laya/structured.py e docs/staged-adoption.md. Conferir a API efetivamente instalada ao executar.
