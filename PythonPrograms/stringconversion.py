user_input=input("Enter the sentenceg with same case: ")
if user_input.isupper():
    user_input=user_input.lower()
    print(user_input)
else:
    user_input=user_input.upper()
    print(user_input)