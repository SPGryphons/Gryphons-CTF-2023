## Challenge Name
-  PDS Corp
## Challenge Difficulty
- Easy
## Challenge Category
- pwn 
## Challenge Description
PDS Corp has commited war crimes in the Afghanistan war and has commited mass genocide and is in violation of the geneve convetion. Evidence of such wrong doings are on this workstation. We have infiltrated into PDS's Corprate Network (Shitty Firewall) Kindly attack this workstation remotely. (Kindly Use the Included Version of Virtual Box)
# Writeup
Scan Using NMAP and notice Windows 7 SP1 has RDP enabled (Port 3389)
![Alt text](image-1.png)
Use CVE-2019-0708 to attack the machine
![Alt text](image.png)
Look for hidden txt file in system with shell
![Alt text](image-3.png)
![Alt text](image-4.png)
# solution
Attack windows 7 SP1 Machine with CVE-2019-0708(Codenamed BlueKeep) to obtain system level access and find flag through user directory hidden file.

