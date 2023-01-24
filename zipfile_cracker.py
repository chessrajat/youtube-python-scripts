import zipfile
from tqdm import tqdm

# initilise our zip file
input_file = "./files/input/confidentail.zip"
wordlist_file = "./files/wordlists/rockyou.txt"

zip_file = zipfile.ZipFile(input_file)
# get count of number of passwords in wordlist

file = open(wordlist_file, "rb")
passwords_count = len(list(file))
file.close()

# loop over the wordlist and check if the password is valid.
with open(wordlist_file, "rb") as f:
    password_found = False
    correct_password = b""
    for password in tqdm(f, total=passwords_count, unit="passwords"):
        try:
            zip_file.extractall(pwd=password.strip())
        except:
            continue
        else:
            password_found = True
            correct_password = password
            break

if password_found:
    print(f"Valid Password found : {correct_password.decode().strip()}")
else:
    print("Password not found, try anotheer wordlist!")