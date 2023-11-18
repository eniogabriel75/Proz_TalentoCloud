document.body.innerHTML += '<h1 id="titulo">Título do Site</h1>';

document.body.innerHTML +=
  '<div id="produto"><h2>Nome do Produto  </h2><p>Descrição do Produto </p><p>Preço: R$ 20,00</p></div>';

const titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.textContent = "Segundo titulo";
document.body.appendChild(titulo);

const produto = document.createElement("div");
produto.id = "produto";

const nomeProduto = document.createElement("h2");
nomeProduto.textContent = "Nome do Produto 1";

const descricaoProduto = document.createElement("p");
descricaoProduto.textContent = "Descrição do Produto 1";

const precoProduto = document.createElement("p");
precoProduto.textContent = "Preço: R$ 19,99";

produto.appendChild(nomeProduto);
produto.appendChild(descricaoProduto);
produto.appendChild(precoProduto);

document.body.appendChild(produto);
