Solution Write-up for The Hidden past of WebSecure Inc.
1. Robotic Assistance - Unearthing the Hidden Paths
By accessing http://localhost:3000/robots.txt, we discovered paths that are disallowed for web crawlers. Among the listed paths, one particular entry caught our eye: /hidden-dir/.

2. Obscure Entrances - JWT Authentication Bypass
Upon navigating to /hidden-portal/, we're greeted with a login page that hinted towards JWT authentication.
Ctf players can then use tools such as hydra to brute force this login page that will allow them to login and see their jwt token.

Using tools like jwt.io, players can then decode the JWT token.
The payload showed {"user": "admin", "elevatedPrivileges": false}
To bypass this control and change the elevatedPrivileges to True, we need to re-encoded the JWT with a modified payload, setting "elevatedPrivileges" to "true". This will allow players access to the admin panel where the flag will be given.

3. Decoding the Past - .git Exposure
From the hint given, players need to start searching for .git repositories and find that http://localhost:3000/.git/ is exposed.

Using tools like GitTools, players need to clone the entire .git repository.
And then using standard git commands like "git log", and "git show <commit_id>", players will then find one commit where the secret key is accidentally added but then removed.
4. JWT Manipulation - Privilege Escalation
Inside the admin panel, if you access it without any jwt tokens, an error will be shown. A invalid jwt token will also throw an error.
Players then need to re-encode the jwt token using the secret key and with the correct information {"user": "admin", "elevatedPrivileges": "true"}.
After getting the new jwt token, use tools such as postman/burpsuite to load a new request to /admin-panel using the token and then the flag will be shown.

Challenge complete