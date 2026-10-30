# Sistema Web - Cadastro de Alunos

Desafio feito no curso de IA Generativa do SENAI:

Você acaba de receber uma demanda da coordenação da escola: o sistema de cadastro de alunos precisa ser atualizado para registrar também o telefone e a data de nascimento de cada aluno. Sua missão é usar a IA como copiloto para realizar essa alteração no banco de dados e no frontend do sistema, sem quebrar o que já está funcionando.

Sugestão de prompts:

Prompt 1 - Banco de dados
Você é um DBA experiente em MySQL.
Preciso que você gere o comando SQL para alterar uma tabela existente
chamada alunos, que já possui as colunas id, nome, email e curso,
adicionando as colunas telefone (VARCHAR 20) e data_nascimento (DATE),
sem apagar os dados que já estão cadastrados.
Responda de forma direta e objetiva, apenas com o comando SQL necessário
e uma breve explicação do que cada linha faz.

Você: acesse o mysql  e atualize o banco de dados do servidor (e salve uma cópia no pc)

Prompt 2 - Back-end python
Você é um desenvolvedor backend especialista em Python e Flask.
Preciso que você atualize as rotas de uma API REST que faz CRUD de alunos,
atualmente trabalhando com os campos nome, email e curso, incluindo os novos
campos telefone e data_nascimento em todas as rotas: GET, POST e PUT.
O código usa mysql-connector-python para se comunicar com o banco de dados MySQL.
Responda com o arquivo app.py completo e atualizado, com comentários explicando
o que foi alterado.

Você: edite o arquivo app.py com o código sugerido e reinicie o serviço.

 (e salve uma cópia no pc)

Prompt 3 - HTML
Você é um desenvolvedor frontend com experiência em HTML semântico.
Preciso que você atualize um formulário de cadastro de alunos que atualmente
possui os campos nome, email e curso, adicionando os campos telefone e
data de nascimento. A tabela que exibe os alunos cadastrados também deve
ser atualizada com as novas colunas.
Responda com o arquivo index.html completo e atualizado, mantendo a estrutura
e os ids dos campos existentes.

Você: edite o arquivo index.html com o código sugerido.

 (e salve uma cópia no pc)

Prompt 4 - JavaScript
Você é um desenvolvedor frontend especialista em JavaScript puro, sem frameworks.
Preciso que você atualize um arquivo script.js que faz requisições fetch para
uma API Flask de cadastro de alunos, atualmente enviando e exibindo os campos
nome, email e curso, incluindo os novos campos telefone e data_nascimento
nas funções de salvar, editar e listar alunos na tabela da página.
Responda com o arquivo script.js completo e atualizado, explicando
brevemente cada função que foi alterada.

Você: edite o arquivo script.js com o código sugerido.

 (e salve uma cópia no pc)

Prompt 4 - DesignerVocê é um especialista em UX e previsa atualizar a aparencia da tela do sistema, para isso, deve reelaborar o arquivo css style.css para uma aplicação mais profissional, responsiva e moderna.

Você:  atualize o arquivo style.css com o código sugerido.

 (e salve uma cópia no pc)

FIM ?
você deve TESTAR o sistema acessando novamente (seu ip público), e caso esteja tudo ok, envie as cópias dos códigos dos arquivos alterados ♥


## Estrutura do Projeto

- `index.html` — Interface web com formulário de cadastro/edição e tabela de alunos.
- `style.css` — Estilização responsiva da página, formulário e tabela.
- `script.js` — Consumo da API REST (`GET`, `POST`, `PUT`, `DELETE`) via `fetch`.
- `app.py` — API REST em Flask conectada ao MySQL (`escola_db`).
- `database.sql` — Script SQL para criação do banco `escola_db` e da tabela `alunos`.
- `estrutura_tabela_mysql.txt` — Estrutura da tabela `alunos` no MySQL (`DESCRIBE alunos`).
- `requirements.txt` — Dependências Python do servidor Flask.

## Pré-requisitos

- Python 3.8+
- Servidor MySQL

## Como executar

1. **Banco de Dados (MySQL):**
   Execute o script `database.sql` no seu MySQL para criar o banco `escola_db` e a tabela `alunos`:
   ```bash
   mysql -u root -p < database.sql
   ```

2. **Back-end (API Flask):**
   Instale as dependências e inicie o servidor:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   A API ficará disponível na porta `5000`.

3. **Front-end:**
   Abra o arquivo `index.html` no navegador (ou sirva-o via servidor HTTP/Apache). Certifique-se de que a constante `api` no topo de `script.js` aponta para o endereço onde o back-end está rodando (por exemplo, `http://localhost:5000`).
