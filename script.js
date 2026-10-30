const api = "http://50.17.13.2:5000";
let editandoId = null;

window.addEventListener("DOMContentLoaded", () => {
  carregarAlunos();

  const botaoSalvar = document.querySelector("#btnSalvar");
  if (botaoSalvar) {
    botaoSalvar.addEventListener("click", salvarAluno);
  }
});

/* =========================
   LISTAR ALUNOS
========================= */
async function carregarAlunos() {
  try {
    const resposta = await fetch(`${api}/alunos`);
    const alunos = await resposta.json();

    const lista = document.getElementById("listaAlunos");
    lista.innerHTML = "";

    alunos.forEach(aluno => {
      const item = document.createElement("tr");

      item.innerHTML = `
        <td>${aluno.nome || ""}</td>
        <td>${aluno.email || ""}</td>
        <td>${aluno.curso || ""}</td>
        <td>${aluno.telefone || ""}</td>
        <td>${aluno.data_nascimento || ""}</td>
        <td>
          <button onclick="editarAluno(${aluno.id})">Editar</button>
          <button onclick="deletarAluno(${aluno.id})">Excluir</button>
        </td>
      `;

      lista.appendChild(item);
    });

  } catch (erro) {
    console.error("Erro ao carregar alunos:", erro);
  }
}

/* =========================
   SALVAR (POST / PUT)
========================= */
async function salvarAluno() {
  try {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const curso = document.getElementById("curso").value;
    const telefone = document.getElementById("telefone").value;
    const data_nascimento = document.getElementById("data_nascimento").value;

    if (!nome || !email) {
      alert("Nome e email são obrigatórios");
      return;
    }

    let url = `${api}/alunos`;
    let metodo = "POST";

    if (editandoId !== null) {
      url = `${api}/alunos/${editandoId}`;
      metodo = "PUT";
    }

    const resposta = await fetch(url, {
      method: metodo,
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        nome,
        email,
        curso,
        telefone,
        data_nascimento
      })
    });

    if (!resposta.ok) {
      throw new Error("Erro ao salvar aluno");
    }

    editandoId = null;

    document.getElementById("nome").value = "";
    document.getElementById("email").value = "";
    document.getElementById("curso").value = "";
    document.getElementById("telefone").value = "";
    document.getElementById("data_nascimento").value = "";

    carregarAlunos();

  } catch (erro) {
    console.error("Erro ao salvar aluno:", erro);
  }
}

/* =========================
   EDITAR
========================= */
function editarAluno(id) {
  fetch(`${api}/alunos`)
    .then(res => res.json())
    .then(alunos => {
      const aluno = alunos.find(a => a.id === id);

      if (!aluno) return;

      editandoId = id;

      document.getElementById("nome").value = aluno.nome || "";
      document.getElementById("email").value = aluno.email || "";
      document.getElementById("curso").value = aluno.curso || "";
      document.getElementById("telefone").value = aluno.telefone || "";

      // ✔ CORREÇÃO DO ERRO DE DATA (FORMATO yyyy-MM-dd)
      document.getElementById("data_nascimento").value =
        aluno.data_nascimento
          ? new Date(aluno.data_nascimento).toISOString().split("T")[0]
          : "";
    });
}

/* =========================
   DELETAR
========================= */
async function deletarAluno(id) {
  try {
    const resposta = await fetch(`${api}/alunos/${id}`, {
      method: "DELETE"
    });

    if (!resposta.ok) {
      throw new Error("Erro ao deletar aluno");
    }

    carregarAlunos();

  } catch (erro) {
    console.error("Erro ao deletar aluno:", erro);
  }
}

/* =========================
   EXPORTAÇÃO GLOBAL (HTML onclick)
========================= */
window.salvarAluno = salvarAluno;
window.editarAluno = editarAluno;
window.deletarAluno = deletarAluno;
window.carregarAlunos = carregarAlunos;