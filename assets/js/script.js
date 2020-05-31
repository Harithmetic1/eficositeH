next = document.getElementById("next").addEventListener("click", aFunction)

var reviewHolder = document.getElementById('picture')
function aFunction(){
    
var randomNumber = Math.floor(Math.random() * 3);
reviewHolder.src = "review/rw" + randomNumber + ".jpg"
}