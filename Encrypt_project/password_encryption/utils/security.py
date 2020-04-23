from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class ApiSecurity():
    def __init__(self, key):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"staticsalt", iterations=30,
                         backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(bytes(key, 'utf-8')))
        self.f = Fernet(key)

    def encrypt(self, msg):
        return self.f.encrypt(bytes(msg, 'utf-8'))


    def decrypt(self, enc_msg):
        return self.f.decrypt(bytes(enc_msg, 'utf-8'))

    def hashing(self, hash_pass):
        hashed = pbkdf2_sha256.hash(hash_pass, rounds=200000, salt_size=16)
        return hashed

    def hashing_verify(self, provide_pass, usr_str):
        res = pbkdf2_sha256.verify(provide_pass, usr_str)
        if res:
            return True
        else:
            return False

# as_obj = ApiSecurity()
# hashed_value = as_obj.hashing("admin@890")
# print("11111111111111111111")
# print(hashed_value)
# print("11111111111111111111")
# check_hash = as_obj.hashing_verify(hashed_value)
# print(check_hash)
