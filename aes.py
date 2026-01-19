from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
message = b"Hello Secure World"
ciphertext = cipher.encrypt(message)
print("Encrypted:", ciphertext)
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt(ciphertext)
print("Decrypted:", plaintext.decode())
