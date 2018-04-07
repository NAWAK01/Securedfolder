import os
import zipfile
import time
import base64
import shutil
import getpass

passwordfile = """yourpasswordfordecrytion"""

def encrypt():
	zf = zipfile.ZipFile("data.zip", "w")
	for dirname, subdirs, files in os.walk("data"):
	    zf.write(dirname)
	    for filename in files:
	        zf.write(os.path.join(dirname, filename))
	zf.close()
	shutil.rmtree('data')

	time.sleep(1)

	with open("data.zip", "rb") as file:
		encoded_string = base64.b64encode(file.read())

	output = open("data.zip", "wb")
	output.write(encoded_string)
	output.close()

def decrypt():
	inputfile = open("data.zip", "rb")
	fileencodedbytes = inputfile.read()
	decodedbytes = base64.b64decode(fileencodedbytes)
	outputfile = open("temp.zip", "wb")
	outputfile.write(decodedbytes)
	inputfile.close()
	os.remove('data.zip')
	outputfile.close()
	try:
		with zipfile.ZipFile("temp.zip","r") as zip_ref:
			zip_ref.extractall("")
	except:
		print ("Error while extracting temp.zip")
	time.sleep(0.3)
	os.remove('temp.zip')

print ("Type [E] for encrypt or [X] for extract")
choice = input(">>")
if str(choice) == "E" or str(choice) == "e":
	print ("[!] Encrypting data folder...")
	time.sleep(0.5)
	try:
		encrypt()
		print ("[+] done")
	except:
		print ("[-] error")
elif str(choice) == "X" or str(choice) == "x":
	print ("  ")
	password = getpass.getpass("Enter the password (will be hidden) >>")
	if str(password) == passwordfile:
		print ("[!] Valid password, decrypting data folder")
		try:
			decrypt()
			print ("[+] done")
		except:
			print ("[-] error")
else:
	for x in range(1000):
		print ("[!] Invalid command ")
	exit()

