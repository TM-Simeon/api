// alert("yes")
function changeId(id){
	// document.getElementById("id").id = "text";
	document.getElementById("text1").style="display:none";
	document.getElementById("text2").style="display:none";
	document.getElementById("text3").style="display:none";
	document.getElementById("text4").style="display:none";
	document.getElementById("text5").style="display:none";
	document.getElementById("text6").style="display:none";
	document.getElementById("text7").style="display:none";
	document.getElementById("text8").style="display:none";
	document.getElementById("text9").style="display:none";

	document.getElementById(id).style="display:inline-block";

	// alert(id+" well")
}

function searchCourse(){
	var email = document.getElementById("save email").innerHTML;
	var course = document.getElementById("courseSelect").value;
	window.location.href = "searchCourse1?email="+email+"&course="+course;
}

function insertcourse(course, email){
	// email = mymail
	window.location.href = "insertcourse?email="+email+"&course="+course;
	// alert(email+" you have successfully registered for "+course)
}