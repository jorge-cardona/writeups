# Authby

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 21 allows anonymous access but no useful files are available. After some
attempts, guessed the credentials for the user Administrator `admin:admin`.\
![ftp-files](images/ftp-files.png)

🔎 The `.htpasswd` file contains an encrypted password for the user offsec.\
![htpasswd](images/htpasswd.png)

🔑 Cracking the password with hashcat to reveal the credentials `offsec:elite`.\
![htpasswd-cracked](images/htpasswd-cracked.png)

🔎 Port 242 is protected but it can be accessed by the user offsec. This site
list the files stored in the FTP folder.\
![http-auth](images/http-auth.png)

💀 Using FTP, uploaded a PHP reverse shell[^1] and executed it over port 242 to
get access as apache.\
![php-rshell](images/php-rshell.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

💀 Executing Juicy Potato[^2] using a CLSID for Windows 8[^3] given that the
user has the `SeImpersonatePrivilege` privilege.\
![jp-privesc](images/jp-privesc.png)

🏴 Admin flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://github.com/ivan-sincek/php-reverse-shell
[^2]: https://github.com/ivanitlearning/Juicy-Potato-x86
[^3]: https://ohpe.it/juicy-potato/CLSID/Windows_8.1_Enterprise