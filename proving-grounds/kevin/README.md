# Kevin

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 80 is running a web server hosting HP Power Manager 4.2 (Build 7).\
![web-server](images/web-server.png)

🔎 Port 445 appears to be vulnerable to CVE-2017-0144 (MS17-10 EternalBlue).\
![nmap-smb](images/nmap-smb.png)

🔎 Couldn't execute the exploit[^1], seems that there isn't an available named
pipe for anonymous sessions.\
![autoblue-exploit](images/autoblue-exploit.png)

🔎 HP Power Manager is vulnerable to Buffer Overflow (CVE-2009-2685).\
![searchsploit-hp](images/searchsploit-hp.png)

💀 Exploit CVE-2009-2685[^2] to gain access as System.\
![hp-exploit](images/hp-exploit.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://github.com/3ndG4me/AutoBlue-MS17-010
[^2]: https://www.exploit-db.com/exploits/10099