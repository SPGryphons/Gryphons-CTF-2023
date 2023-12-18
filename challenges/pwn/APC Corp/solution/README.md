## Challenge Name
-  APC Corp
## Challenge Difficulty
- Easy
## Challenge Category
- pwn 
## Challenge Description
We have infiltrated into APC corp network, we would like to take over APC corp's domain controller, could you help us find a user with comprimised password?




# Writeup
Using nmap to scan machine and realising it is a DC (LDAP,kpassword5)
![Alt text](image.png)
Using Metasploit to attack machine using ZeroLogon
![Alt text](image-1.png)
Scanning host to check for netbios name
![Alt text](image-2.png)
Adding name into msf to set the exploit into action
![Alt text](image-3.png)
![Alt text](image-4.png)
Once Done, use secretsdump.py (impacket) to export password hashes
![Alt text](image-5.png)
Use Crackstation to find weak password
![Alt text](image-6.png)
Use RDP (TCP 3389) to connect to Domain Controller (DC) using the stolen credentials
![Alt text](image-7.png)
Find the Hidden flag inside of user's folder
![Alt text](image-8.png)
# solution
Attack windows server 2019 with CVE-2020-1472 to dump NTLM hash and use crackstation to determine user3 password and sign in using remote desktop and find flag through user directory hidden file

