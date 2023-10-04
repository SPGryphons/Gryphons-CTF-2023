import websockets.client
import json

URI = "ws://127.0.0.1:1337/ws"


def guess(num):
  return json.dumps({"type": "guess", "number": num})


async def solve():
  async with websockets.client.connect(URI) as websocket:
    await websocket.send(guess(1))

    for _ in range(100):
      res = json.loads(await websocket.recv())
      num = res["next_number"]

      await websocket.send(guess(num))

    while True:
      res = json.loads(await websocket.recv())
      if res["type"] == "flag":
        print(res["flag"])
        break


if __name__ == "__main__":
  import asyncio
  asyncio.run(solve())