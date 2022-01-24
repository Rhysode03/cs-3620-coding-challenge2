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
    products = {
        'bike': 10.00,
        'car': 50.00,
        'shoes': 3.00,
        'belt': 5.00,
        'saw': 15.00
    }
    print(products.get(p, 'That is not a product.'))


product(input("Choose a product to view price:"))

# Part 5

odd = list(x for x in range(1, 101) if x % 3 == 0)
print(odd)
