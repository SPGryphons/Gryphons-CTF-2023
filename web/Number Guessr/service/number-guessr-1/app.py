from random import Random

from quart import Quart, send_file, websocket

app = Quart(__name__)


@app.route("/")
async def index():
  return await send_file("index.html")


@app.websocket("/ws")
async def ws():
  try:
    rand_obj = Random()
    score = 0
    while True:
      data = await websocket.receive_json()

      if data["type"] == "guess":
        guess = int(data["number"])
        num = rand_obj.randint(1, 100)
        if guess == num:
          score += 1
          result = "correct"
        else:
          score = 0 
          result = "incorrect"

        await websocket.send_json({
          "type": "guess_result",
          "number": num,
          "result": result,
          "score": score
        })

      elif data["type"] == "get_flag":
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