# Hutch

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 88 (Kerberos) indicates that the server is probably an Active Directory
Domain Controller ADDC.

🔎 Port 135 and 445 allows anonymous sessions but no shares are available.

🔎 Port 80 is running an IIS server 10.0 with WebDav enabled.\
![nikto](images/nikto.png)

🔎 Port 389 is using LDAP, looking up the machine's hostname and additional
entries.\
![ldap-hostname](images/ldap-hostname.png)

![ldap-entries](images/ldap-entries.png)

🔑 Found user credentials in LDAP results `fmcsorley:CrabSharkJellyfish192`.\
![user-password](images/user-password.png)

🔎 Checking SMB shares for fmcsorley but only the default ones are available.\
![user-shares](images/user-shares.png)

🔎 Testing if fmcsorley have access to the WebDav console.\
![davtest-run](images/davtest-run.png)

💀 Although all checks fail, it is possible to upload files via WebDav.
Uploading an ASPX reverse shell[^1] to get access as
iis apppool\\defaultapppool.\
![reverse-shell](images/reverse-shell.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 General system information.
![system-info](images/system-info.png)

🔎 The `SeImpersonatePrivilege` privilege indicates that is possible to escalate
privileges by abusing tokens (not tested).\
![user-info](images/user-info.png)

🔎 Notice that LAPS is installed in the system.\
![laps](images/laps.png)

🔑 Dumping LAPS creds[^2] and revealing the Administrator password
`/hIx4.zja;/r$B`.\
![laps-creds](images/laps-creds.png)

🔎 Using port 5985 (WinRM) to access with Administrator credentials.\
![winrm](images/winrm.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://www.darknet.org.uk/2014/12/insomniashell-asp-net-reverse-shell-bind-shell
[^2]: https://www.hackingarticles.in/credential-dumpinglaps/