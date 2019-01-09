# MODULE
# This module has 5 functions for string processing !

def welcomeScreen(option):
	if option =="YES" or option == "yes" or option == "Yes":
		print("\n\t\t\tWELCOME TO THE FUNCTIONALITY OF BCStringProcessor.py\n")
		str = ""
		for i in range(5):
			str = ""
			for j in range(1,10):
				str += "*\t!~\t*\t!~\t*\t!~\t*"
			print(str)
	else:
		print("GOOD BYE THEN !")
		exit()




def findstrIndex(paragraph,string):                                    # finding index of string
	for i in range(len(paragraph)):
		if paragraph[i] == string:
			return i
		
	return False



def countStrInPara(paragraph,string):                                 # counting any alphabet in paragraph
	counter = 0
	count1  = 0
	while counter < len(paragraph):
		if paragraph[counter] == string:
			count1 += 1
		counter += 1
	return( count1 )

	
	
paragraph = input()

def checkAlpha(paragraph):                                     # check all alphabets or not
	count = 0
	while count < len(paragraph):
		if ( paragraph[count] == "A") or (paragraph[count] == "a" ) or (paragraph[count] ==  "B") or (paragraph[count] ==  "b" )  or ( paragraph[count] == "C") or (paragraph[count] == "c" ) or ( paragraph[count] ==  "D" or paragraph[count] ==  "d" ) or  ( paragraph[count] ==  "E") or (paragraph[count] ==  "e" ) or ( paragraph[count] ==  "F") or (paragraph[count] == "f" )  or ( paragraph[count] ==  "G") or (paragraph[count] ==  "g" ) or ( paragraph[count] ==  "H" ) or (paragraph[count] ==  "h" ) or (paragraph[count] ==  "I") or (paragraph[count] ==  "i" ) or ( paragraph[count] ==  "J" ) or (paragraph[count] ==  "j" ) or ( paragraph[count] ==  "K" ) or (paragraph[count] ==  "k" ) or (paragraph[count] ==  "L") or (paragraph[count] ==  "l" ) or ( paragraph[count] == "M") or (paragraph[count] ==  "m" ) or (paragraph[count] == "N") or (paragraph[count] ==  "n" ) or (paragraph[count] ==  "O") or (paragraph[count] ==  "o" ) or ( paragraph[count] ==  "P") or (paragraph[count] == "p" ) or (paragraph[count] == "Q") or (paragraph[count] ==  "q" ) or ( paragraph[count] ==  "R") or (paragraph[count] ==  "r" ) or ( paragraph[count] ==  "S") or (paragraph[count] ==  "s" ) or (paragraph[count] ==  "T") or (paragraph[count] ==  "t" ) or (paragraph[count] ==  "U") or (paragraph[count] ==  "u" ) or ( paragraph[count] ==  "V") or (paragraph[count] ==  "v" ) or  (paragraph[count] ==  "W") or (paragraph[count] ==  "w" ) or (paragraph[count] ==  "X") or (paragraph[count] ==  "x" ) or (paragraph[count] ==  "Y") or (paragraph[count] ==  "y" ) or (paragraph[count] == "Z") or (paragraph[count] ==  "z" ): 
			
			flag = True
			
			
		else:
			flag = False
			break
		count += 1

	return flag


		
			
def removing(paragraph,string):                               # removing any value from string
	str = ""
	for i in paragraph:
		if i != string :
			
			str += i
	return str
		




def searchingNumInSeq(num,sequence):                         # searching Num In Sequence
	count = 0
	
	while count < len(sequence):
		if sequence[count] == num:
			return ("searched number that is",num) , (" has position", count)
			break


		count += 1

	return False
		
	
def ending():
	return("WE HOPE THAT YOU ENJOYED MY MODULE FUNCTIONALITY HAVE A NICE DAY * * ")
	



























