# from Crypto.Cipher import AES

# input_value = input()

# key = bytes.fromhex('da1d32181d122d21') # 16진수 -> ascii
# iv = bytes.fromhex('ba7cdeae124s')
# BS = 16
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# raw = pad(input_value)
# cipher = AES.new(key, AES.MODE_CBC, iv)

# output_value = cipher.encrypt(raw).hex()
# print(output_value)

import base64
import hashlib
from Crypto import Cipher
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS-len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]

class AESCipher():
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        message  = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')

    def __iv(self):
        return chr(0) * 16


if __name__=='__main__':
    key = 'helena'
    message = 'hello!'

    aes = AESCipher(key)
    encrypt = aes.encrypt(message)
    decrypt = aes.decrypt(encrypt)

    print(encrypt)
    print(decrypt)