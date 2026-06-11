# Pattern Matching Program

text = input("Enter main string: ")
pattern = input("Enter pattern to search: ")

if pattern in text:
    print("Pattern Found")
else:
    print("Pattern Not Found")