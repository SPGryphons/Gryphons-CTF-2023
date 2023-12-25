from random import Random

from quart import Quart, send_file, websocket


N = 1_000_000

app = Quart(__name__)


@app.route("/")
async def index():
  return await send_file("index.html")


@app.websocket("/ws")
async def ws():
  try:
    random = Random()
    score = 0
    while True:
      data = await websocket.receive_json()

      if data["type"] == "guess":
        randbits = random.getrandbits(32)
        num = (randbits % N) + 1

        guess = int(data["number"])
        if guess == num:
          score += 1
          result = "correct"
        else:
          score = 0 
          result = "incorrect"

        await websocket.send_json({
          "type": "guess_result",
          "guess_id": randbits,
          "number": num,
          "result": result,
          "score": score,
        })

        if score >= 100:
          with open("flag.txt") as f:
            flag = f.read()
          await websocket.send_json({
            "type": "flag",
            "flag": flag
          })
  
      else:
        await websocket.send_json({
          "type": "error",
          "message": "Invalid message type"
        })

  finally:
    await websocket.close(1000)