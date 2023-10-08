1. Starts off at the login page
2. View page source to see a 'beforeunload' eventlistener
3. Open the console and spam refresh the page to reveal a '/H1nt1.html' path being output everytime your refresh the page.
4. Visit /H1nt1.html to find a corrupted Image file.
5. Use any hex editor tool to fix the hex headers to 'FFD8' (jpg file format) to fix the image.
6. Image reveals the username and a hint to the path /dreamybull.html
7. /dreamybull.html presents with another image. Image hints a text hidden within it
8. Download the image and view it with a notepad and scroll all the way down to find a base64 encoded message at the end.
8. Decode the message to find the password.
9. Login with the username and password
10. Once logged in, solve the riddle. Answer is "echo" or "an echo" (not case sensitive) to obtain an AES key
11. View localstorage to find the encrypted message and with which cipher mode
12. Use any online or offline tool to decrypt the meessage to find another pair of login credentials
13. After logging in with new credentials, find the flag by highlighting around the page. It is hidden in 3 places:
	- Above the congratulations message
	- middle right of the page
	- All the way bottom left side of the page
Or they can Ctrl-F 'GCTF23'