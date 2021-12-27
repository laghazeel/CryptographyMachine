#cryptography Machine, encryption & decryption mechanisms.

# programmed by --------Laghzal-Mouad---------------------Laghazeel------

# keys function

def machine():

	# define the keys and the crypto values
	Keys = 'abcdefghijklmnopqrstuvwxyz0987654321!/?@çà&é*$ù%§< >^'
	value = Keys[-1] + Keys[-2] + Keys[-3] + Keys[-4] + Keys[0:-1] 

	# set encryption/decryption dictionaries
	encrypDic = dict(zip(value,Keys))
	decrypDic = dict(zip(Keys,value))

	# User interface to input a message
	message = input(" Enter your secret text ! : ")

	# set the mode E: for encode D: for decode
	mode = input(" Choose your crypto mode (E: for encode D: for decode) : ")

	#The machine logic 
	if mode.upper() == 'E':
		newmessage = ''.join([encrypDic[letter] for letter in message.lower()]) # Encryption

	elif mode.upper() == 'D':
		newmessage = ''.join([decrypDic[letter] for letter in message.lower()]) # Decryption 

	else: 
		print(" Please pick the right choice ! ")

	return newmessage.capitalize()







