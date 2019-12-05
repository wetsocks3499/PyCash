# PyCash - a barebones check registry tool
import os
lessRead = "cat PyCash.txt | less"
written = ""

def writeFile():
	f = open("PyCash.txt", "a")
	f.write(written)
	f.close()
def readFile():
	os.system(lessRead)

print("""
Welcome to PyCash.

Please select an option:
[1] Add a payment
[2] Add a deposit
[3] View finances""")
response = input("\n>>> ")

# switch cases
while True:
	if response == 3:
		readFile
