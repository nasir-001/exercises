#Authur:Nasir Lawal
#Date: 16-Apr-2020
"""
Description: Program that count the total number of words in sentence
"""

def main():

	user_input = input("Enter a sentece here: ")

	listSentence = str.split(user_input, '.')
	listUserInput = str.split(user_input)
	countWords = 0
	countSentence = 0
	
	for a in listUserInput:
		countWords += 1
	print("The total number of words" + " " + countWords)

	for x in listSentence:
		countSentence += 1
	print("The total number of sentence" + "  " + countSentence)

if __name__ == "__main__":
	main()