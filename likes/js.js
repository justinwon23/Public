




function add(id){
    var Countelement = document.querySelector(id);
    console.log(Countelement);
    Countelement.innerText = parseFloat(Countelement.innerText)  + 1 + " likes"
    // Countelement.innerText = Countelement.innerText + "dog"
}