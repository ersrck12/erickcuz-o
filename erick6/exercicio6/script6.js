let cliques = 0;
let mostraHTML = document.getElementById("mostraHTML");

function contador() {
   
    cliques+=0;

    mostraHTML.innerHTML = `<p> número de cliques: ${cliques}</P>`
    console.log(cliques);
}