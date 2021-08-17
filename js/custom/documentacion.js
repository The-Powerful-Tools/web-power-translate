window.addEventListener('DOMContentLoaded', (event) => {
    var lol = document.getElementsByClassName('gray');
    for(i = 0;i < lol.length;i++){
        if(lol[i].ariaExpanded) {
            lol[i].insertRule('transform: rotate(90deg);')
        }
    } 
    });