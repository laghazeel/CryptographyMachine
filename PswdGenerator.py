# programmed by --------Laghzal-Mouad---------------------Laghazeel------

import random
import string

def PasswordGenerator():
  
  N = 0
  n = input(" Choose your password key lenght ! :  ")
  N = int(n)
  Type = input(" choose your password  Type ! \t\nl for lowercase\nu for uppercase\nL for letters\nd for digits\np for punctuation\nM for mixed characters :  ")
  
# lowercase password
  if Type =='l':
     letters = string.ascii_lowercase
     pswd = ''.join(random.choice(letters) for i in range(N)) 
     print(pswd)

  elif Type =='u':
#  uppercase password
   letters = string.ascii_uppercase
   pswd= ''.join(random.choice(letters) for i in range(N))
   print(pswd)

  elif Type =='L':
#  letters password
   letters = string.ascii_letters
   pswd = ''.join(random.choice(letters) for i in range(N))
   print(pswd)

  elif Type =='d':
#  digits password
   letters = string.digits
   pswd = ''.join(random.choice(letters) for i in range(N))
   print(pswd)

  elif Type =='p':
# punctuation password
   letters = string.punctuation
   pswd = ''.join(random.choice(letters) for i in range(N))
   print(pswd)
# mixed password
  elif Type =='M':
   letters = string.punctuation + string.digits + string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase
   pswd = ''.join(random.choice(letters) for i in range(N))
   print(pswd)       

  else:
   print(" Please enter the right choice : ")


    
    



  



