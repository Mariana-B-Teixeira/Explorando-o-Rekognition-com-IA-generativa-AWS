from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configuração da conexão com o MySQL


def get_connection():
        return mysql.connector.connect(
                host="localhost",
                user="admin",
                password="@senhaforte123",
                database="escola_db"
        )


# ==========================================
# GET - Listar todos os alunos
# ALTERADO:
# Incluídos os campos telefone e data_nascimento
# no retorno da API.
# ==========================================
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome,
            email,
            curso,
            telefone,
            data_nascimento
        FROM alunos
    """)

    alunos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(alunos)


# ==========================================
# GET - Buscar aluno por ID
# ALTERADO:
# Incluídos os campos telefone e data_nascimento
# no retorno da API.
# ==========================================
@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            nome,
            email,
            curso,
            telefone,
            data_nascimento
        FROM alunos
        WHERE id = %s
    """, (id,))

    aluno = cursor.fetchone()

    cursor.close()
    conn.close()

    if aluno:
        return jsonify(aluno)

    return jsonify({"erro": "Aluno não encontrado"}), 404


# ==========================================
# POST - Cadastrar novo aluno
# ALTERADO:
# Adicionados telefone e data_nascimento
# na leitura do JSON e no INSERT.
# ==========================================
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')
    curso = dados.get('curso')
    telefone = dados.get('telefone')
    data_nascimento = dados.get('data_nascimento')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alunos
        (
            nome,
            email,
            curso,
            telefone,
            data_nascimento
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        nome,
        email,
        curso,
        telefone,
        data_nascimento
    ))

    conn.commit()

    novo_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({
        "mensagem": "Aluno cadastrado com sucesso",
        "id": novo_id
    }), 201


# ==========================================
# PUT - Atualizar aluno
# ALTERADO:
# Adicionados telefone e data_nascimento
# na atualização do registro.
# ==========================================
@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')
    curso = dados.get('curso')
    telefone = dados.get('telefone')
    data_nascimento = dados.get('data_nascimento')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE alunos
        SET
            nome = %s,
            email = %s,
            curso = %s,
            telefone = %s,
            data_nascimento = %s
        WHERE id = %s
    """, (
        nome,
        email,
        curso,
        telefone,
        data_nascimento,
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "mensagem": "Aluno atualizado com sucesso"
    })


# ==========================================
# DELETE - Remover aluno
# Nenhuma alteração necessária.
# ==========================================
@app.route('/alunos/<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "mensagem": "Aluno removido com sucesso"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
