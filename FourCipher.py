from typing import IO, List

y1 = 	   ["A", "B", "C", "D", "E",
			"F", "G", "H", "I", "J",
			"K", "L", "M", "N", "O",
			"P", "R", "S", "T", "U",
			"V", "W", "X", "Y", "Z"]

x1 = ["A"]*25

x2 = ["A"]*25	  

def RemoveList(duplicate:  List[str]) -> List[str]:
	"""
	Remove duplicates in the list
	return the new list
	""" 
	final_list = [] 
	for Letter in duplicate: 
		if Letter not in final_list:
			final_list.append(Letter) 
	return final_list 

def Square(y1: List[str], x1: List[str]) -> List[str]:
	"""
		Save the new matrix
	"""
	index=0

	for x in range(5):
		x1[index] = y1[index]
		x1[index + 1] = y1[index + 1]
		x1[index + 2] = y1[index + 2]
		x1[index + 3] = y1[index + 3]
		x1[index + 4] = y1[index + 4]
		index=index+5


def Encrypt(name: str, n: int, lengthOfName: int) -> str:
	"""
	Basic Encryption/Decryption for a Four-square cipher
	Do not support any non alphabetical element
	"""
	if(lengthOfName%2 != 0):
		name = name + "z"
	l = [name[i:i+n] for i in range(0, lengthOfName, n)]#separation by two
	k = ""
	index = 6
	index2 = 6
	size = len(l)

	for z in range(size):	
#The length of the message

#################### X side ###########################
#################### Handling Q exception #################					
		if l[z][0].capitalize() == "Q":
			locationY = x1.index(l[z][1].capitalize())
			k+="Q"
			k+=x1[locationY]
########################Y side#############################
#################### Handling Q exception #################			
		elif l[z][1].capitalize() == "Q":
			locationX = x2.index(l[z][0].capitalize())
			k+=x2[locationX]
			k+="Q"

		else:
			locationX = y1.index(l[z][0].capitalize())
			x = locationX//5
			y = locationX % 5
			locationY = y1.index(l[z][1].capitalize())
			index = locationY//5
			index2 = locationY % 5
			k+=x1[x*5 + index2]
			k+=x2[index*5 + y]


	return k

#################################  Main ########################################

Reset = 1
while Reset == 1:
	FirstKey = str(input("Key 1: ")).replace(" ", "")
	FirstKey= RemoveList(FirstKey.upper())


	#Removing the dublicates and add to the key to x1.
	Square(RemoveList(FirstKey + y1), x1)

	SecondKey = str(input("Key 2: ")).replace(" ", "")
	SecondKey= RemoveList(SecondKey.upper())

	#Removing the dublicates and add to the key to x1.
	Square(RemoveList(SecondKey + y1), x2)

	name = str(input("Message: ")).replace(" ","")

	n = 2 #Divide the strings into pairs 
	lengthOfName = len(name)
	Encrypt2= Encrypt(name,n,lengthOfName)

	print("Encryption: "+ Encrypt2)
	lengthOfEncrypt=len(Encrypt2)
	n=2#Divide the strings into pairs 

	Reset = int(input("Repeat press: 1. To stop press: 2 \n"))
