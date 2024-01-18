# Exfiltrated

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Scan results shows some disallowed paths in `robots.txt`.\
![robots-txt](images/robots-txt.png)

🔎 CMS Subrion v4.2.1 admin panel.\
![admin-panel](images/admin-panel.png)

🔎 This version of Subrion seems to be vulnerable to Arbitrary File Upload
(CVE-2018-19422).\
![searchsploit-subrion](images/searchsploit-subrion.png)

💀 Exploiting the file upload to RCE[^1] to gain access as the `www-data` user.\
![exploit-subrion](images/exploit-subrion.png)

🔎 Found an interesting file at `/opt/image-exif.sh`.\
![image-exif](images/image-exif.png)

🔎 Exiftool may be vulnerable to command injection[^2].\
![exiftool-poc](images/exiftool-poc.png)

🔎 Upgrading to a fully-interactive shell.\
`$ python3 -c “import pty; pty.spawn('/bin/bash')”`

🔎 Attaching a bash reverse shell to a generic image.\
![revshell](images/revshell.png)

💀 Uploading the image and exploiting exiftool's vulnerability to obtain a shell
as `root`.\
![exiftool-exploit](images/exiftool-exploit.png)

🏳 User Flag.\
![user-flag](images/user-flag.png)

🏴 Admin Flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.exploit-db.com/exploits/49876
[^2]: https://ine.com/blog/exiftool-command-injection-cve-2021-22204