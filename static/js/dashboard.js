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

// changeId("text1")