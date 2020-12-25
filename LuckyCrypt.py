#coding:utf-8

#LuckyCrypt
#by LuckySmile :)

#Note for myself : 32 to 126

#imports
import time
import os

def askValidText(what):
    msg = input(f"What is the {what} you want to crypt ? : ")
    while msg == "":
        msg = input("! Please write something : ")
    #Check that user doesn't write forbidden characters (ex : 'ç' or 'è')
    while not checkChars(msg):
        msg = input(f"! Please write a valid {what} : ")
        while msg == "":
            msg = input("! Please write something !")
    return msg

def askValidKey():
    key = input("What is the key ? : ")
    while key == "":
        key = input("! Please write something :")
    while not checkChars(key):
        key = input("! Please write a valid key : ")
        while key == "":
            key=input("! Please write something  : ")
    return key

def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print("[error] Couldn't find your OS name... Can't clear screen")

def nicePrint(msg):
    for letter in msg:
        print(letter, end='', flush=True)
        time.sleep(0.01)

def checkChars(text):
    for letter in text:
        if ord(letter) < 32 or ord(letter) > 126:
            nicePrint("<error>")
            time.sleep(1)
            nicePrint(f" Character : [{letter}] Forbidden !")
            time.sleep(1)
            print("")
            return False
    return True

def checkFile(file):
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            if not checkChars(line.rstrip("\n")):
                return False
    return True

def menu():
    print("")
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)")
    print("")
    print("1 : Crypt")
    print("2 : Decrypt")
    print("3 : Crypt file")
    print("4 : Decrypt file")
    print("0 : Quit")
    print("")
    choice = input("Make your choice : ")
    if choice.lower() == "exit" or choice.lower() == "quit":
        choice = "0"
    while not choice.isdigit():
        choice = input("! Please, enter a number : ")
    choice = int(choice)
    while choice < 0 or choice > 4:
        choice = input("! Please, enter a number between 0 and 4 : ")
        if choice.lower() == "exit" or choice.lower() == "quit":
            choice = "0"
        while not choice.isdigit():
            choice = input("! Please, enter a number : ")
        choice = int(choice)
    return choice

def seeYou():
    clearScreen()
    seeYou = ['S', 'e', 'e', ' ', 'y', 'o', 'u', ' ', ':', ')']
    for i in range(len(seeYou)):
        print(seeYou[i], end='', flush=True)
        time.sleep(0.1)
    print(" !", end='', flush=True)
    time.sleep(1)
    clearScreen()

def crypt(msg, key):
    crypted = ""
    cpt = 0
    for letter in msg:
        charCrypted = ord(letter) + ord(key[cpt]) -96
        #We stay in utf-8 (32 to 126), so for exemple if ord = 127 we want it to be 32
        if charCrypted > 126:
            charCrypted = charCrypted - 95
        crypted += chr(charCrypted)
        cpt += 1
        if cpt == len(key):
            cpt = 0
    return crypted

def decrypt(msg, key):
    decrypted = ""
    cpt = 0
    for letter in msg:
        charDecrypted = ord(letter) - ord(key[cpt]) + 96
        #We stay in utf-8 (32 to 126), so for exemple if ord = 31 we want it to be 126
        if charDecrypted < 32:
            charDecrypted = charDecrypted + 95
        decrypted += chr(charDecrypted)
        cpt += 1
        if cpt == len(key):
            cpt = 0
    return decrypted

def saveMsg(mode, msg, result):
    first = "<error>"
    second = "<error>"
    if mode == "CRYPTED":
        first = "Original :"
        second = "Crypted  :"
    else:
        first = "Crypted   :"
        second = "Decrypted :"
    with open("Save.txt", 'w') as file:
        file.write(f"{first} {msg}\n{second} {result}")

def readFile(file):
    text = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            text.append(line.rstrip("\n"))
    return text

def cryptFile(file, key):
    crypted = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            crypted.append(crypt(line.rstrip("\n"), key))
    return crypted

def decryptFile(file, key):
    decrypted = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            decrypted.append(decrypt(line.rstrip("\n"), key))
    return decrypted

def saveFile(mode, file, result):
    if mode == "CRYPT":
        newFile = f"{file[:-4]}-crypted.txt"
    else:
        newFile = f"{file[:-4]}-decrypted.txt"
    with open(newFile, 'wt', encoding="utf-8") as file:
        for i in range(len(result)):
            if i < len(result)-1:
                file.write(f"{result[i]}\n")
            else:
                file.write(result[i])

def choice1():
    clearScreen()
    print("< Crypting >")
    print("")
    msg = askValidText("sentence")
    key = askValidKey()
    crypted = crypt(msg, key)
    print("")
    nicePrint("Original : ")
    time.sleep(1)
    nicePrint(msg)
    time.sleep(1)
    print("")
    nicePrint("Crypted  : ")
    time.sleep(1)
    nicePrint(crypted)
    time.sleep(1)
    print("")
    print("")
    saveMsg("CRYPTED", msg, crypted)
    nicePrint("Your data has been saved in [Save.txt] !")
    time.sleep(1)
    print("")
    enter = input("Press enter to continue...")
    clearScreen()
    
def choice2():
    clearScreen()
    print("< Decrypting >")
    print("")
    msg = askValidText("crypted sentence")
    key = askValidKey()
    decrypted = decrypt(msg, key)
    print("")
    nicePrint("Crypted    : ")
    time.sleep(1)
    nicePrint(msg)
    time.sleep(1)
    print("")
    nicePrint("Decrypted  : ")
    time.sleep(1)
    nicePrint(decrypted)
    time.sleep(1)
    print("")
    print("")
    saveMsg("DECRYPTED", msg, decrypted)
    nicePrint("Your data has been saved in [Save.txt] !")
    time.sleep(1)
    print("")
    enter = input("Press enter to continue...")
    clearScreen()

def choice3():
    clearScreen()
    print("< Crypting file >")
    print("")
    cpt = 0
    for file in os.listdir():
        if file.endswith(".txt") and file != "Save.txt":
            nicePrint(f"[{file}]")
            print("")
            cpt += 1
    if cpt == 0:
        nicePrint("! No files detected...")
        time.sleep(1)
        print("")
        print("")
        nicePrint("Please move the file yout want to crypt in the same directory as [LuckyCrypt.py]")
        print("")
        nicePrint("Make sure this is a [.txt] file")
        print("")
        print("")
        enter = input("Press enter to continue...")
    else:
        print("")
        nicePrint(f"{cpt} files detected")
        print("")
        print("")
        file = input("Write the name of the file you want to crypt : ")
        if file == "":
            file = input("! Please write something : ")
        if not file.endswith(".txt"):
            file += ".txt"
        while not os.path.exists(f"{file}"):
            file = input(f"! The file [{file}] doesn't exist here, try again : ")
            while file == "":
                file = input("! Please write something : ")
            if not file.endswith(".txt"):
                file += ".txt"
        if not checkFile(file):
            print(f"! Can't crypt [{file}]")
            print("")
            enter = input("Press enter to continue...")
        else:
            key = askValidKey()
            clearScreen()
            text = readFile(file)
            crypted = cryptFile(file, key)
            nicePrint("Original :")
            time.sleep(1)
            print("")
            for line in text:
                nicePrint(line)
                print("")
            time.sleep(1)
            print("")
            nicePrint("Crypted  :")
            time.sleep(1)
            print("")
            for line in crypted:
                nicePrint(line)
                print("")
            time.sleep(1)
            saveFile("CRYPT", file, crypted)
            print("")
            print("")
            nicePrint(f"Crypted file saved in [{file[:-4]}-crypted.txt]")
            print("")
            print("")
            enter = input("Press enter to continue...")
    clearScreen()

def choice4():
    clearScreen()
    print("< Decrypting file >")
    print("")
    cpt = 0
    for file in os.listdir():
        if file.endswith(".txt") and file != "Save.txt":
            nicePrint(f"[{file}]")
            print("")
            cpt += 1
    if cpt == 0:
        nicePrint("! No files detected...")
        time.sleep(1)
        print("")
        print("")
        nicePrint("Please move the file yout want to decrypt in the same directory as [LuckyCrypt.py]")
        print("")
        nicePrint("Make sure this is a [.txt] file")
        print("")
        print("")
        enter = input("Press enter to continue...")
    else:
        print("")
        nicePrint(f"{cpt} files detected")
        print("")
        print("")
        file = input("Write the name of the file you want to decrypt : ")
        if file == "":
            file = input("! Please write something : ")
        if not file.endswith(".txt"):
            file += ".txt"
        while not os.path.exists(f"{file}"):
            file = input(f"! The file [{file}] doesn't exist here, try again : ")
            while file == "":
                file = input("! Please write something : ")
            if not file.endswith(".txt"):
                file += ".txt"
        if not checkFile(file):
            print(f"! Can't decrypt [{file}]")
            print("")
            enter = input("Press enter to continue...")
        else:
            key = askValidKey()
            clearScreen()
            text = readFile(file)
            decrypted = decryptFile(file, key)
            nicePrint("Crypted :")
            time.sleep(1)
            print("")
            for line in text:
                nicePrint(line)
                print("")
            time.sleep(1)
            print("")
            nicePrint("Decrypted  :")
            time.sleep(1)
            print("")
            for line in decrypted:
                nicePrint(line)
                print("")
            time.sleep(1)
            saveFile("DECRYPT", file, decrypted)
            print("")
            print("")
            nicePrint(f"Decrypted file saved in [{file[:-4]}-decrypted.txt]")
            print("")
            print("")
            enter = input("Press enter to continue...")
    clearScreen()

if __name__ == "__main__":
    choice = menu()
    while choice != 0:
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            choice3()
        elif choice == 4:
            choice4()
        else:
            choice = 0
            nicePrint("<error> Exiting program...")
            time.sleep(2)
        choice = menu()
    seeYou()