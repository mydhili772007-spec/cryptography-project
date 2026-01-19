import hashlib

text = "Code Red"
hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)
