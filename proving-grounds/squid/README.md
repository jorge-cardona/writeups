# Squid

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Scan results shows a `http-proxy` running on port 3128. Checking additional
ports on localhost using Spose[^1] through the proxy.\
![spose-scan](images/spose-scan.png)

🔎 Accessing port 8080 on localhost by configuring FoxyProxy[^2] to use the
server's proxy. Found `Wampsever` instance.\
![wamp-server](images/wamp-server.png)

🔎 The `phpinfo` page and **phpMyAdmin** console are exposed.\
![phpinfo](images/phpinfo.png)
![phpmyadmin](images/phpmyadmin.png)

🔑 Accessing **phpMyAdmin** default credentials `root:[no pass]`.\

💀 Executing a query to generate a web shell in `C:/wamp/www`[^3].\
![Winchell-query](images/webshell-query.png)

🔎 Running commands in the machine as System.\
![Winchell-whim](images/webshell-whoami.png)

🔎 Uploaded a Net Cat binary and spawned a reverse shell as System.\
![upload-tact](images/upload-netcat.png)
![reverse-shell](images/reverse-shell.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)

### References
[^1]: https://github.com/aancw/spose
[^2]: https://getfoxyproxy.org/
[^3]: https://www.hackingarticles.in/shell-uploading-web-server-phpmyadmin/