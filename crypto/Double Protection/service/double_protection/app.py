from Crypto.Cipher import AES 
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from secrets import token_bytes
from flag import flag
import socketserver as ss

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

class TcpHandler(ss.BaseRequestHandler):
    def handle(self) -> None:
        print(f"[+] connection established : {self.client_address}")
        try:
            self.request.settimeout(8)
            K1, K2, IV = secrecy()
            ct = super_encrypt(flag,K1,K2,IV)
            self.request.send(f"Double Protection service v1.0\n\nThis is the encrypted flag:\n\nIV = {IV.hex()}\nCT = {ct}\n\nEnter a buffer to encrypt (in hex)\n\n>> ".encode())
            
            try:
                buffer = self.request.recv(1024).strip().decode()
                candidate = bytes.fromhex(buffer)
                self.request.send(f'Plaintext = {buffer}\nEncrypted = {super_encrypt(candidate,K1,K2,IV)}\n\nGood Luck!'.encode())
                self.request.close()
                print(f"[-] connection terminated  : {self.client_address}")
            except:
                self.request.send(b"Not a valid input!")
                self.request.close()
                print(f"[-] connection terminated  : {self.client_address}")
        except:
            print(f"[X] vv i think something went wrong? vv")
            print(f"[-] connection terminated  : {self.client_address}")

if __name__ == "__main__":
    HOST, SOCKETPORT = "0.0.0.0", 1337
    print(f"[?] hosting server at: {HOST}:{SOCKETPORT}")
    server = ss.ThreadingTCPServer((HOST,SOCKETPORT),TcpHandler)
    server.serve_forever()

