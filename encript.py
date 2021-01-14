import random
import secrets
import hashlib
import uuid



def hash_function(password):
    #generate a random uuid as salt
    salt = uuid.uuid4().hex
    print("\nsalt = "+salt)
    return hashlib.sha256(salt.encode("ascii", "replace")+password.encode("ascii", "replace")).hexdigest()+':'+salt
  
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    #replace for preventing string errors
    return password == hashlib.sha256(salt.encode("ascii", "replace") + user_password.encode("ascii", "replace")).hexdigest()

password = "azerty"
print("\n--------------------------------------------------PASSWORD--------------------------------------------------")

print("\npassword: "+ password)
hashed = hash_function(password)
print("\n--------------------------------------------------HASHING--------------------------------------------------")
print("\nhashed: "+hashed)
print("\n------------------------------------------------VERIFICATION------------------------------------------------")

print("\ncheck for password: (True/False) " )
print( check_password(hashed, password))
print("\n-----------------------------------------------------END-----------------------------------------------------")
