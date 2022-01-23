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

def files(a):
    text = open('demo.txt', 'a')
    text.write(a)
    text.close()


files(input("What would you like to write to the file?"))
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()


# Part 4

def product(p):
    products = [
        {
            'id': 1,
            'Name': 'Bike',
            'Price': 10.00,
        },
        {
            'id': 2,
            'Name': 'Car',
            'Price': 50.00,
        },
        {
            'id': 3,
            'Name': 'Shoes',
            'Price': 3.00,
        },
        {
            'id': 4,
            'Name': 'Belt',
            'Price': 5.00,
        },
        {
            'id': 5,
            'Name': 'Saw',
            'Price': 15.00,
        }
    ]
    case: 'id' == 1
    print(1 in products)
    case: 2
    print(2 in products)
    case: 3
    print('id' == 3 in products)


product(input("Choose a product from 1-5:"))
