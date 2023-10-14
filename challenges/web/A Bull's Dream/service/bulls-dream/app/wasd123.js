// Authenticates user
function getCookie(){
  const cDecoded = decodeURIComponent(document.cookie);
  const cArray = cDecoded.split("; ")

  for (i = 0; i < cArray.length; i++){
    const arrayElement = cArray[i].split("=")
    const name = arrayElement[0]
    const value = arrayElement[1]
    if (name === "Dcookie") {
      if (value === "DreamyBullAmbatublou") {
        return true
      } else {
        break;
      }
    }
  }
}

if (!getCookie()){
  window.location.href = "login.html"
}

localStorage.setItem("ECB","kbFP760fEH2CLKQ1GAj+29bwfsg+QNgouEMq58R22VKvrsZ0IDJNEqUHWyGG86q/")
document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    var form = document.getElementById("RiddleForm");
  
    // Add a submit event listener
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission
  
      // Get the input value
      var answerInput = document.getElementById("answer");
      var inputValue = answerInput.value.toLowerCase(); // Convert input to lowercase
  
      // Get the output element
      var outputElement = document.getElementById("output");
  
      // Check if the input is correct
      if (inputValue === "echo" || inputValue === "an echo") {
        // Display key if the input is correct
        outputElement.textContent = "AESSecretKey: INeedMoreBoulets";
      } else {
        // Display a message for other inputs
        outputElement.textContent = "Try again!";
      }
    });
  });