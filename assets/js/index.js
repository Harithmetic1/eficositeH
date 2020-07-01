var icon = document.getElementById("nav-icon");
var nav = document.getElementById("nav");
icon.addEventListener("click", function(){
    nav.classList.toggle("open")
})

const carouselImages = document.querySelector('.carousel_images');
const carouselButtons = document.querySelectorAll('.carousel_button');
const numberOfImages = document.querySelectorAll('.carousel_images img').length;
const splash = document.querySelector('.splash');
let imageIndex = 1;
let translateX = 0;


document.addEventListener('DOMContentLoaded', (e)=>{
    setTimeout(()=>{
        splash.classList.add('display-none');
    }, 2000);
})


carouselButtons.forEach(button => {
    button.addEventListener('click', event => {
        if(event.target.id === 'previous') {
            if(imageIndex !== 1){
                imageIndex--;
                translateX += 300;
            }
        }
        else{
            if(imageIndex !== numberOfImages) {
                imageIndex++;
                translateX -= 300;
            }
        }

        carouselImages.style.transform = `translateX(${translateX}px)`;
    });
    
})
