# programmed by --------Laghzal-Mouad---------------------Laghazeel------

from cryptography.fernet import Fernet # Symmetric-key 
import rsa # Asymmetric-key 

# Symmetric-key : uses one public key for encryp & decrypt less secure  ---- Fernet ----.
# Asymmetric-key : uses 2 keys, public key in encrypt, private key in decrypt more secure ---- RSA ----. 

#-----------------------------------------Fernet------------------------------------------

def Fernetcrypto():

# let's have an iput string to encrypt
  message = input("enter your secret string :  ")

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator like random.choice
# here I'm using fernet to generate key
  key = Fernet.generate_key()

# Instance the Fernet class with the key
  fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string, it must
# be encoded to byte string before encryption
  encMessage = fernet.encrypt(message.encode())
  print("original string  : ", message)
  print("encrypted string : ", encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
  decMessage = fernet.decrypt(encMessage).decode()
  print("decrypted string: ", decMessage)

#-------------------------------------------RSA --------------------------------------------

def Rsacrypto():

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
  publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
  message = input("enter your secret string :  ")

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
  encMessage = rsa.encrypt(message.encode(),
						publicKey)

  print("original string: ", message)
  print("encrypted string: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
  decMessage = rsa.decrypt(encMessage, privateKey).decode()

  print("decrypted string: ", decMessage)












