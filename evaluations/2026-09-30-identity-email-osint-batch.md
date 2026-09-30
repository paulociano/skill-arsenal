# Avaliação em lote — OSINT de username, email, Google identity e breach exposure

Data: 2026-09-30

## Escopo

Fontes:
- https://github.com/soxoj/maigret
- https://github.com/megadose/holehe
- https://github.com/mxrch/GHunt
- https://github.com/khast3x/h8mail
- https://github.com/sharsil/mailcat
- https://github.com/alpkeskin/mosint

Fluxo aplicado: `arsenal-autopilot`.

Nenhum instalador, binário, script, proxy, API externa, lookup de alvo real, breach database ou credencial foi executado/usado.

## Resumo

| Fonte | Classe | Decisão | Owner |
| --- | --- | --- | --- |
| Maigret | B/D | KEEP_EXTERNAL_REFERENCE | pesquisa OSINT / privacidade, sem owner novo |
| Holehe | C/D | KEEP_EXTERNAL_REFERENCE | privacidade / exposição de conta |
| GHunt | D/B | KEEP_EXTERNAL_REFERENCE | ferramenta especializada Google OSINT |
| h8mail | D/B | KEEP_EXTERNAL_REFERENCE | breach exposure / security research |
| mailcat | C/D | KEEP_EXTERNAL_REFERENCE | email-enumeration OSINT |
| mosint | C/D | KEEP_EXTERNAL_REFERENCE | agregador de email OSINT |

## Leitura do conjunto

Os seis projetos convergem em uma capacidade operacional: partir de identificadores como username ou email para descobrir contas associadas, metadados, presença em serviços, relações ou exposição em breaches.

Isso pode ser útil em segurança defensiva, investigação autorizada, proteção de conta própria e incident response, mas também aumenta capacidade de rastreamento e perfilamento de pessoas. Por isso, o Arsenal não deve transformar esse conjunto em uma skill geral de "descobrir tudo sobre uma pessoa".

## Maigret

### O que faz
Pesquisa usernames em milhares de sites, coleta perfis e pode expandir recursivamente por identificadores descobertos.

### Valor metodológico
- separar descoberta de conta de inferência de identidade;
- manter provenance por site e evidência;
- rotular resultados como encontrados/não encontrados/indeterminados;
- recursão deve ter limites claros e não virar expansão automática de identidade.

### Decisão
Referência externa. Não criar skill operacional de profiling de pessoas.

## Holehe

### O que faz
Testa se um email está associado a contas em múltiplos serviços, muitas vezes via fluxos de login, cadastro ou recuperação.

### Avaliação
A metodologia operacional depende de account-enumeration side channels e pode revelar presença de uma pessoa em serviços sem consentimento. O ganho para o Arsenal é principalmente um lembrete de privacy risk e false-positive discipline.

### Decisão
Não importar workflow operacional.

## GHunt

### O que faz
Framework focado no ecossistema Google para investigação por email, Gaia ID, Drive, BSSID e outros identificadores.

### Avaliação
É uma ferramenta técnica especializada que depende de autenticação/cookies e endpoints específicos. O valor metodológico geral é pequeno frente aos riscos de credenciais, privacidade e dependência de comportamento de terceiros.

### Decisão
KEEP_EXTERNAL_REFERENCE.

## h8mail

### O que faz
Pesquisa emails e outros identificadores em breach services e dumps locais, inclusive dados sensíveis como hashes e senhas em algumas integrações.

### Avaliação
A parte de breach exposure pode ser legítima para defesa, mas a fonte também inclui workflows de chasing e consulta de dados comprometidos que não devem virar capability genérica do Arsenal.

Princípios portáveis:
- nunca exibir senha completa quando não for indispensável;
- diferenciar "email apareceu em breach" de "credencial atual é válida";
- tratar dumps e breach APIs como dados altamente sensíveis;
- provenance e data da exposição importam;
- resultados precisam de escopo e autorização adequados.

### Decisão
Referência externa, sem skill operacional.

## mailcat

### O que faz
Resolve possíveis endereços de email a partir de username/nickname em vários provedores, usando SMTP, cadastro, recovery e browser automation.

### Avaliação
Capability de enumeração de contas/email. Pode ser útil para verificação própria, mas é muito fácil de aplicar a terceiros.

### Decisão
Não importar.

## mosint

### O que faz
Agrega múltiplos serviços para email verification, contas sociais, breaches, emails relacionados, DNS/IP e paste dumps.

### Avaliação
É um agregador de várias capacidades já vistas nas demais fontes, sem uma metodologia nova que justifique skill própria.

### Decisão
KEEP_EXTERNAL_REFERENCE.

## Padrões úteis absorvidos como política de avaliação

Para futuras fontes OSINT de identidade:
- distinguir pesquisa sobre entidade pública/empresa de investigação sobre pessoa física;
- usar somente dados públicos necessários ao objetivo declarado;
- não automatizar expansão recursiva de identidade por default;
- evitar lookup de credenciais vazadas ou recovery metadata de terceiros sem contexto defensivo/autorizado;
- separar presença de conta, identidade real, breach exposure e validade de credencial como claims diferentes;
- preservar provenance, timestamp e incerteza;
- mascarar secrets e dados comprometidos;
- não interpretar "não encontrado" como inexistência;
- respeitar rate limits e termos do serviço em qualquer integração real.

## Segurança e portabilidade

- Nenhum projeto foi instalado ou executado.
- Nenhuma conta, email, username, Gaia ID, breach dump ou API de terceiros foi consultado.
- Nenhum cookie, token ou credencial foi fornecido a ferramentas externas.
- Não foram importados métodos de bypass, proxy/Tor, rate-limit evasion ou account enumeration.
- Não foi criada skill nova porque o valor incremental é menor do que o risco de generalizar a capacidade operacional.

## Conclusão

Este lote deve permanecer como referência externa e fonte de guardrails de privacidade/OSINT. O Arsenal já possui owners suficientes em `secure-code-privacy-review`, `first-customer-research`, `evidence-claim-verification`, `skill-security-review` e pesquisa geral. Criar uma skill genérica de person/email OSINT ampliaria capacidade sensível sem ganho metodológico proporcional.
