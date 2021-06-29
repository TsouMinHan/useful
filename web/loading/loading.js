function loading() {
    let blockUI = document.createElement("div");
    blockUI.setAttribute("class", "mask");
    blockUI.setAttribute("id", "loading");

    let img = document.createElement("img");
    img.setAttribute("src", "./static/img/loading-icon-animated-gif-9.jpg");

    blockUI.appendChild(img);
    document.body.appendChild(blockUI);
}

function finish() {
    let blockUI = document.querySelector("div[id='loading'][class='mask']");
    blockUI.remove();
}
