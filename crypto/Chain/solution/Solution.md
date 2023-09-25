## CTF Challenge: Chain

### Overview:
"Chain" is a multi-layered cryptography challenge where participants must decode a series of encrypted messages. Each decrypted message provides a hint for the next cipher technique, creating a chain of cryptographic puzzles.

### Challenge Details:

**Initial CipherText**:a2V5OkRPTlRVU0VWSUdFTkVSRSBtZXNzYWdlOkwgTCBrdmxid2ggRCBsb2hhJ3ggeW1ncyBnYWNrIG96ZyBvcmZtdWkgZCBmbmJmIHhpaWtrIC4gWHVpaWkndiBnYiB5eW8gbWkgQW9ydGVnc3VzISB7SsK3csK3WlNFSlFYV0dLdnBzb3IsWk4yey1aTS1BS1ZJRk0tRkxRfXp5d1czVVItQy1WT30=

**Hints**:

1. The presence of the `=` sign at the end suggests Base64 encoding.
2. The decoded message contains a key suggesting the use of the Vigenère cipher.
3. The decrypted message from the Vigenère cipher hints at the Rail Fence cipher.

### Solution:

1. **Base64 Decoding**:
   Decode the initial CipherText using Base64 to get:
key:DONTUSEVIGENERE message:Zvrky svz irp glv vdwy yyfgza or Fmekddbky? A fpzoiq xyi vspkyl mi wti. {J·c·WEDCVKMLKztver,KK2{-LL-TPIYKM-JPT}pyhT3GQ-V-AB}

2. **Vigenère Cipher**:
Using the Vigenère cipher with the key `DONTUSEVIGENERE`, decrypt the message to obtain:

Where are all the rail fences in Singapore? I buried the secret in one. {W·y·FAAOIRSTGelpae,GT2{-HI-FCPESI-OHN}lldC3CN-H-NI}

3. **Rail Fence Cipher**:
Apply the Rail Fence cipher on the decrypted message to reveal the final solution:
Well played, GCTF23{A-CHAIN-OF-CIPHERS-IS-NOTHING}

### Conclusion:
 Each step is designed to lead to the next, the hints
are pretty obvious but tests the participant's knowledge
of ciphers.
