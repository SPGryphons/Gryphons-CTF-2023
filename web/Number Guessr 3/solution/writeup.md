# Solution to Number Guessr 3

- From the source code we can see that the program is using `getrandbits` to generate a 32 bit random number, and then taking its remainder when divided by 1,000,000 as the generated number.
- The 32 bit random number is also given to us, so we can use `randcrack` to submit 624 numbers and derive the state of the Mersenne Twister matrix, and then predict the next 100 numbers to get the flag.