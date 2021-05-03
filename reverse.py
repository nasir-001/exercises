#Authur:Nasir Lawal	
#Date: 16th-Apr-2020

"""
Description: Reverse a given string from user
"""

def main():

	user_input = input("Enter the string to be reverse")

	reverse_user_input = []
	for a in user_input:
		reverse_user_input.insert(0, a)

	print(reverse_user_input)

if __name__ == "__main__":
	main()