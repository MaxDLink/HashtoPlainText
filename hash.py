import hashlib

with open("salt.txt", "r") as f:
  salt = f.read().strip()

hashes = []
with open("example_passwords.txt", "r") as f:
  for line in f:
    # strip new line character
    password = line.strip()
    # concat salt and password, encode to utf-8
    salted_password = (salt + password).encode('utf-8')
    # hash salted password
    hash_value = hashlib.sha256(salted_password).hexdigest()
    hashes.append(hash_value)

for h in hashes:
  print(h)



