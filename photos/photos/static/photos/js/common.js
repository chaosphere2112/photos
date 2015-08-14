function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function getToken(){
	return getCookie("csrftoken");
}

function ajax(url, data, success, failure, method) {
	if (method === undefined) {
		method = "POST";
		var type = "json";
	}

	$.ajax(url, {"method": method,
				 "headers":{"X-CSRFToken": getToken()},
				 "data": JSON.stringify(data),
				 "dataType": type,
				 "mimeType": "application/json",
				}).done(function(data) {
		if (success !== undefined) {
			success(data);
		}
	}).fail(function(jqxhr){
		if (failure !== undefined) {
			failure(jqxhr);
		}
	});
}