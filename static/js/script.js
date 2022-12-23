
// alert("fine")

function checkpassword(){
	let pass1 = document.getElementById("pass1").value;
	let pass2 = document.getElementById("pass2").value;
	if(pass1 == pass2){
		//do nothing
	}
	else{
		alert("passwords dont match")
	}
}
function changehref(){
	var email = document.getElementById("inputemail").value;
	window.location.href = "/" + email;
}
