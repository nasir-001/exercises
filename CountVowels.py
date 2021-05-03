#Authur: Nasir Lawal
#Date: 16th-Apr-2020
"""
Description: Counting Vowel and consonant sound in a sentece as well as whitespace
"""


def main():

	user_input = input("Enter the letter here.")

	vowel = ['a', 'e', 'i', 'o', 'u']
	countVowel = 0
	countConsonat = 0
	countSpace = 0

	if user_input:
		convertUserInput = user_input.lower()
	for a in convertUserInput:
		if a in vowel:
			countVowel += 1
		elif a == ' ':
			countSpace += 1
		else:
			countConsonat += 1

	print("The total number of vowel is" + " " + str(countVowel))
	print("The total number of consonant is" + " " + str(countConsonat))
	print("The total number of whitespace is" + " " + str(countSpace))


if __name__ == "__main__":
	main()