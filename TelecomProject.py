# Read the input from command line – Reference ID
# Check for validity – it should be 12 digits and allows number and alphabet
import re
import rsa

publicKey, privateKey = rsa.newkeys(512)

while True:
    ref_id = input("Enter Reference ID: ")
    is_valid = False

    if (len(ref_id) < 12) | (len(ref_id) > 12):
        print("Not valid. Reference ID should be 12 digits.")
        continue
    elif not re.search("[0-9]", ref_id):
        print("Not valid. Reference ID should contain numbers.")
        continue
    elif not re.search("[A-Z]", ref_id):
        print("Not valid. Reference ID should contain alphabets.")
        continue
    elif not re.search("[$#@]", ref_id):
        print("Not valid. Reference ID should contain at least one special character from $#@")
        continue
    else:
        is_valid = True
        break

if is_valid:
    print(ref_id, "is a valid Reference ID.")

encRefID = rsa.encrypt(ref_id.encode(), publicKey)
print("Entered Reference ID:", ref_id)
print("Encrypted Reference ID:", encRefID)
decRefID = rsa.decrypt(encRefID, privateKey).decode()
print("Decrypted Reference ID:", decRefID)
