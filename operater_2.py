#Checking if the character entered is an alphabet or not.
user_input = input("Enter your character please : ")

if len(user_input) :
    user_input = (input("Please enter only one character : "))

if user_input.isalpha() :
    print("Character is in alphabets.")
else :
    print("Character is number.")