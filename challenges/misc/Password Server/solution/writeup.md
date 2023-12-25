# Solution to Password Server

1. Find the timing attack vunlerability in the `str_cmp` function
2. Measure the time taken for each character in the password and the character that takes the longest is the correct one
3. Repeat for each character in the password
4. Crack the password