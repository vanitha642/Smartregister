function openMenu(){

let menu=document.getElementById("sideMenu");

if(menu.style.width==="250px"){
menu.style.width="0";
}
else{
menu.style.width="250px";
}

}

function toggleProfile(){

let menu=document.getElementById("profileMenu");

if(menu.style.display==="block"){
menu.style.display="none";
}
else{
menu.style.display="block";
}

}
