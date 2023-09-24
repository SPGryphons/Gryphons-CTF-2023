# This is the encrypted flag:

# IV = ad783339ad3a9d5dad5872cd5a3e38ae
# CT = 126cd563ff7956eecf5b9149e562acf6282e0e43dbdcd3d98cd12a8458181104f93b179907c5962d872bff8b66175348

# Enter a buffer to encrypt (in hex)

# >> ff
# Plaintext = ff
# Encrypted = 796d2d1591ec6e917da6487960487d6d

flag = bytes.fromhex('126cd563ff7956eecf5b9149e562acf6282e0e43dbdcd3d98cd12a8458181104f93b179907c5962d872bff8b66175348')
IV = bytes.fromhex('ad783339ad3a9d5dad5872cd5a3e38ae')
CT = bytes.fromhex('796d2d1591ec6e917da6487960487d6d')

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Hash import SHA256
from Cryptodome.Util.number import long_to_bytes as ltb
cts = []
keys = []

def encrypt(buffer,K1,IV):
    C1 = AES.new(K1,AES.MODE_CBC,IV)
    return C1.encrypt(pad(buffer,16))

def decrypt(buffer,K2,IV):
    C2 = AES.new(K2,AES.MODE_OFB,IV)
    return C2.decrypt(buffer)

def kdf(key):
    for _ in range(5):
        key = SHA256.new(key).digest()
    return key

for i in range(2**16):
    key = kdf(ltb(i,2))
    cts.append(encrypt(b'\xff',key,IV))
    keys.append(key)

print('2^16 operation done')

for j in range(2**16):
    key = kdf(ltb(j,2))
    candidate = decrypt(CT,key,IV)
    if candidate in cts:
        K1 = keys[cts.index(candidate)]
        K2 = key
        print(f'Key 1 = {K1.hex()}\nKey 2 = {K2.hex()}')
        C1 = AES.new(K1,AES.MODE_CBC,IV)
        C2 = AES.new(K2,AES.MODE_OFB,IV)
        print(unpad(C1.decrypt(C2.decrypt(flag)),16).decode())
        break