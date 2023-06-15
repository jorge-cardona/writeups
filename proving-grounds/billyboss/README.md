# Billy Boss

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 80 is running BaGet a NuGet and symbol sever.\
![baget](images/baget.png)

🔎 Port 8081 is running an instance of Nexus v3.21.0-05.\
![nexus](images/nexus.png)

🔎 This version of Nexus seems vulnerable to Remote Code Execution (RCE),
but authentication is required.\
![searchploit-nexus](images/searchsploit-nexus.png)

🔑 After several attempts found credentials for Nexus `nexus:nexus`.\
![nexus-login](images/nexus-login.png)

💀 Modify the exploit[^1] to drop a netcat binary and initiate a reverse shell 
to get access as billyboss\\nathan.\
![nexus-exploit](images/nexus-exploit.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 The user has granted the `SeImpersonatePrivilege` privilege, which means is
possible to elevate privilege via PrintSpoofer[^2].\
![user-info](images/user-info.png)

🔎 System information.\
![system-info](images/system-info.png)

💀 Choose the right binary, with the previous information, and execute the 
exploit[^3] to spawn a new cmd session as System.\
![printspoofer-exploit](images/printspoofer-exploit.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.exploit-db.com/exploits/49385
[^2]: https://itm4n.github.io/printspoofer-abusing-impersonate-privileges
[^3]: https://github.com/itm4n/PrintSpoofer