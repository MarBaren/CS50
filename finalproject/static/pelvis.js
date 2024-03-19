// Get all elements with class="closebtn"
var close = document.getElementsByClassName("closebtn");
var i;

// Loop through all close buttons
for (i = 0; i < close.length; i++) {
  // When someone clicks on a close button
  close[i].onclick = function(){

    // Get the parent of <span class="closebtn"> (<div class="alert">)
    var div = this.parentElement;

    // Set the opacity of div to 0 (transparent)
    div.style.opacity = "0";

    // Hide the div after 600ms (the same amount of milliseconds it takes to fade out)
    setTimeout(function(){ div.style.display = "none"; }, 400);
  }
}

function toggleFill(element) {
    // Toggle de kleur van het pictogram


    // Haal het woord op dat moet worden opgeslagen
    var word = element.dataset.word;


    // Haal de huidige status van het pictogram op
    var fillStatus = element.dataset.fill;

    // Toggle de 'FILL' waarde op basis van de huidige staat
    if (fillStatus == 1) {
        element.style.fontVariationSettings = "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24";
        element.dataset.fill = 0;
        fillStatus = 0;

    } else {
        element.style.fontVariationSettings = "'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24";
        element.dataset.fill = 1;
        fillStatus = 1;
    }

    // Stuur een AJAX-verzoek naar de server om de favoriet te schakelen
    toggleFavorite(word, fillStatus);
}

function toggleFavorite(word, fillStatus) {
    // Stuur een AJAX-verzoek naar de server om de favorietstatus te schakelen
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/information", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Verzoek is succesvol verwerkt
            console.log("Favorite toggled successfully");
        }
    };
    xhr.send(JSON.stringify({ word: word, fillStatus: fillStatus }));
}



function show(elementId) {
    document.getElementById(elementId).style.display = "block";
}

function hide(elementId) {
    var element = document.getElementById(elementId)
    element.style.display = "none";
}

function blurr(elementId) {
    var element = document.getElementById(elementId)
    element.style.filter = "blur(3px)";
}

function notblurr(elementId) {
    var element = document.getElementById(elementId)
    element.style.filter = "blur(0px)";
}

function backgroundIn(elementId) {
    var element = document.getElementById(elementId);
    element.style.filter = "brightness(0.5)";
    element.style.boxShadow = "0px 12px 16px 0px rgba(0,0,0,0.50), 0px 17px 50px 0px rgba(0,0,0,0.19)";
}

function backgroundOut(elementId) {
    var element = document.getElementById(elementId);
    element.style.boxShadow = "0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19)";
}

function out(elementId) {
    var element = document.getElementById(elementId);
    element.style.filter = null;
}




document.addEventListener("DOMContentLoaded", function() {
    var queryString = new URLSearchParams(window.location.search);
    console.log(queryString);
    var urlParams = new URLSearchParams(queryString);


    var videoUrl = urlParams.get('video');

    var videoElement = document.getElementById('myVideo');
    videoElement.src = videoUrl; // Zorg ervoor dat de video bestaat in dezelfde map
});


