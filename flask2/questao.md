# 📝 Atividade Avaliativa — Desenvolvimento com Flask (Entrega em 4 dias)
**Objetivo:** Desenvolver uma aplicação web com Flask que permita o cadastro e a visualização de preferências de filmes de usuários. A aplicação deve utilizar formulários, requests/responses, cookies e strings de consulta para armazenar e recuperar as informações.

## 🧩 Descrição da Atividade
Você deverá criar uma aplicação com as seguintes páginas:

### Página inicial (/)

* Apresenta um menu com dois links: “Cadastrar preferências” e “Ver preferências salvas”.

### Página de cadastro de preferências (/cadastro)

* Exibe um formulário com:
    * Nome do usuário (input text)
    * Gênero favorito (select: Ação, Comédia, Drama, Ficção, Terror)
    * Notificações por e-mail? (checkbox)
    * Botão para enviar
* Ao submeter, as informações devem ser armazenadas usando cookies, com validade de 7 dias.
* Redireciona o usuário para a página de visualização.

### Página de visualização de preferências (/preferencias)

* Recupera os dados salvos nos cookies.
* Exibe as preferências do usuário, se existirem.
* Caso não existam, exibe uma mensagem e um link para /cadastro.

### Página de recomendação de filmes (/recomendar)

* Acessada via string de consulta (exemplo: /recomendar?genero=acao)
* Exibe uma lista de filmes com base no gênero informado na string de consulta.
* Use um dicionário fixo com 3 filmes para cada gênero.

## 📦 Entrega

**Você deve entregar:**

* Código da aplicação em uma pasta nomeada nome_sobrenome
* Não enviar a pasta .env
* Arquivo README.md com instruções de execução e explicações sobre como os recursos foram utilizados
* Um print (ou captura de tela) da aplicação em funcionamento

## Como executar

* crie um venv com os comandos `python3 -m venv env` no linux e `py` ou `python -m venv env` no windows, após a instalação do venv abra-o com `source env/Scripts/activate` no windows gitbash e `source env/bin/activate` ou `activate.fish` se estiver usando o shell fish. Após isso baixar o flask com `pip install flask` após a instalação ser concluida abra o diretório da atividade e rode `flask run --debug`

## Recursos utilizados

* foram utilizados os recursos url_for para indexar o caminho das funções python, make_response para uso de cookies, render_template para uso de templates html, request para requisitar valores de forms e redirect para redirecionar o usuário para a página de observação de cookies após a definição dos mesmos.
