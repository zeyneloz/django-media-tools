window.onload = function (e) {
    (function () {
        var images = document.getElementsByClassName('preview-widget-img');
        for (var i = 0; i < images.length; i++) {
            images[i].onclick = function () {
                var modal = document.getElementById(this.dataset.modalId);
                var modalImg = document.getElementById(this.dataset.modalImgId);
                var captionText = document.getElementById(this.dataset.modalCaptionId);
                modal.style.display = "block";
                modalImg.src = this.src;

                if (captionText) {
                    // if the caption text is visible
                    captionText.innerHTML = this.src;
                    captionText.href = this.src;
                }

                // close the modal when user clicks on the image
                modal.onclick = function () {
                    modal.style.display = "none";
                };
            };
        }
    })();
};