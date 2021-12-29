import binascii, os
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
#get the encrypted key
x=open(os.environ['HOME'] +'/Desktop/plain','rb')
hexval=x.read()
#convert the key from hex to bytes
enckey=binascii.unhexlify(hexval)
#import the private key
server_key = RSA.import_key(open('private.pem').read(), passphrase="123456")
decryptorRSA = PKCS1_OAEP.new(server_key)
# decrypt the key and write the result as hex in a file named key
deckey=decryptorRSA.decrypt(enckey)
print(deckey)
f=open(os.environ['HOME'] + '/Desktop/key','wb')
f.write(binascii.hexlify(deckey))
f.close()