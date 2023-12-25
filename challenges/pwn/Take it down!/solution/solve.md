# Take it down!
`noteinator` given. Two vulnerabilities inside include
1. `gets()` call that creates an overflow
2. `printf()` call that contains a format string vulnerability

NOTE: it is conceptually possible to solve this challenge with `printf()`... I think. However, this will be left as an exercise for the reader.

solve script can be found [here](./exp.py)

The solution involves 2 parts.
1. Leaking the canary
2. Overflowing the buffer + canary to overwrite the return address with address of `win()` function.
