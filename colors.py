from colorama import Fore, Back, Style

def GREEN(x , word):
    if(x < 4):
        print(Back.GREEN + Fore.BLACK + word[x] , end = "")
    else:
        print(Back.GREEN + Fore.BLACK + word[x] + Style.RESET_ALL)

def YELLOW(x , word):
    if(x < 4):
        print(Back.YELLOW + Fore.BLACK + word[x] , end = "")
    else:
        print(Back.YELLOW + Fore.BLACK + word[x] + Style.RESET_ALL)
def WHITE(x , word):
    if(x < 4):
        print(Back.WHITE + Fore.BLACK + word[x] , end = "")
    else:
        print(Back.WHITE + Fore.BLACK + word[x] + Style.RESET_ALL)



