# Avaliação — PrettyPrinted/youtube_video_code (todas as pastas)

Data: 2026-10-02  
Fonte: https://github.com/PrettyPrinted/youtube_video_code  
Branch avaliada: `master`  
Commit/tree observado: `9b9389b3ac54d02e4267abc124d136d0f4a5dff7`

## Escopo

Foram triadas **269 pastas de projetos** no padrão `YYYY/MM/DD/<video-projeto>`, cobrindo 2015–2026. A triagem de todas as pastas usou título, posição temporal e manifesto/estrutura do repositório. Onze projetos com novidade plausível foram aprofundados por leitura de código. Não foram executados installers, aplicações, hooks, scrapers, modelos, CLIs ou serviços externos.

Esta avaliação usa a unidade **capability**, não “uma skill por vídeo”. O repositório é predominantemente uma coleção de exemplos didáticos de Flask/Django/Python e deve funcionar como catálogo externo de receitas, não como pacote de skills.

## Resultado executivo

- **0 novas skills criadas.**
- **5 métodos portáveis absorvidos em owners existentes.**
- Projetos técnicos específicos permanecem como **referência externa sob demanda**.
- Tutoriais básicos, duplicados ou datados foram **rejeitados como skills**, sem julgamento de qualidade pedagógica.

### Contagem de triagem

- C → REJECT_AS_SKILL: 174
- B/C → REFERENCE_ONLY: 51
- D → KEEP_EXTERNAL_REFERENCE: 33
- B/D → KEEP_EXTERNAL_REFERENCE: 6
- B/D → ABSORB_METHOD_ONLY: 5

## Métodos absorvidos

1. **PDF/extração estruturada: schema + invariantes semânticas**
   - Fonte: `2026/06/13/How I Read PDFs With Pydantic AI`
   - Observado: extração tipada de extrato bancário e verificação aritmética entre saldo inicial, transações e saldo final.
   - Owner: `document-extraction-pipeline`.
   - Valor: output tipado não basta; relações de domínio calculáveis devem ser verificadas.

2. **Extração web em duas etapas**
   - Fonte: `2026/07/31/How I Scrape Websites With Python in 2026`
   - Observado: discovery por endpoint JSON e detalhe em páginas server-rendered.
   - Owner: `web-extraction-pipeline`.
   - Valor: usar fonte estruturada para descobrir IDs/URLs e raspar somente detalhes necessários.

3. **Browser workers com isolamento por perfil e allowlist**
   - Fonte: `2026/09/30/This Pydantic AI feature make browser automation easy`
   - Observado: subagentes especializados, browser profiles separados e `allowed_domains`.
   - Owner: `computer-use-agent-engineering`.
   - Valor: isolamento por worker deve incluir perfil e rede/domain scope quando disponível.

4. **Hooks como enforcement point, não como policy inteira**
   - Fonte: `2026/09/03/How to Build Custom Hooks for Codex and Claude Code`
   - Observado: `PreToolUse` intercepta tool call antes da execução.
   - Owner: `agent-action-governance`.
   - Adaptação: validar payload, evitar logging irrestrito e rejeitar regras frágeis por substring.

5. **Pipeline local de reunião por artefatos**
   - Fonte: `2026/07/24/How I Use a Local AI Model to Summarize My Video Calls`
   - Observado: vídeo → áudio → transcript → resumo.
   - Owner: `meeting-knowledge-capture`.
   - Valor: cada estágio deve permanecer verificável e fonte/transcript não devem ser descartados antes da validação.

## Candidatos aprofundados, mas não promovidos

### Django + MCP server
`2026/04/16/How to add an MCP Server to Your Django Projects`

Mostra um toolset fino sobre uma service layer e uso de contexto autenticado para mutações. É um bom exemplo de integração, mas uma única implementação simples não sustenta ainda um owner `mcp-server-engineering`. Manter como referência de arquitetura, não skill.

### Pydantic AI básico e harness/memory
`2026/05/13/Learn Pydantic AI in 15 Minutes` e `2026/08/22/Pydantic AI is more powerful with these new features`

Structured output, dependency injection, tools, instrumentation e memory são úteis, mas já pertencem a owners existentes como `structured-output-contract`, `agent-memory-engineering`, `llm-observability-evaluation` e arquitetura de agentes. Não importar runtime PydanticAI/Harness.

### SQLAlchemy mistakes
`2025/05/21/Five SQLAlchemy Mistakes Every Python Developer Should Know`

Boas receitas de ORM, loading e sessão, mas são framework/library knowledge. Devem ser fundamentadas na versão instalada quando usadas, via `library-version-grounding`, não transformadas em skill estática.

### Django Silk
`2025/11/28/How to Fix Your Django App Performance Issues With Django-Silk`

Ferramenta concreta de profiling. Mantida como referência. O comportamento canônico é medir/query-profile antes de otimizar; a ferramenta depende do projeto.

### Django Tasks 6.0
`2025/12/28/Intro to the Django Tasks Framwork: New in Django 6.0`

Capability relevante, mas altamente versionada. Consultar documentação atual da versão do Django no projeto. Não codificar como skill genérica.

## Segurança e portabilidade

- O repositório contém exemplos que usam subprocess, proxies, credenciais-placeholder, APIs, autenticação, uploads, cloud e hooks.
- Nenhum código externo foi executado nesta avaliação.
- Exemplos de hooks podem registrar payloads de tool calls; isso pode capturar dados sensíveis.
- O scraper de 2026 inclui proxy placeholders. O padrão de extração foi absorvido **sem** adotar proxy bypass ou anti-detection.
- Exemplos de browser agents com proxies/perfis foram usados apenas para o princípio de isolamento; o Arsenal não assume proxies nem ferramentas da fonte.
- Model names e APIs do tutorial são exemplos temporais, não defaults canônicos.
- Receitas antigas podem estar incompatíveis com versões atuais; uso futuro exige `library-version-grounding`.

## Mudanças publicadas no Arsenal

- `skills/document-extraction-pipeline/SKILL.md`
- `skills/web-extraction-pipeline/SKILL.md`
- `skills/computer-use-agent-engineering/SKILL.md`
- `skills/agent-action-governance/SKILL.md`
- `skills/meeting-knowledge-capture/SKILL.md`

O `ARSENAL INDEX.md` não precisa ser alterado porque nenhuma skill/stack foi criada ou renomeada e as descriptions canônicas continuam válidas.

## Limites da avaliação

- “Todas as pastas” significa triagem de todos os 269 projetos pelo tree/manifest e aprofundamento seletivo dos candidatos com novidade plausível, conforme a política de lote do Arsenal.
- Não significa execução funcional de 269 demos.
- Tutoriais com nome semelhante foram consolidados por capability para evitar duplicação.
- Projetos antigos permanecem úteis pedagogicamente; “REJECT_AS_SKILL” significa apenas que não justificam uma skill operacional separada.

## Apêndice — triagem de todas as 269 pastas

| Pasta | Família | Decisão | Motivo |
|---|---|---|---|
| 2015/11/18/Adding jQuery Events to Yet to Be Created Elements | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/Creating a RESTFul API Using Python and Flask (2 of 4) - POST Requests | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/Creating a RESTFul API Using Python and Flask (3 of 4) - PUT Requests | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/Creating a RESTFul API With Flask (1 of 4) - GET Requests | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/Creating a RESTFul API With Flask (4 of 4) - DELETE Requests | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/How to Use Underscore Templates Part 2 | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/18/How to Use Underscore Templates | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/21/An Introduction to Python and Flask Templates | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/22/Python and Flask Templates Part Two - Loops and Inheritance | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/23/Basic Flask Folder Structure | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/23/Flask Hello World | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/24/Adding Columns to Data Sourced jQuery Data Table | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/28/An Intro to AJAX Promises in jQuery | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/28/Decoupling AJAX Calls and Data in jQuery | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/11/30/jQuery Promise Methods - Fail and Always | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/05/How to Send HTTP Requests in Python for Beginners | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/06/Learn How to Send Requests to the Google Maps API With Python | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/07/An Example Of Using the Google Maps API With Python | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/14/Inserting Into a MySQL Database in Flask Using Flask-MySQLDB | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/19/Creating Your Own jQuery Promises | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/20/Using jQuerys each Function | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/21/How to Use Flask to Create and Read Cookies | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/22/Using the url_for Function in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/24/Creating a RESTFul API in Flask Using Flask-Restless and Flask-SQLAlchemy - GET Requests | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/25/POST and DELETE Requests in Flask-Restless | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/28/An Introduction to Flask-Uploads | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2015/12/29/Flask Request Decorators | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/01/04/Creating a Login Page in Flask Using Sessions | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/02/20/Form Handling in Flask Using WTForms | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/02/21/Form Handling in Flask - WTForms Validators | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/04/27/Creating a User Login System Using Python, Flask and MongoDB | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/05/20/Python Requests Tutorial - How to Call a Weather API | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/05/23/Creating a MongoDB-Backed RESTFul API With Python and Flask | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/05/26/Creating a RESTFul API With Python and Bottle | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/06/27/Creating a Chat App With Flask-SocketIO | async / realtime | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/07/22/Submit AJAX Forms with jQuery and Flask | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/08/15/Flask Blueprints - Using Templates | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/08/25/Intro to Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/10/10/Intro to Flask-Admin | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2016/12/14/Flask-Admin Custom Views | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/01/17/Using Flask-WTForms With Flask-Bootstrap | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/03/03/Build a User Login System With Flask-Login, Flask-WTForms, Flask-Bootstrap, and Flask-SQLAlchemy | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/03/27/Using jQuery to Update a Page Without Refresh (Part 1 of 2) | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/06/Flask - Basic App Organization | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/19/Using Flask-Mail to Send Email Confirmation Links | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/21/Intro to Flask-WTF (Part 1 of 5) | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/24/Using Validators in Flask-WTF (Part 2 of 5) | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/26/Using a reCAPTCHA in Your Flask-WTF Form (Part 3 of 5) | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/04/28/Flask-WTF - Creating a Macro to Reduce Code Duplication (4 of 5) | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/05/05/Flask-WTF - Converting a Bootstrap Template (5 of 5) | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/05/23/Creating a Dynamic Select Field With Flask-WTF and JavaScript | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/09/01/Generating Select Fields in Flask-WTF From SQLAlchemy Queries (QuerySelectField) | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/09/04/Building a Blog App With Flask and Flask-SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/09/25/Creating Paypal Express Payments in a Flask App | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/09/27/Creating a Todo List App With Flask and Flask-SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/09/28/Connect to Twitter and Github With OAuth in Flask Using Flask-Dance [Part 1] | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2017/10/12/Integrating Flask-Dance With Flask-Login and Flask-SQLAlchemy[Part 2] | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/01/16/Django Authentication Basics | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/02/14/Building a Fortnite Stat Comparison App With Flask and Bulma | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/03/15/How to Use Django REST Framework Permissions | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/03/31/Creating a Chat App in Flask Using Pusher and jQuery | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/04/12/Creating a Weather App in Django Using Python Requests [Part 1] | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/04/18/Creating a Weather App in Flask Using Python Requests [Part 1] | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/04/23/Creating a Weather App Using Node and Express | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/05/20/Using an SSH Tunnel to With Flask-SQLAlchemy for Python Anywhere MySQL Database | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/05/24/Creating a Dynamic Select Field With Flask-WTF and JavaScript | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2018/06/10/Using the Django LoginView | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/01/01/Using the Inline Form Set Factory in Django (Part 1 of 2) | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/01/04/Creating a Diary App in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/01/30/Authentication and Authorization With Flask-Login | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/05/07/Python Requests Beginner Tutorial - POST Requests With Stripe API | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/05/09/Flask Movie API Example | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/05/29/Connecting to a MongoDB in Flask Using Flask-PyMongo (2019) | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/05/30/MongoDB Operations Using Flask-PyMongo (2019) | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/06/03/Updating the Flask Weather App [Part 2] | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/06/06/Updating the Django Weather App [Part 2] | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/06/12/Building a URL Shortener in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/06/14/Getting Started With Flask-SQLAlchemy [2019] | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/06/21/Get Form Checkbox Data in Flask With .getlist | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/10/Parsing and Formatting Dates in Python With Datetime | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/21/Return JSON Data in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/23/3 Quick Tips to Make Your Flask Apps Better | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/24/Build a Question and Answer App in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/25/Deploy a Flask App to Heroku With a Postgres Database [2019] | deploy / infra | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/26/How to Fix werkzeug.exceptions.BadRequestKeyError - 400 Bad Request in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/27/Django Example App - YouTube Search With YouTube Data API | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/28/Create a YouTube Search App in Flask Using the YouTube Data API | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/29/Use Flask-SQLAlchemy With Existing Database With Reflect and Automap | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/30/Create Custom Commands in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/07/31/How to Convert JSON Data Into a Python Object | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/01/How to Install and Use Django on Windows for Beginners (2019) | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/02/Intro to Django Messages | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/03/The Basics of Django ListView | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/04/Organizing a Flask Project Beyond Single File | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/05/Flask-Praetorian Walkthrough A Library for API Security With JSON Web Tokens JWT | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/06/CORS in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/07/Adding Links to Views in Django Templates | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/08/Flask REST API Example With Pluggable Views and MethodView | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/08/19/Return JSON Data in Flask 1.1 | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/09/08/Sending Emails in Django With Celery | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/09/23/Connecting to a MySQL Database in Flask Using Flask-MySQLDB (2019) | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/10/11/Intro to Flask-Security | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/10/17/Some New Features in Python 3.8 | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/10/19/Deploy a Serverless Flask App using Zappa | deploy / infra | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/10/28/Python Tutorial for Beginners #1 - Printing, Input, and Variables | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/11/19/Using the Python String Methods | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/12/16/Building a Simple Static Site Generator in Python | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2019/12/26/Intro to Marshmallow A Python Object Serialization Library | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/01/01/Validation in Python's Marshmallow Library | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/01/06/Using Flask-WTF With Flask-Uploads | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/01/18/A Quick Intro to Translation in Django (Internationalization) | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/02/07/An Introduction to Sessions in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/02/10/Creating a Login Page in Flask Using Sessions | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/02/11/Creating a Poll App in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/02/16/Using Django Widget Tweaks to Easily Modify Form Field HTML Attributes | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/02/28/How to Export CSV Files From Django | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/03/09/How to Copy Django Model Instance Objects | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/03/15/How to Install and Use Django on Windows for Beginners (2020) | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/04/16/How to Use MySQL and SQLite Database Functions With Flask-SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/04/28/How to Use the Related Name Attribute in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/05/10/Creating a Custom Save Method in Django Models | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/05/16/Adding Extra Fields On Many-To-Many Relationships in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/05/Intro to Flask-Caching | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/08/How to Create Custom Commands in Django | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/10/Deploy a Django App to Heroku | deploy / infra | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/12/Accepting Payments in Flask Using Stripe Checkout [2020] | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/15/How to Use a Database Connection URL in Django | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/17/How to Connect to a Postgres Database in Python | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/19/Intro to Flask Blueprints | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/22/Flask Blueprints - Using Templates | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/24/How to Create a Celery Task Progress Bar in Django | async / realtime | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/26/Flask-SQLAlchemy Example Query: Get Average Fulfillment Time | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/06/29/How to Create a Grid in a Jinja2 Template | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/07/01/Accepting Payments in Django Using Stripe Checkout | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/07/03/Asynchronous Tasks in Python - Getting Started With Celery | async / realtime | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/07/06/Intro to Postgres JSON Columns in Flask-SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/07/13/Building a Food Tracker App in Flask | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/01/Beginner Flask Project: Create a Todo App With Flask and MongoDB | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/04/Intro to FastAPI - The Best Way to Create APIs in Python? | FastAPI | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/06/How to Create Joins in SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/15/Integrating Tortoise ORM into a FastAPI App | FastAPI | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/19/Integrating AIOHTTP Into a FastAPI App | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/09/30/Django Pagination Tutorial | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/10/05/Some New Features in Python 3.9 | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/10/27/Server-Side Sessions in Flask with Flask-Session | deploy / infra | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/11/24/How to Call a Async Function From Synchronous Code in Python | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2020/12/31/How to Speed Up API Requests With Async Python | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/01/05/FastAPI Authentication Example With OAuth2 and Tortoise ORM | auth / security | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/01/29/Python Files - How to Read & Write Files With 5 Examples | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/02/17/How to Return Files in FastAPI | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/03/25/Django Debug Toolbar - A Tool to Help You With Your Django Projects | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/04/10/How to Create Background Tasks in Fast API | async / realtime | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/05/10/How to Upload Files to S3 Using Django Storages | deploy / infra | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/05/22/Some New Features in Flask 2.0 | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/05/24/Using Async Functions Inside of Flask Routes | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/07/20/How to Write Complicated Queries in Django With F Expressions | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/07/27/The First Thing You Should Do at the Start of a New Django Project | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/07/28/How to Use Select Related and Prefetch Related in Django | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/08/22/How to Perform Full Text Searches in Django With Postgres | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/09/01/Type Hints in Python: What, Why, and How | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/10/14/How to Use Google Sheets With Python (2021) | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/10/27/Building a Kanban Board App in FastAPI and React | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/11/21/How to Use Django Sessions | Django | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/11/30/How to Enable User Invites in Flask-User | Flask | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2021/12/17/Querying With Dates in  Flask-SQLAlchemy | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/01/03/Creating One-To-Many Relationships in Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/05/Creating Many-To-Many Relationships in Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/22/Uploading and Returning Files With a Database in Flask | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/25/Connecting to a Database in Flask Using Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/28/Inserting, Updating, and Deleting from a Database in Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/29/Intro to Flask-SQLAlchemy Queries | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/01/30/SQLAlchemy Migrations Using Flask-Migrate | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/02/02/How to Use Flask-SQLAlchemy With Flask Blueprints | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/03/10/Five Python OOP Features You Should Know | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/03/30/Dynamic Web Pages Without JavaScript? - Intro to HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/04/09/Django + HTMX Example App: Progress bar, infinite scroll and modal with NO JavaScript | async / realtime | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/05/10/How to Sort Results in PyMongo | data / performance | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/05/13/First Look at PyScript - Completely Replace JavaScript With Python in Your HTML | frontend / interaction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/06/10/Learn a Different Approach to Configuring Your Flask Apps | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/07/05/How to Upload, Process, and Download CSV Files in Flask apps | data / extraction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/08/10/How to Cancel a Running Task in Celery | async / realtime | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/09/30/How to Add Flask-Migrate to an Existing Flask-SQLAlchemy Project | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/10/02/How to Use Association Objects and Proxies in Flask-SQLAlchemy Many to Many Relationships | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/10/04/How to Easily Style Your Django Form Fields With Django Widget Tweaks | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/10/26/Some New Features in Python 3_11 | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2022/11/18/How to Use Recaptchas in Django Forms | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/11/30/Getting Started With Testing in Flask | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2022/12/06/Intro to Automated Browser Testing Flask Apps With Playwright and Pytest | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/01/13/How to Deploy a Flask App and Postgres Database to Render | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/01/27/An Example of Celery in a Flask App With Multiple Files | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/01/30/How to Upload Files to AWS S3 in Flask | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/02/11/Using Multiple Select Fields with Flask-WTF and Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/02/25/How to Integrate Filestack in Flask Apps to Easily Handle File Uploads | data / extraction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/03/30/Creating a Chat App With Flask-SocketIO | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/04/28/The Simplest Login System in Flask: HTTP Basic Auth | auth / security | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/04/29/How to Schedule Tasks in the Future With Celery | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/04/30/Create a Dependent Select Field With Flask-WTF and HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/05/01/How to Easily Create REST APIs with Flask-RESTX | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/05/06/Create a Dependent Select Field in Django With HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/05/10/JSON Web Token Authentication in Flask-RESTX | auth / security | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/05/27/How to Use Async SQLAlchemy in FastAPI | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/06/29/How to Deploy a Django App and Postgres Database to Render | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/07/17/How to Deploy a Flask App to a Linux Server with a Domain Name | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/08/08/How to Create an Instant Search Bar With Flask and HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/08/09/How to Write SQLAlchemy 2.0-Style Queries in Flask-SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/08/10/Intro to Flask-Admin | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/09/07/Intro to Django Tenants - Create a Separate Database Schema for Each User | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/09/08/How to Deploy a Flask and Celery App to Render | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/09/19/How to Dynamically Add Schedules to Celery Beat | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/10/04/Getting Started With Django Celery Beat | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/10/16/Easiest Way to Send Emails in Flask | AI / agents | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2023/11/30/How to Upload Files Directly From Frontend to S3 Using Flask and Uppy | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2023/12/20/Multipart Uploads Directly to S3 With Uppy | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/01/17/Getting Started With Django All Auth | auth / security | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2024/02/29/Creating a Progress Bar for Celery Task Progress in a Flask App | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/03/28/How to Stream OpenAI API Responses in a Flask App | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/04/26/Reading Emails in Python with IMAP Tools | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/05/18/Getting Started With Elasticsearch in Django - Faster Text Search for Your Apps | data / performance | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/06/20/Building a Speech Transcription App Using Flask and OpenAI | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/07/24/Create APIs in Django - Intro to Django Ninja | Django | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2024/08/21/How to Create an Instant Search Bar With Django and HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2024/09/18/How to Add Language Translations to Your App With Flask-Babel | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2024/09/25/How to Run Flask and Postgres in a Docker Environment | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/10/26/How to Stream OpenAI API Responses in a Django App | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2024/11/07/How to Use the Flask Command Line Interface | Flask | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2024/12/11/How to Create a Modal With HTMX Only (No JavaScript) | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/01/03/Intro to Customizing the Django Admin Dashboard | Django | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/01/11/Intro to Django Crispy Forms - An Easy to Style Forms in Django | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/02/05/How to Read and Write CSV Files in Python | data / extraction | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2025/02/28/Building a Document Summarizer App with Flask and OpenAI | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/03/19/Getting Started With Celery: Asynchronous Tasks in Python | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/03/21/Getting Started With Celery in Flask Apps | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/03/24/Intro to Background Tasks in Django With Celery | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/03/26/How to Deploy a Django App and Postgres Database to Fly.io | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/03/28/How to Easily Manage Your Django Settings With Django-Environ | Django | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/03/31/How to Create a Flask & HTMX Form With Flask-WTF and Modern SQLAlchemy | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/04/02/Getting Started With Flask-Security | auth / security | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/04/04/Sending Emails in Flask-Security With Celery | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/04/10/Intro to the Django REST Framework | Django | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/04/18/Real-Time Updates with Flask-SSE (Server-Sent Events) | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/05/15/How to Use SQLAlchemy in 2025 | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/05/21/Five SQLAlchemy Mistakes Every Python Developer Should Know | data / performance | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2025/05/31/Learn to Build AI-Powered Apps in Python - Beginner Tutorial | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2025/06/06/Learn FastAPI, Fast | FastAPI | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/06/12/How to Deploy a Django App Online | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/06/27/Flask and Celery: Deploy to Sevalla Platform Tutorial | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/07/04/FastAPI Backend Project for Beginners - PydanticAI & Redis | AI / agents | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/07/10/React Frontend Project for Beginners - React Query & FastAPI | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/07/16/Learn How to Deploy a FastAPI and React Project | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/07/25/How to Use Celery Beat in a Flask App to Create Dynamic Schedules | async / realtime | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/07/30/Laravel Deployment Troubleshooting for Beginners | deploy / infra | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/08/10/Getting Started With Database Migrations in Flask - Flask-Alembic | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/08/22/Learn to Create Dynamic Choice Fields With HTMX | frontend / interaction | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/08/30/Modern SQLAlchemy + Flask - Full Tutorial | data / performance | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2025/09/05/Gemini API and Python - Intro Tutorial | AI / agents | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/10/31/Integrate Clerk Authentication With a React Frontend and Django API | auth / security | D → KEEP_EXTERNAL_REFERENCE | Receita técnica dependente de framework/serviço; consultar sob demanda |
| 2025/11/28/How to Fix Your Django App Performance Issues With Django-Silk | data / performance | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2025/12/28/Intro to the Django Tasks Framwork: New in Django 6.0 | Django | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2026/03/30/Every Class-Based View in Django Explained | AI / agents | B/C → REFERENCE_ONLY | Boa receita de implementação, sem mudança comportamental suficiente para skill |
| 2026/04/16/How to add an MCP Server to Your Django Projects | AI / agents | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2026/05/13/Learn Pydantic AI in 15 Minutes | AI / agents | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2026/05/18/Beginner Python AI Project Example - Workout Tracker | AI / agents | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2026/06/13/How I Read PDFs With Pydantic AI | AI / agents | B/D → ABSORB_METHOD_ONLY | Padrão portátil incorporado em owner existente |
| 2026/07/24/How I Use a Local AI Model to Summarize My Video Calls | AI / agents | B/D → ABSORB_METHOD_ONLY | Padrão portátil incorporado em owner existente |
| 2026/07/31/How I Scrape Websites With Python in 2026 | data / extraction | B/D → ABSORB_METHOD_ONLY | Padrão portátil incorporado em owner existente |
| 2026/08/17/Intro to Niquests - A complete replacement for the Python Requests library | Python / web misc | C → REJECT_AS_SKILL | Tutorial básico, estreito, duplicado ou datado; não justifica owner |
| 2026/08/22/Pydantic AI is more powerful with these new features | AI / agents | B/D → KEEP_EXTERNAL_REFERENCE | Útil, mas overlap alto ou evidência insuficiente para skill nova |
| 2026/09/03/How to Build Custom Hooks for Codex and Claude Code | AI / agents | B/D → ABSORB_METHOD_ONLY | Padrão portátil incorporado em owner existente |
| 2026/09/30/This Pydantic AI feature make browser automation easy | AI / agents | B/D → ABSORB_METHOD_ONLY | Padrão portátil incorporado em owner existente |
