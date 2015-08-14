var current_photo = window.location.pathname.split("/")[3];
$("#save").click(function(){
	var csrf = getToken();

	ajax("/photos/photo/" + current_photo, {"caption": $("#caption").val()}, function(){
		console.log("Updated");
	});
});