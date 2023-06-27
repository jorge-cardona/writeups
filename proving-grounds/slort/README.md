# Slort

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Ports 21 (ftp) and 445 (smb) don't allow anonymous connections.\
![ftp-anon](images/ftp-anon.png)

![smb-anon](images/smb-anon.png)

🔎 Ports 4443 and 8080 are running an instance of XAMPP.\
![xampp-dashboard](images/xampp-dashboard.png)

🔎 The contents of `phpinfo.php` are exposed.\
![phpinfo](images/phpinfo.png)

🔎 Found some interesting folders using FFUF.\
![ffuf-scan](images/ffuf-scan.png)

🔎 The resource `/site` redirects to a website.\
![slort-site](images/slort-site.png)

🔎 Seems vulnerable to Local File Inclusion (LFI).\
![lfi-test](images/lfi-test.png)

🔎 And Remote File Inclusion (RFI) as well.\
![rfi-test](images/rfi-test.png)

💀 Execute a PHP reverse shell[^1] hosted with Python to get access as rupert.\
![php-revshell](images/php-revshell.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 User information.\
![user-info](images/user-info.png)

🔎 System information.\
![system-info](images/system-info.png)

🔎 In `C:\Backup` there's a file indicating that `TFTP.EXE` is running every 5
minutes.\
![backup-info](images/backup-info.png)

🔎 Checking file permissions shows that the user has full access.\
![file-perms](images/file-perms.png)

💀 Replaced the `TFTP.EXE` file with a reverse shell generated with MSF to get
access as System.\
![msf-revshell](images/msf-revshell.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://github.com/ivan-sincek/php-reverse-shell