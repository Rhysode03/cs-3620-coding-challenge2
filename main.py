# Part 1
def bmi():
    weight = float(input("What is your weight(kg):"))
    height = float(input("What is your height(m):"))
    m = round(weight / (height * height), 2)
    print(m)


bmi()


# Part 2

def split(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Cannot divide by zero.')


num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number to divide by:"))
split(num1, num2)



# Part 3

