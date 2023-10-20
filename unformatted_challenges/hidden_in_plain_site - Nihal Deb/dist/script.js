let mouseX = 0;
let mouseY = 0;

let flashlight = document.getElementById("FL");
const isTouchDevice = () => {
  try {
    document.createEvent("TouchEvent");
    return true;
  } catch (e) {
    return false;
  }
};

function getMousePosition(e) {
  mouseX = !isTouchDevice() ? e.pageX : e.touches[0].pageX;
  mouseY = !isTouchDevice() ? e.pageY : e.touches[0].pageY;

  flashlight.style.setProperty("--Xpos", mouseX + "px");
  flashlight.style.setProperty("--Ypos", mouseY + "px");
};

document.addEventListener("mousemove", getMousePosition);
document.addEventListener("touchmove", getMousePosition);

var login_attempts=3;
    function check_form()
    {
     var name=document.getElementById("name").value;
     var pass=document.getElementById("pass").value;
     if(name=="talkerscode" && pass=="talkerscode")
     {
      alert("SuccessFully Logged In");
      document.getElementById("name").value="";
      document.getElementById("pass").value="";
      window.location.href="https://youtu.be/x3LwHhDD6TY";
     }
     else
     {
      if(login_attempts==0)
      {
       alert("No Login Attempts Available");
      }
      else
      {
       login_attempts=login_attempts-1;
       alert("Login Failed Now Only "+login_attempts+" Login Attempts Available");
       if(login_attempts==0)
       {
        document.getElementById("name").disabled=true;
        document.getElementById("pass").disabled=true;
        document.getElementById("form1").disabled=true;
       }
      }
     }
     
     return false;
    }

/* =========================================================================== */

function swapTiles(cell1,cell2) {
  var temp = document.getElementById(cell1).className;
  document.getElementById(cell1).className = document.getElementById(cell2).className;
  document.getElementById(cell2).className = temp;
}

function shuffle() {
//Use nested loops to access each cell of the 3x3 grid
for (var row=1;row<=3;row++) { //For each row of the 3x3 grid
   for (var column=1;column<=3;column++) { //For each column in this row
  
    var row2=Math.floor(Math.random()*3 + 1); //Pick a random row from 1 to 3
    var column2=Math.floor(Math.random()*3 + 1); //Pick a random column from 1 to 3
     
    swapTiles("cell"+row+column,"cell"+row2+column2); //Swap the look & feel of both cells
  } 
} 
}

function clickTile(row,column) {
  var cell = document.getElementById("cell"+row+column);
  var tile = cell.className;
  if (tile!="tile9") { 
       //Checking if white tile on the right
       if (column<3) {
         if ( document.getElementById("cell"+row+(column+1)).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+row+(column+1));
           return;
         }
       }
       //Checking if white tile on the left
       if (column>1) {
         if ( document.getElementById("cell"+row+(column-1)).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+row+(column-1));
           return;
         }
       }
         //Checking if white tile is above
       if (row>1) {
         if ( document.getElementById("cell"+(row-1)+column).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+(row-1)+column);
           return;
         }
       }
       //Checking if white tile is below
       if (row<3) {
         if ( document.getElementById("cell"+(row+1)+column).className=="tile9") {
           swapTiles("cell"+row+column,"cell"+(row+1)+column);
           return;
         }
       } 
  }
  
}


