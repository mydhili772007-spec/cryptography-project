from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(b"Secret Message")

print("Encrypted:", encrypted)

cipher_dec = PKCS1_OAEP.new(key)
decrypted = cipher_dec.decrypt(encrypted)

print("Decrypted:", decrypted.decode())
