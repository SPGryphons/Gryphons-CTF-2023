import websockets.client
import json

URI = "ws://127.0.0.1:1337/ws"

async def solve():
  async with websockets.client.connect(URI) as websocket:
    await websocket.send(json.dumps({
      "type": "get_flag"
    }))
    data = json.loads(await websocket.recv())
    print(data["flag"])


if __name__ == "__main__":
  import asyncio
  asyncio.run(solve())