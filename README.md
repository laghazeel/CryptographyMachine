------------------------------------------------------------
informations -----Laghzal-Mouad-------laghazeel---
------------------------------------------------------------
- Encryption is the process of encoding the data.
  i.e converting plain text into ciphertext. 
  This conversion is done with a key called an encryption key.

- Decryption is a process of decoding the encoded data. 
  Converting the ciphertext into plain text. 
  This process requires a key that we used for encryption.

- We require a key for encryption. 
  There two main types of keys used for encryption and decryption. 
  They are Symmetric-key and Asymmetric-key.

- Symmetric-key : (Fernet)
    In symmetric-key encryption, the data is encoded and decoded with the same key.
    This is the easiest way of encryption, but also less secure. 
    The receiver needs the key for decryption, so a safe way need for transferring keys. 
    Anyone with the key can read the data in the middle.
-  Asymmetric-key :
    In Asymmetric-key Encryption, we use two keys a public key and private key. 
    The public key is used to encrypt the data and the private key is used to decrypt the data. 
    By the name, the public key can be public (can be sent to anyone who needs to send data). 
    No one has your private key, so no one the middle can read your data.

-------------------------------------------------------------------------------------
About the program  -----Laghzal-Mouad-------laghazeel---
-------------------------------------------------------------------------------------
- This python project is consisting of a menu that contains 5 options

    1:  Basic cryptomachine (Dict(zip())) 
    2:  Symmetric key encryption (Fernet) 
    3:  Asymmetric key encryption (RSA)
    4:  Generate password (Random)
    5:  Exit
- Each option refer to a crypto function.
- 1 is for a basic concept of crypto i used dict(zip) python functions to
   encrypt and dycript text, and a pre-defined key (static).
- 2 & 3 are for symmetric & asymmetric crypto using libs like
  cryptography and rsa. (Fernet for one public key, less secure & RSA for public & private
  keys more secure )
- 4 is for a password generator with  String and Random in python, they are multiple choices
   for any password type you want to generate.

---Note !!---- 
This program contains a lot of options nested in the menu 
Take your time to check it all.

---------------------------------------------------------------------------------
For execution  -----Laghzal-Mouad-------laghazeel---
----------------------------------------------------------------------------
There are 4 python files, you can use any OS you want, go to main.py execute it 
and have fan .

-----------------------------------------------------
License    -----Laghzal-Mouad-------laghazeel---
-----------------------------------------------------
For me any project i'v done i consider it an open-source
for everyone, you can use the code as you want
 !! But i'll be thankful if you give me a credit for reusing it
Thanks, and Enjoyyyyyyyyyy ! 