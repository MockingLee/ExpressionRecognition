(function () {
    var takePicture = document.querySelector("#take-picture")
    var showPicture = document.querySelector("#show-picture");
    if (takePicture && showPicture) {
        // Set events
        takePicture.onchange = function (event) {
            // Get a reference to the taken picture or chosen file
            var files = event.target.files,
                file;
            if (files && files.length > 0) {
                file = files[0];
                try {
                    var url = "faceDet"
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', url, true);
                    xhr.responseType = "blob";
                    xhr.onload = function () {

                        if (this.status == 200) {
                            var blob = this.response;

                            showPicture.onload = function (e) {
                                window.URL.revokeObjectURL(showPicture.src);
                                var sub = document.getElementById("sub")
                                if (sub)
                                    sub.parentNode.removeChild(sub)
                                var MyDiv = document.getElementById("01")
                                var bt = document.createElement("button");           //createElement生成button对象
                                bt.id = "sub"
                                bt.innerHTML = "预测";
                                bt.onclick = function () {                          //绑定点击事件
                                    var upload = new Upload(file);
                                    upload.doUpload();
                                };
                                MyDiv.appendChild(bt);
                            };
                            showPicture.src = window.URL.createObjectURL(blob);

                        }
                    }
                    var formData = new FormData();
                    formData.append("file", file);
                    xhr.send(formData);


                    // Get window.URL object


                    // var URL = window.URL || window.webkitURL;
                    // //
                    // // // Create ObjectURL
                    // alert(file)
                    // var imgURL = URL.createObjectURL(file);
                    // //
                    // // // Set img src to ObjectURL
                    // showPicture.src = imgURL;

                    // Revoke ObjectURL after imagehas loaded
                    // showPicture.onload = function () {
                    //     // URL.revokeObjectURL(imgURL)
                    //     alert(123)
                    //
                    //
                    // };
                } catch (e) {
                    try {
                        // Fallback if createObjectURL is not supported
                        var fileReader = new FileReader();
                        fileReader.onload = function (event) {
                            showPicture.src = event.target.result;
                        };
                        fileReader.readAsDataURL(file);
                    } catch (e) {
                        // Display error message
                        var error = document.querySelector("#error");
                        if (error) {
                            error.innerHTML = "Neither createObjectURL or FileReader are supported";
                        }
                    }
                }
            }
        };
    }
})();

var Upload = function (file) {
    this.file = file;
};

Upload.prototype.getType = function () {
    return this.file.type;
};
Upload.prototype.getSize = function () {
    return this.file.size;
};
Upload.prototype.getName = function () {
    return this.file.name;
};
Upload.prototype.doUpload = function () {
    var that = this;
    var formData = new FormData();

    // add assoc key values, this will be posts values
    formData.append("file", this.file, this.getName());
    formData.append("upload_file", true);

    $.ajax({
        type: "POST",
        url: "getPre",
        xhr: function () {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                myXhr.upload.addEventListener('progress', that.progressHandling, false);
            }
            return myXhr;
        },
        success: function (data) {
            // your callback here
            alert(data)
        },
        error: function (error) {
            // handle error
        },
        async: true,
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        timeout: 60000
    });
};

Upload.prototype.progressHandling = function (event) {
    var percent = 0;
    var position = event.loaded || event.position;
    var total = event.total;
    var progress_bar_id = "#progress-wrp";
    if (event.lengthComputable) {
        percent = Math.ceil(position / total * 100);
    }
    // update progressbars classes so it fits your code
    $(progress_bar_id + " .progress-bar").css("width", +percent + "%");
    $(progress_bar_id + " .status").text(percent + "%");
};



