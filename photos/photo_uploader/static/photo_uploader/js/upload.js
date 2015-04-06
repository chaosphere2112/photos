// Set up event on drag/drop for upload_block

function init_uploader() {

    var uploader = document.getElementById("upload_block");
    uploader.addEventListener("dragenter", dragenter, false);
    uploader.addEventListener("dragover", dragover, false);
    uploader.addEventListener("dragexit", dragexit, false);
    uploader.addEventListener("drop", drop, false);

    var template = document.getElementById("image_form_template");
    template = template.getElementsByClassName("image_wrapper")[0];

    var form = document.getElementById("upload_form");
    var csrf_token = getCookie("csrftoken");


    function dragenter(e) {
        e.stopPropagation();
        e.preventDefault();
    }
    function dragover(e) {
        e.stopPropagation();
        e.preventDefault();
        // Add class to show we're over it
        uploader.classList.add("dragged_over");
    }
    function dragexit(e) {
        e.stopPropagation();
        e.preventDefault();
        // Add class to show we're over it
        uploader.classList.remove("dragged_over");   
    }
    function drop(e) {
        e.stopPropagation();
        e.preventDefault();

        var dt = e.dataTransfer;
        var files = dt.files;

        handleFiles(files);
        uploader.classList.remove("dragged_over");
    }

    function num_children(node) {
        var real_count = 0;
        for (var i = 0; i < node.childNodes.length; i++) {
            var child = node.childNodes.item(i);
            if (child.nodeType === 1) {
                real_count++;
            }
        }
        return real_count;
    }

    function handleFiles(files) {
        var formData = new FormData();
        formData.append("csrfmiddlewaretoken", csrf_token);
        var file_num = num_children(form) - 1; // adjust for CSRF token
        if (file_num == 0) {
            // first append, add "save" button
            var save_button = document.createElement("input");
            save_button.id = "submit_button";
            save_button.type = "submit";
            save_button.value = "Save Captions";
            form.appendChild(save_button);
        } else {
            save_button = form.getElementsByTagName("input").namedItem("submit_button");
        }

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var imageType = /^image\//;

            if (!imageType.test(file.type)) {
                continue;
            }

            var form_elements = template.cloneNode(true);
            form_elements.id = file.name;
            var img = form_elements.getElementsByTagName("img")[0];
            img.file = file;

            var inputs = form_elements.getElementsByTagName("input");
            inputs[0].name = "file_name_" + file_num;
            inputs[0].value = file.name;
            inputs[1].name = "caption_" + file_num;

            var remove = form_elements.getElementsByTagName("button")[0];
            remove.addEventListener("click", removeElementFunc(form_elements), false);

            form.insertBefore(form_elements, save_button);

            var reader = new FileReader();
            reader.onload = (function(aImg) { return function(e) { aImg.src = e.target.result; }; })(img);
            reader.readAsDataURL(file);
            
            formData.append(file.name, file);
            file_num ++;
        }

        var xhr = new XMLHttpRequest();
        xhr.open('POST', "/photos/upload", true);
        xhr.onload = function(e) { 
            result = JSON.parse(e.currentTarget.responseText);
            console.log(result);
        };

        xhr.send(formData);  // multipart/form-data
    }
    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2) return parts.pop().split(";").shift();
    }
    function removeElementFunc(el) {
        return function(e) {
            form.removeChild(el);

            var xhr = new XMLHttpRequest();

            var name = el.getElementsByTagName("input")[0].value;
            
            xhr.open('DELETE', "/photos/upload", true);
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

            xhr.onload = function(e) { 
                result = JSON.parse(e.currentTarget.responseText);
                console.log(result);
            };

            xhr.send(JSON.stringify({"filename": name}));
        }
    }

}

init_uploader();