# PyCash - a barebones check registry tool
import os
lessRead = "less PyCash.txt"
written = ""

def writeFile():
	f = open("PyCash.txt", "a")
	f.write(written)
	f.close()
def readFile():
	os.system(lessRead)
running = True
while running == True:
    print("""
\033[1;33;40m Welcome to PyCash. \033[0m

Please select an option:
[1] Add a payment
[2] Add a deposit
[3] View finances""")
    response = input("\n>>> ")

# switch cases

    if response == "3":
        running = False
        readFile()
    else:
        print("\nError. Unrecognized response.")
