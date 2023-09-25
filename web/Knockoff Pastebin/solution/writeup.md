# Solution to Knockoff Pastebin

1. Register an account on the site. You'll be redirected to a page with a link to your profile.
2. Notice that the JWT code reads the `kid` field to determine the path to the token's secret. This code is vulnerable to path traversal.
3. Create a paste with a random 32 byte string, e.g. `2ae4515a8dee9c62ad6d0976775641c455ef7cef29f62ac37be21ef1bc15319f`.
4. You will be redirected to a page with a link to your paste. The link will be of the form `http://example.com/paste/<user_id>/<paste_id>`.
5. Modify your JWT token's `kid` field to `../uploads/<user_id>/<paste_id>`, and `admin` to `true`. Sign it with the string you used in step 3.
6. Refresh the page after setting the cookie. If you did it correctly, you will be on the same page, else you would've been redirected to the login page.
7. The `/raw` endpoint is vulnerable to path traversal when you are an admin. There is a filter that prevents you from reading the flag.
8. Notice that the Flask server is running with debug mode on. Which means we can use the `console` endpoint to execute arbitrary code.
9. Get the needed info to generate the console PIN from the following urls:
- `http://example.com/raw/..%252F..%252Fproc/net/arp (Get the network interface name)`
- `http://example.com/raw/..%252F..%252Fsys/class/net/*/address ("*": network interface name, Get the MAC address)`
- `http://example.com/raw/..%252F..%252Fproc/sys/kernel/random/boot_id (Get the boot ID)`
- `http://example.com/raw/..%252F..%252F/proc/self/cgroup (Only take the part after the last slash in the first line)`
10. Put in the strings obtained in [here](./get_key.py) and run it. You should get the console PIN.
11. Enter the PIN in the console and execute the following code:
```python
print(open('/flag.txt').read())
```

### Disclaimer: Once they get access to the console, they can basically do anything, as such, this challenge might go down frequently.