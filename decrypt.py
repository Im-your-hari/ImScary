import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == 'decrypt.py' or file == 'key.key' or file == 'encrypt.py' or file == 'key.key':
    continue
  if os.path.isfile(file):
    files.append(file)
print(files)

with open('key.key',"rb") as key:
  secretkey = key.read()

secretphrase = "its_hari"

user_phase = input("Enter the key to decrypt your files :: ")

if user_phase == secretphrase:
  for file in files:
    with open(file,'rb') as thefile:
      contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file,'wb') as thefile:
      thefile.write(contents_decrypted)
    print("Your files are decrypted..!")
    
else:
  print("Dont play with me.. Enter the correct secret phase..")
