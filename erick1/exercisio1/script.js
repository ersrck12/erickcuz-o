let num1;
let num2;
let resultado;

num1 = Number(window.prompt("digite aqui o primeiro número:"));
num2 = Number(window.prompt("digite o segundo número"));

resultado = num1 + num2;

parOuImpar = resultado %2;

/*if(resultado > 10) {
    alert("o número " + resultado + " é maior do que 10")
} else{
    alert("o número " + resultado + " é menor do que 10")
}
alert(resultado);*/

if(parOuImpar == 0) {
    alert("o número " + resultado + " é par")
} else{
    alert("o número " + resultado + " é Impar")
}
alert(resultado);


