import myStringProcessor           

def main():

	option = input("Do you want to use the functionality of myStringProcessor.py (Yes or No? ")

	myStringProcessor.welcomeScreen(option)                                             # Using function of Module

	print("Here you have following functions:\n")

	print("1.finding string index\n2.counting any alphabet in paragraph\n3.check all alphabets or not\n4.removing any value from string\n5.searching Num In Sequence")

	option1 = input("Do you want to find the index of string in paragraph:(Y or N) ? ")

	if option1 == "Y" or option1 =="y" :

		paragraph = input("Write any paragraph\t")

		string    = input("Write any string to find its index at first occurance in paragraph\t")

		print(myStringProcessor.findstrIndex(paragraph,string))                               # Using function of Module


	option2 = input("Do you want to count string in paragraph:(Y or N) ? ")

	if option2 == "Y" or option2 =="y" :

		paragraph = input("Write any paragraph\t")

		string    = input("Write any string to be count in paragraph\t")

		print(myStringProcessor.countStrInPara(paragraph,string))                               # Using function of Module



	option3 = input("Do you want to check whether all para is in alphabets or not:(Y or N) ? ")

	if option3 == "Y" or option3 == "y":

		paragraph = input("Write any paragraph of your choice:\t")

		print(myStringProcessor.checkAlpha(paragraph))                                             # Using function of Module



	option4 = input("Do you want to remove string from paragraph:(Y or N) ? ")

	if option4 == "Y" or option4 == "y":

		paragraph = input("Write any paragraph of your choice:\t")

		string    = input("Write any letter you want to remove from the paragraph\t")

		print(myStringProcessor.removing(paragraph,string))                                           # Using function of Module





	option5 = input("Do you want to search any number in the sequence:(Y or N) ? ")                    # Option if you want search num in the sequence

	if option5 == "Y" or option5 == "y":

		sequence = (input("Enter any sequence of numbers without space\t"))

		num      = (input("Enter the number to find in the sequence\t"))

		print(myStringProcessor.searchingNumInSeq(num,sequence))                                        # Using function of Module

	print(myStringProcessor.ending())




main()


