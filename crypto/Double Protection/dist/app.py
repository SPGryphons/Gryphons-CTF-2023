from Crypto.Cipher import AES 
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from secrets import token_bytes

flag = b'GCTF23{???}'

def kdf(key):
    for _ in range(5):
        key = SHA256.new(key).digest()
    return key

def secrecy():
    return kdf(token_bytes(2)),kdf(token_bytes(2)),token_bytes(16)

def super_encrypt(buffer, K1, K2, IV):  
    C1 = AES.new(K1,AES.MODE_CBC,IV)
    C2 = AES.new(K2,AES.MODE_OFB,IV)
    ct = C2.encrypt(C1.encrypt(pad(buffer,16))).hex()
    return ct

K1, K2, IV = secrecy()
ct = super_encrypt(flag, K1, K2, IV)

print(f"Double Protection service v1.0\n\nThis is the encrypted flag:\n\nIV = {IV.hex()}\nCT = {ct}\n\nEnter a buffer to encrypt (in hex)\n\n")

try:
    buffer = bytes.fromhex(input('>> '))
    print(f'Plaintext = {buffer.hex()}\nEncrypted = {super_encrypt(buffer,K1,K2,IV)}\n\nGood Luck!')
except:
    print("Not a valid input!")