# key name = key.key
# secretphrase = "its_hari"

import os
from cryptography.fornet import Fornet

files = []
for file in os.listdir():
  if file == 'main.py' or file == 'keygen.py' or file = "key.key":
    continue
  if os.path.isfile(file):
    files.append(file)

print(files)

key = Fornet.generate_key()

with open('key.key','wb') as thekey:
  thekey.write(key)