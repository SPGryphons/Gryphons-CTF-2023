# Solution
Here is the solution for the challenge: Droid's Login.
The application APK distributed is identical to the challenge "Droid's Toolbox"; they are a 2 part challenge together.
However, participants may choose to solve either first.

## Steps

1. Download the APK and install it on a device.

2. You will be presented with this login screen.
![Login screen](login.png)

3. To gain access to credentials, we shall decompile the application.
Use [Dex2Jar](https://github.com/pxb1988/dex2jar) to get a JAR file from the APK.
Afterwards, you can use a JAR disassembler like [Procyon](https://github.com/mstrobel/procyon) to dump the JAR classes as text files in your directory. This will produce readable Java files we can read. Open this directory in the editor of your choice.
Alternatively, you may use [JADX](https://github.com/skylot/jadx).
> [!NOTE]
> The application is written in Kotlin and compiled to the Android JVM.

Sample CLI output:
```bash
cheezihanlucius on czluciusPC.local code/challc/gctf
❯ d2j-dex2jar.sh droid-toolbox.apk
dex2jar droid-toolbox.apk -> ./droid-toolbox-dex2jar.jar


cheezihanlucius on czluciusPC.local code/challc/gctf
❯ java -jar procyon-decompiler-0.6.0.jar droid-toolbox-dex2jar.jar -o droid-toolbox
Decompiling android/support/v4/app/INotificationSideChannel...
Decompiling android/support/v4/os/IResultReceiver...
Decompiling android/support/v4/os/ResultReceiver...
Decompiling androidx/activity/ActivityViewModelLazyKt...
Decompiling androidx/activity/Api19Impl...
Decompiling androidx/activity/Api26Impl...
Decompiling androidx/activity/Cancellable...
Decompiling androidx/activity/FullyDrawnReporter...
Decompiling androidx/activity/FullyDrawnReporterKt...
Decompiling androidx/activity/FullyDrawnReporterOwner...
Decompiling androidx/activity/OnBackPressedCallback...
Decompiling androidx/activity/OnBackPressedDispatcher...
Decompiling androidx/activity/OnBackPressedDispatcherKt...
Decompiling androidx/activity/PipHintTrackerKt...

```

4. The app package name is `dev.czlucius.gctf23challenge`, so we shall navigate to `<path>/dev/czlucius/gctf23challenge`
In `MainActivity.java`, there is this line (somewhere around line 40):
```java
if (Intrinsics.areEqual(string, "@dmin") && Intrinsics.areEqual(string2, "f62264b387396e88b28766bbf5bbe8ec5623")) {
```
We can see that the username is `@dmin` and the password is `f62264b387396e88b28766bbf5bbe8ec5623`.
Using this, we can log in to the application.

5. The flag is GCTF23{f62264b387396e88b28766bbf5bbe8ec5623}
