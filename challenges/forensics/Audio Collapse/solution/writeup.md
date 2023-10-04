# Solution
1. Play the song, and you may realise a slight audio blip (Or I'm crazy.) compared to the original. This is due to audio steganography.
2. To decode the hidden message, we will be using Wave, a package available in native python.
- The code used
    ```python
    import wave
    import os

    os.chdir('G:\\GCTF\\StegaSound\\dist') #This was used to do final check on the script. Remove if unneccesary for you.

    song = wave.open("song_embedded.wav", mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]

    print("Sucessfully decoded: "+decoded)
    song.close()
    ```
- Change the directory to the one with the wav file or error will occur.
3. If all goes well, the program should dispense out the message hidden inside :D