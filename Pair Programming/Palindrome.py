# Program to check whether a string is palindrome

text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")