let titulo = document.getElementById("titulo");
console.log(titulo);
let link = document.querySelector("a");
console.log(link);

titulo.innerText = "JavaScript";
link.innerText = "Site da Proz";

let listaNaoOrdenada = document.querySelector("ul");
console.log(listaNaoOrdenada);
let listaOrdenada = document.querySelector("ol");
console.log(listaOrdenada);

listaNaoOrdenada.innerHTML = `
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
`;
listaOrdenada.innerHTML = `
<li><a href="https://www.google.com/">Google</a></li>
<li><a href="https://www.facebook.com/?locale">Facebook</a></li>
<li><a href="https://www.instagram.com/">Instagram</a></li>
`;
