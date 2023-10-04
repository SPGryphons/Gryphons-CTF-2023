r"""
_____                                    __    _____                          
|  __ \                                  | |  / ____|
| |__) |_ _ ___ _____      _____  _ __ __| | | (___   ___ _ ____   _____ _ __ 
|  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  \___ \ / _ \ '__\ \ / / _ \ '__|
| |  | (_| \__ \__ \\ V  V / (_) | | | (_| |  ____) |  __/ |   \ V /  __/ |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_____/ \___|_|    \_/ \___|_|
"""

import string
import secrets
import time

CHARSET = string.ascii_lowercase + string.digits

password = "".join(secrets.choice(CHARSET) for _ in range(8))


def str_cmp(s1, s2):
  if len(s1) != len(s2):
    return False
  for a, b in zip(s1, s2):
    time.sleep(0.001)
    if a != b:
      return False
  return True


MAX_ATTEMPTS = 3000

attempt = 0

print(__doc__.strip())

while attempt < MAX_ATTEMPTS:
  p = input("Enter password: ")
  if str_cmp(p, password):
    print("Correct!")
    with open("flag.txt") as f:
      print("Flag:", f.read())
    exit(0)
  else:
    print("Incorrect!")
    attempt += 1

print("Too many attempts!")
