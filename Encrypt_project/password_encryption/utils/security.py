
from passlib.hash import pbkdf2_sha256

class ApiSecurity():
    def __init__(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def hashing(self):
        hashed = pbkdf2_sha256.hash("password", rounds=200000, salt_size=16)

        return hashed

    def hashing_verify(self):
        res = pbkdf2_sha256.verify("password", hash)
        return res