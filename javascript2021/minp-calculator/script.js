
function equal()
{

   let inputButton = document.getElementById('input').value;

    let a = eval(inputButton);

    document.getElementById('input').value+=a;  
}

function number(val){
    document.getElementById('input').value = val;
}

function operator(){
    document.getElementById('input').value = "";
}