# Droid's Toolbox
Droid always keeps his keys securely, can you find a way to use them?

Tip: This challenge requires an Android device. If you do not have one, you can use the emulator on Android Studio, or you can use GenyMotion.


## Summary
- **Author:** Lucius Chee Zihan
- **Discord Username:** lcz5
- **Category:** Misc
- **Difficulty:** Hard

## Hints
- `Decompile the APK. You can try jadx, or dex2jar+procyon` (100 points)
- `The flag is encrypted with 2048-bit RSA.` (50 points)
- `Android's keystore is built to be secure, don't try to extract any keys from a modern device; it probably won't work` (110 points)
- `Have you thought of the application signature?` (200 points)

## Files
- [`droid-server-dist.zip`](dist/droid-server-dist.zip)
- [`droid_toolbox.apk`](dist/droid_toolbox.apk)


## Services
- [`droid-toolbox-server`](service/droid-toolbox-server) (port 10083)


## Flags
- `GCTF23{AndR01D_Is_S0_Fun!_f9fee49985}` (static)
