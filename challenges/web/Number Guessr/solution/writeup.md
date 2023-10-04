# Solution to Number Guessr

- Send a websocket request to the server with the following payload:

```json
{
    "type": "get_flag"
}
```

- The server will respond with the flag.