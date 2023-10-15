# Solution
This is the solution for the challenge: UTF-9.


## Brief overview
UTF-9 is a modified version of the Unicode Transformation Format (UTF), with 9 bits in a byte instead of 8.
All prefixes are kept (e.g 10...).
As such, the code points will be shifted.
e.g. originally (_ indicates seperation between prefix and content)
```
110_00010 10_100011
```
afterwards
```
110_000001 10_0100011
```


## Note
This has no relation to RFC 4042, although that may be helpful.

## Steps
1. Open the file in the language of your choice and read from it.
2. Iterate through each 9 bits (nonets) in a `while` loop which increments by 9, a counter variable, each time. (or a for loop which increments by 9).
3. Check the first bit of the nonet.
4. Here is the workflow:
```
x is original bits, X is added bits due to extra 1 bit. all x represent the code point's binary sequence.
1 byte: X is 0
0Xxxxxxxx

2 bytes: The code point fills up X2 ordinarily.
110Xxxxxx 10Xxxxxxx

3 bytes: The code point fills up X3, then X2 then X1
1110Xxxxx 10Xxxxxxx 10Xxxxxxx

4 bytes:
11110Xxxx 	10Xxxxxxx 	10Xxxxxxx 	10Xxxxxxx
```
read from next 1 byte
            discard the 1st 3 bits of 1st byte.
            discard the 1st 2 bits of 2nd byte
            discard the 1st 2 bits of 3rd byte
            the remaining bits form the byte sequence, arrange them from MSB to LSB // bitshift can be used
4. (Psuedocode)
note: byte and nonet are used interchangeably and all refer to a 9 bit byte unless explicitly stated otherwise.
if 1st bit is 0, convert the binary of the remaining 8 bits to an integer.
else (the 1st bit is 1):
    check 2nd bit.
    if 2nd bit is 0, throw an error(continuation byte at the 1st nonet)
    else:
        check 3rd bit.
        if 3rd bit is 0:
            read from next 1 byte
            discard the 1st 3 bits of 1st byte.
            discard the 1st 2 bits of 2nd byte
            the remaining bits form the byte sequence, arrange them from MSB to LSB // bitshift can be used
        else:
            check 4th bit.
            if 4th bit is 0:
                read from next 2 bytes
                discard the 1st 3 bits of 1st byte.
                discard the 1st 2 bits of 2nd byte
                discard the 1st 2 bits of 3rd byte
                the remaining bits form the byte sequence, arrange them from MSB to LSB // bitshift can be used
            else:
                check 5th bit.
                if 5th bit is 0:
                    read from next 3 bytes
                    discard the 1st 3 bits of 1st byte.
                    discard the 1st 2 bits of 2nd byte
                    discard the 1st 2 bits of 3rd byte
                    discard the 1st 2 bits of 4th byte
                    the remaining bits form the byte sequence, arrange them from MSB to LSB // bitshift can be used
                else:
                    either ignore or throw an error // because its an undefined condition.

5. A decoding script is provided in the solution/ directory.
6. Join the characters together, and the passphrase will be revealed. (Flag_旗帜_Bendera_கொடி_7d08890)
7. Use it to unlock the zip.
8. The flag file will be inside. (`GCTF23{St@ndaRDs_4R3_FuN!_7dd3449}`)


## Encoding script
An encoding script is provided in the solution/ directory.
It reads from "input" and saves to "output".
