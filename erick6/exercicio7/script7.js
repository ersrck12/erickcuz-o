let mostraHTML = document.getElementById("mostraHTML");

let cliques = 0;

function aleatorio() {

cliques = parseInt(Math.random() * 101);

mostraHTML.innerHTML += `<p> Numero de cliques: ${cliques}</p>`;
}

function zerar(){

mostraHTML.innerHTML = null;

}