from os import system
inputWord = "Abheek"
usrString = ""
attempts = 0
tries = []
errorset = False

for i in range(len(inputWord)):
    usrString+="*"

print(usrString)

while "*" in usrString and attempts < 6:
    attempts += 1
    try:
        a = input("Guess: ")[0].lower()
    except IndexError:
        print("Enter a letter.")
        errorset = True
        break
    tries.append(a)
    if a in inputWord.lower():
        system("clear")
        print(a + " is in the word!")
        for i in range(len(inputWord)):
            if a == inputWord[i].lower():
                if i == 0:
                    usrString = inputWord[i] + usrString[1:]
                else:
                    usrString = usrString[:i] + inputWord[i] + usrString[i+1:]
        print(usrString)
    else:
        system("clear")
        print("Nice Try, but " + a + " is not in the word.")
        print("Your attempts are: " + str(tries).replace("]", "").replace("[", "").replace("'", ""))
        print(usrString)


if errorset:
    print("", end="")
elif attempts < 6:
    print("Congrats, you won!")
else:
    print("Too many attempts , you just died.")
    