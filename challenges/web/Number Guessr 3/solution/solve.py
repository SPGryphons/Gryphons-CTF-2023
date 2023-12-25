import json

import randcrack # python -m pip install randcrack
import websockets.client

URI = "ws://127.0.0.1:1337/ws"
N = 1_000_000


def guess(num):
  return json.dumps({"type": "guess", "number": num})


async def solve():

  cracker = randcrack.RandCrack()

  async with websockets.client.connect(URI) as websocket:
    # Submit the guess_id of the first 624 guesses
    print("[*] Getting the Mersenne Twister state...")
    for _ in range(624):
      await websocket.send(guess(1))

      res = json.loads(await websocket.recv())
      cracker.submit(res["guess_id"])

    # Predict the next 100 numbers
    print("[*] Predicting the next 100 numbers...")
    for _ in range(100):
      randbits = cracker.predict_getrandbits(32)
      num = (randbits % N) + 1

      await websocket.send(guess(num))
      res = json.loads(await websocket.recv())
      if res["result"] == "correct":
        print(f"[+] Correct guess: {num}")
      else:
        print(f"[-] Incorrect guess: {num}")
        raise Exception("Incorrect guess")

    while True:
      res = json.loads(await websocket.recv())
      if res["type"] == "flag":
        print(f"[+] Flag: {res['flag']}")
        break


if __name__ == "__main__":
  import asyncio
  asyncio.run(solve())