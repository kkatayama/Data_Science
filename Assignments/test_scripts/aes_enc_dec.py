# coding: utf-8
import base64
from hashlib import sha256
from Crypto.Cipher import AES

# encrypt
key = sha256('gizmo'.encode()).digest()
cipher = AES.new(key, AES.MODE_EAX)
nonce  = cipher.nonce
ciphertext = cipher.encrypt('igWA1FLJR2rEsOYqNep1eOOgy'.encode())

with open('soda_token.key', 'wb') as f:
    f.write(base64.b64encode(key + nonce + ciphertext))

# decrypt
with open('soda_token.key', 'rb') as f:
    raw = base64.b64decode(f.read())
key = raw[:32]
nonce = raw[32:48]
ciphertext = raw[48:]

cipher = AES.new(key, AES.MODE_EAX, nonce)
api_token = cipher.decrypt(ciphertext).decode()
print(api_token)
