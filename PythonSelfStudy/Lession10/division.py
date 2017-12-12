''' print(5/0) '''
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Input two numbers, and I'll divid them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nInput the first number: ")
    if first_number == 'q':
        break
    second_number = input("Input the second number: ")
    if first_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("You can't input anything not a number")
    else:
        print(answer)
