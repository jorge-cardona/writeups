# Algernon

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 21 allows anonymous access.\
![ftp-dirlisting](images/ftp-dirlisting.png)

🔎 Download all files to search for usernames and passwords.\
![grep-creds](images/grep-creds.png)

🔎 Port 9998 is running a web server with SmarterMail.\
![smartermail-login](images/smartermail-login.png)

🔎 SmarterMail seems vulnerable to RCE[^1].\
![searchsploit-sm](images/searchsploit-sm.png)

🔎 The build number is below the build required for the exploit (6985).\
![smatermail-build](images/smartermail-build.png)

💀 Modify and run the exploit to get access as System.
```python
HOST='192.168.159.65'
PORT=17001
LHOST='192.168.49.159'
LPORT=80
```
![smartermail-exploit](images/smartermail-exploit.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.exploit-db.com/exploits/49216