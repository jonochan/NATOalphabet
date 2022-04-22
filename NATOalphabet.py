Nalphabet = {
    "a" : "Alpha ",
    "b" : "Bravo ",
    "c" : "Charlie ",
    "d" : "Delta ",
    "e" : "Echo ",
    "f" : "Foxtrot ",
    "g" : "Golf ",
    "h" : "Hotel ",
    "i" : "India ",
    "j" : "Juliett ",
    "k" : "Kilo ",
    "l" : "Lima ",
    "m" : "Mike ",
    "n" : "November ",
    "o" : "Oscar ",
    "p" : "Papa ",
    "q" : "Quebec ",
    "r" : "Romeo ",
    "s" : "Sierra ",
    "t" : "Tango ",
    "u" : "Uniform ",
    "v" : "Victor ",
    "w" : "Whiskey ",
    "x" : "Xray",
    "y" : "Yankee",
    "z" : "Zulu",
    }

def translate(text):
    length = len(text)
    translation =""
    for x in range(length):
        currentChar = text[x].lower()
        if currentChar in Nalphabet:
            translation = translation + Nalphabet.get(currentChar)
        elif currentChar == "!" or currentChar == "." or currentChar == "?" or currentChar == ",":
            translation = translation[:-1] + currentChar + " "
    return translation[:-1]


file = open(r"C:\Users\Chiza\Desktop\python\translate.txt", "r")
number = int(file.readline())
number = number +1
text = file.readline()
file.close()
result = translate(text)
print(result)
file = open("translate.txt", "w")
file.write(str(number) + "\n")
file.write(result)
file.close()
