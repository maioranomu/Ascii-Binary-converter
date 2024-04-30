from ascii import asdecode, asencode
from bin import bindecode, binencode
import os

def cls():
    os.system("cls")
def main():
    while True:
        cls()
        menu = input("1 BINARIO | 2 ASCII ")
        if menu == "1":
            cls()
            binmenu = input("1 ENCODE | 2 DECODE ") 
            if binmenu == "1":
                binencode()
            elif binmenu == "2":
                bindecode()
            else:
                print("Error")
        elif menu == "2":
            cls()
            asciimenu = input("1 ENCODE | 2 DECODE ")
            if asciimenu == "1":
                asdecode()
            elif asciimenu == "2":
                asencode()
            else:
                print("Error")
main()