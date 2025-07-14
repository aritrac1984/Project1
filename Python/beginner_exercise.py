# exercise-1

# number1 = int(input("Enter first number:"))
# number2 = int(input("Enter second number:"))

# if number1*number2 <= 1000:
#     print(number1*number2)
# else:
#     print(number1+number2)

# exercise-2

# previous_number = 0

# for current_number in range(10):
#     print(
#         f"Current number {current_number} Previous number {previous_number} Sum: {current_number+previous_number}")
#     previous_number = current_number

# exercise-3

# input_string = input("Enter a string: ")

# start_pointer = 0

# while start_pointer <= len(input_string)-1:
#     print(input_string[start_pointer])
#     start_pointer += 2

# exercise-4

# def remove_chars(word, n):
#     # write your code
#     print(word[n:len(word)])

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# # output 'tive' first four characters are removed

# print(remove_chars("pynative", 2))
# # output 'native'

# exercise-5

# numbers_list = [10, 20, 30, 40, 30, 20, 10]
# numbers_list = [10, 20, 30, 40, 50, 60, 70]

# if numbers_list[0] == numbers_list[len(numbers_list)-1]:
#     print("True")
# else:
#     print("False")

# exercise-6

# numbers_list = [3, 5, 10, 14, 17, 20]

# for num in numbers_list:
#     if num % 5 == 0:
#         print(num)

# exercise-7

# string_x="My name is Neel. Neel is 40. Neel is a good boy. Neel is a programmer"

# print(f"Neel appears {string_x.count("Neel")} times")

# exercise-8

# for x in range(6):
#     for y in range(x):
#         print(x, end=" ")
#     print("\n")

# exercise-9

# input_number=input("Enter a name/number: ").upper()

# reversed_number=input_number[::-1].upper()

# if input_number==reversed_number:
#     print("Input name/number is a Palindrome")
# else:
#     print("Input name/number is not a Palindrome")

# exercise-10

# empty_list = []

# odd_list = [10, 15, 23, 25, 30]
# even_list = [16, 17, 22, 24, 27]

# for num1 in odd_list:
#     if num1 % 2 != 0:
#         empty_list.append(num1)

# for num2 in even_list:
#     if num2 % 2 == 0:
#         empty_list.append(num2)

# print(empty_list)

# exercise-11

# num = int(input("Enter a number: "))

# reversed_number = 0

# while num != 0:
#     reversed_number = reversed_number * 10 + num % 10
#     num //= 10

# print(f"Reversed number is {reversed_number}")

# exercise-12

# salary = int(input("Enter a salary: "))

# if salary <= 10000:
#     income_tax = 0
# elif salary > 10000 and salary <= 20000:
#     income_tax = (salary - 10000) * 0.1
# elif salary>20000:
#     income_tax = 1000 + ((salary - 20000) * 0.2)

# print(f"Income tax: {income_tax}")

# exercise-13

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end=" ")
#     print("\t")

# exercise-14

# for i in range(6, 0, -1):
#     print("*" * i, end="\n")

# exercise-15

# def exponent(base, power):
#     return base ** power

# print(exponent(2, 10000))

# exercise-17

# num1=0
# num2=1

# for i in range(15):
#     print(num1, end=" ")
#     result=num1+num2
#     num1=num2
#     num2=result

