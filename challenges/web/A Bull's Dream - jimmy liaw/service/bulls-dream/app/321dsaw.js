// Authenticates user
function getCookie(){
  const cDecoded = decodeURIComponent(document.cookie);
  const cArray = cDecoded.split("; ")

  for (i = 0; i < cArray.length; i++){
    const arrayElement = cArray[i].split("=")
    const name = arrayElement[0]
    const value = arrayElement[1]
    if (name === "Scookie") {
      if (value === "SPSecretUser1qwer$#@!") {
        return true
      } else {
        break;
      }
    }
  }
}

if (!getCookie()){
  alert('ByeBye')
  window.location.href = "login.html"
}

function createDiv(position, left, top, right, bottom, text) {
  const div = document.createElement("div");
  div.style.position = position;
  div.style.color = "white";
  div.textContent = text;

  // Set positioning attributes based on provided values
  if (position === "absolute") {
      if (left !== undefined) div.style.left = left;
      if (top !== undefined) div.style.top = top;
      if (right !== undefined) div.style.right = right;
      if (bottom !== undefined) div.style.bottom = bottom;
  }

  document.body.appendChild(div);
}

// Add the div elements when the webpage is opened
createDiv("absolute", "100px", undefined, undefined, "-2500px", "GCTF23{Not_The_Real_Flag}");
createDiv("absolute", "100px", "0px", undefined, "0px", "GCTF23{Not_The_Real_Flag}");
createDiv("absolute", undefined, "1250px", "0", undefined, "GCTF23{Not_The_Real_Flag}");
createDiv("absolute", undefined, undefined, "0", "-2500px", ".");


