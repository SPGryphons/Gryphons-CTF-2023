# Solution to Knockoff Pastebin 2

1. Notice that the `/api/login` endpoint sends a request to the `/otp/verify` endpoint to verify the OTP. It gets the URL to do so via `request.root_url`. This attribute is vulnerable to being changed by setting the `host` header. Additionally, if no `password` is sent to the `/api/login` endpoint, it will not check for the correct password.
2. There are 2 ways for us to gain access to the admin's account:
  - Setup our own web server that returns `{"success": True}` when `/otp/verify` is requested. Then, we can set the `host` header to our server's IP address and port. This way we can login without needing the OTP.
  - Use a webhook service like [webhook.site](https://webhook.site) to capture the request sent to `/otp/verify` and then set the `host` header to the webhook URL. This way we can get the OTP secret and generate our own OTPs.
3. Open the paste to get the flag.