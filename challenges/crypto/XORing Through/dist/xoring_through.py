from secrets import token_bytes
from hashlib import md5
from Crypto.Util.strxor import strxor
secret = token_bytes(56)
flag = open('original_flag.png','rb').read()
length = len(flag)
blocks = length // 16 + 1
keys = b''
for _ in range(blocks):
    secret = md5(secret).digest()
    keys += secret 
open('flag.png','wb').write(strxor(keys[:length],flag))