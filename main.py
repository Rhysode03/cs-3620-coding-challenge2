# Part 1

def int_validation(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Input was not a number. Please input a number')
            continue
        return value


w = int_validation(input("What is your weight(kg)"))
h = int_validation(input("What is your height(m)"))


def bmi(value): {
    return round(w / (h * h), 2))
}
