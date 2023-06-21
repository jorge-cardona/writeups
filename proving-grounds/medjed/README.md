# Medjed

### Port Scan
![port-scan-1](images/port-scan-1.png)
![port-scan-2](images/port-scan-2.png)

## Procedure
🔑 Port 8000 contains an unfinished configuration wizard for barracudadrive 6.5.
Created an Administrator account.\
![conf-wizard](images/conf-wizard.png)

🔎 This version of BarracudaDrive appears to be vulnerable to Privilege
Escalation.\
![searchsploit-barracuda](images/searchsploit-barracuda.png)

🔎 BarracudaDrive enables WebDAV with `r/w` access rights.\
![webdav-barracuda](images/webdav-barracuda.png)

🔎 Access WebDAV with the account previously created.\
![webdav-access](images/webdav-access.png)

🔎 Found XAMPP installation serving a web page on port 45332, which allows to
access files in the web server root.\
![listening-ports](images/listening-ports.png)

![webpage](images/webpage.png)

💀 Uploaded a reverse shell[^2] to `htdocs` using WebDAV and executed it through
the web server to get access as medjed/jerren.\
![reverse-shell](images/reverse-shell.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 System information.\
![sys-info](images/sys-info.png)

💀 Generating and uploading a reverse shell to exploit the PrivEsc[^1]
identified earlier. Followed the steps, and after reboot received a connection
from the machine as System.\
![msfvenom-payload](images/msfvenom-payload.png)
![privesc-exploit](images/privesc-exploit.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.exploit-db.com/exploits/48789
[^2]: https://github.com/ivan-sincek/php-reverse-shell