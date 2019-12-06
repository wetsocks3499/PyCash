# PyCash - a barebones check registry tool
import os
total = 0
lessRead = "less PyCash.txt"
dollars = ""
written = ""
paymentTo = ""
date = ""
memo = ""

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
    if response == "1":
        print("\nPlease enter the dollar amount paid:\n>>> ")
        dollars = input()
        total -= int(dollars)
        print("\nTo whom was it paid?\n>>> ")
        paymentTo = input()
        print("\nOn what date was it paid?\n>>> ")
        date = input()
        print("\nWould you like to add a memo? (Press Enter to leave it blank)\n>>> ")
        memo = input()
        written = "\nPayment to "+paymentTo+" for $"+dollars+" on "+date+" [Total: $"+dollars+"]"+memo
        writeFile()
        running = False
    if response == "2":
        print("\nPlease enter the dollar amount deposited:\n>>> ")
        dollars = input()
        total += int(dollars)
        print("\nOn what date was it deposited?\n>>> ")
        date = input()
        print("\nWould you like to add a memo? (Press Enter to leave it blank)\n>>> ")
        memo = input()
        written = "\nDeposit for $"+dollars+" on "+date+" [Total: $"+dollars+"]"+memo
        writeFile()
        running = False
    if response == "3":
        running = False
        readFile()
