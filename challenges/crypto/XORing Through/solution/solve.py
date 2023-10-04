from hashlib import md5
from Crypto.Util.strxor import strxor

enc_flag = open("flag.png",'rb').read()
enc_header = enc_flag[:16]
kpa = bytes.fromhex('89504e470d0a1a0a0000000d49484452')
secret = strxor(kpa,enc_header)
blocks = len(enc_flag) // 16
keys = b'' + secret

for _ in range(blocks):
    secret = md5(secret).digest()
    keys += secret 
solved = strxor(keys[:len(enc_flag)],enc_flag)
open('solved.png','wb').write(solved)