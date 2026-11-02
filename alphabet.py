enter = input("type in the character you want to check")

if len(enter) == enter.isalpha():
    print("It is a letter")
else:
    print("It is not a letter")