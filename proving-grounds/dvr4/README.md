# DVR4

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 8080 is hosting an instance of Argus
Surveillance.\
![argus-home](images/argus-home.png)

🔎 Found two potential users, **Administrator** and **Viewer**.\
![argus-users](images/argus-users.png)

🔎 Argus may be vulnerable to path traversal (CVE-2018-15745).\
![searchploit-argus](images/searchploit-argus.png)

🔎 Testing if the file `Windows\system.ini` is reachable.\
![system-ini.png](images/system-ini.png)

🔑 Could not get the Administrator's SSH key but found the key of the user
Viewer[^1].\
![ssh-key](images/ssh-key.png)

🔎 Accessing the machine as Viewer.\
![viewer-ssh](images/viewer-ssh.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 User groups and privileges.\
![viewer-info](images/viewer-info.png)

🔎 Searchploit results showed that Argus could be vulnerable to Privilege
Escalation. Checking if it's possible to write in the current directory.\
![check-perms](images/check-perms.png)

🔎 Found the encrypted Administrator password in the `DVRParams.ini` file.\
![admin-password](images/admin-password.png)

🔑 Searchploit also indicated a Weak Password Encryption vulnerability in Argus
(CVE-2022-25012). Cracking the Administrator password[^2].\
![cracked-password](images/cracked-password.png)

🔎 Uploading an instance of Netcat.\
![netcat-upload](images/netcat-upload.png)

🔎 Spawning a reverse shell using `runas` and getting access as Administrator.\
![reverse-shell](images/reverse-shell.png)

🏴 Admin flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.bitvise.com/wug-publickey
[^2]: https://github.com/s3l33/CVE-2022-25012/blob/main/CVE-2022-25012.py