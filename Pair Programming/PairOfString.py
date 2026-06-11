# Program to find pairs of numbers that do not exceed a given limit

numbers = [1, 2, 3, 4, 5]

limit = int(input("Enter limit: "))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] <= limit:
            print(numbers[i], numbers[j])