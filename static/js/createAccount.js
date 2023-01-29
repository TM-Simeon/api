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

// general javascript for all files
function changehref(){
	var email = document.getElementById("input2").value;
    var username = document.getElementById("input1").value;
    var password = document.getElementById("pass1").value;
	window.location.href = "/createuser?email="+email+"&username="+username+"&password="+password;
}