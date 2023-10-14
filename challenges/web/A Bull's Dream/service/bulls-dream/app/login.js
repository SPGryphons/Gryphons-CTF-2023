function handleLogin() {
    // Get the entered username and password
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Check if the credentials are correct
    if (username === 'DreamyBull' && password === 'Ambatublou') {
        // Call the setCookie function
        var concatenated = username + password
        setCookie("Dcookie", concatenated, 1)

        // Redirect to wasd123.html
        window.location.href = 'wasd123.html';
    } else if (username === 'SPSecretUser' && password === '1qwer$#@!'){
        // Call the setCookie function
        var concatenated = username + password
        setCookie("Scookie", concatenated, 1)
        // Redirect to 321.dsaw.html
        window.location.href = '321dsaw.html'
    }   
    else {
        alert('Invalid credentials. Please try again.');
    }
}

// Attach the function to the form's submit event
document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    handleLogin(); // Call the login function
});

// When the user refreshes the page and triggers the beforeunload
function output(){
    console.log('/H1nt1.html')
}

//set credentials in cookies
function setCookie(name, value, daysToLive){
    const date = new Date()
    date.setTime(date.getTime() + (daysToLive * 24 * 60 * 60 * 1000))
    let expires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${expires};`
}