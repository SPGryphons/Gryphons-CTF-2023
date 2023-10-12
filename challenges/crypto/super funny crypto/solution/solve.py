pwd = [109, 53, 152, 113, 155, 102, 25, 92, 140, 150, 57, 84, 102, 238, 127, 161, 114, 130, 91, 163, 107, 43, 172, 63, 113, 149, 84, 95, 84, 326, 228, 119, 180, 81]
FAKE_PWD = "ariretbaantvirlbhhc"

def random_cipher(s,i): 
  def splitter(s):
    # Split the string into two halves
    s1,s2=s[:len(s)//2],s[len(s)//2:]
    # Interleave the two halves
    return "".join(map(lambda _:"".join(_),zip(s1,s2)))
  # Repeat the cipher i times
  for _ in range(i):
    s = splitter(s)
  return s

def xor(*s):
  # XOR each character in the strings
  return "".join(chr(ord(c)^ord(d)) for c,d in zip(*s))

def base64(s):
  # Base64 encode the string
  import base64
  return base64.b64encode(s.encode("utf-8")).decode("utf-8")


import random
_random = random.Random()

_random.seed(286984)
# _random.seed(19**4*2 + 19**3*3 + 19*(19**2 - 19*3 - 1) + 8)

shifts = [_random.randint(0, _random.randint(64, 256)) for _ in range(len(pwd))]
_random.shuffle(shifts)
b = "".join(chr(pwd[i] - shifts[i]) for i in range(len(pwd)))
a = xor(b, base64(FAKE_PWD*2))
rotations = _random.randint(1, 100)

# For our flag, the cipher has a period of 10
# So we just do the encryption to the nearest multiple of 10
rotations = 10 - (rotations % 10)
print(random_cipher(a, rotations))