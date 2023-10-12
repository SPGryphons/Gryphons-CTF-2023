# foreigner
files given
- ALIENWARE
- main.c
- translator
NOTE: `translator` is the compiled version of `main.c`. <br>
We are given a binary that when ran, gives the following output
```
$ ./translator
Welcome!
Enter password: test
Huh???
```
the binary does a few things
1. Read data from `ALIENWARE` file
2. Execute "instructions" based on data in file
3. We have "registers" that store data that we can later operate with. We can only operate with data in the registers. `MOV` is the exception, allowing us to set the values of the registers.

Modifiying the source, we can create a program trace. We can then trace to a `getchar()` call, which I annotated as `SCAN`. I have also annotated the other instructions for a bit more clarity.
```
SCAN 0
test
MOV 1, 0x47
SUB 0, 1 | 116 - 71
JG 0, 3, 37f
IP: 37f
MOV 2, 0x68
MOV 0, 0x48
MOV 3, 0x3f
MOV 1, 0x75
PRINT 0 | H
H
PRINT 1 | u
u
PRINT 2 | h
h
PRINT 3 | ?
?
PRINT 3 | ?
?
PRINT 3 | ?
```
There is a `JGE` jump that compares register `0` and `3`, jumping to `0x37f`. With `MOV 2, 0x68` being the first instruction at the address. Hence, all is left is to work backwards to sastify the cases. In the first case, it's a simple substraction with the character `G`, with a following comparison with `0`. If the number is greater then `0`, the branch is taken. Otherwise, the branch is not taken.

Via modifying the source even more to prevent it from branching, we can create a small disassembler that will allow us to look at what the full program might look like(assuming nothing weird). We then meet this weird pattern that seems to repeat with various different values throughout, all jumping to `0x37f` if the value is > 0.
```
[...]
SCAN 0
MOV 1, 0x01
MOV 2, 0x41
XOR 0, 2 | 65 ^ 65
ADD 0, 1 | 0 + 1
MOV 1, 0x08
SUB 0, 1 | 1 - 8
JG 0, 3, 37f
SCAN 0
MOV 1, 0x51
MOV 2, 0x63
XOR 0, 1 | 65 ^ 81
SUB 0, 2 | 16 - 99
JG 0, 3, 37f
[...]
```
Reversing the operations will then allow the player to get the flag: `GCTF23{sm4ll_1nst_s3ts_are_1if3!}`
