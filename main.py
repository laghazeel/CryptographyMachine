# programmed by --------Laghzal-Mouad---------------------Laghazeel------

from Cryptomachine import machine
from Cryptofunctions import Fernetcrypto, Rsacrypto
from PswdGenerator import PasswordGenerator

# set up the menu with dictionnary
menu_options = {
    1: 'Basic cryptomachine (Dict(zip())) ',
    2: 'Symmetric key encryption (Fernet) ',
    3: 'Asymmetric key encryption (RSA) ',
    4: 'Generate password (Random) ',
    5: 'Exit '
}

# define the function to print the menu options
def print_menu():
    for key in menu_options.keys():
        print (key, '  *----------*  ', menu_options[key])

# make menu options with functions !! make them in separate files to keep the code readable and easy
def cryptomachineBasic():
     print(machine())
def cryptomachineSymetric():
     print(Fernetcrypto())
def cryptomachineAsymetric():
     print(Rsacrypto())
def PSWgenerator():
     print(PasswordGenerator())     
def exitpy():
    print(exit)
    exit()

# the infinite loop while will keep the program running until the user type exit option to stop it
while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice : '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           cryptomachineBasic()
        elif option == 2:
            cryptomachineSymetric()
        elif option == 3:
            cryptomachineAsymetric()
        elif option == 4:
            PSWgenerator()
        elif option == 5:
            exitpy()
        else:
           print('Invalid option. Please enter a number between 1 and 4.')

# enjoyyyyyyyyy programming with Laghazeel.