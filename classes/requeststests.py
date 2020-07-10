run=True
while run:
    first_number=int(input('Enter first number: '))
    symbol=input('Enter any symbol:')
    second_number=int(input('Enter second number:'))
    if symbol == '+':
        print(first_number+second_number)
    elif symbol == '-':
        print(first_number-second_number)
    elif symbol == '*':
        print(first_number * second_number)
    else:
        print(first_number/second_number)


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        if symbol == '+':
            print(self.a+self.b)

    def multiply(self):
        if symbol == '*':
            print(self.a*self.b)

    def subract(self):
        if symbol == '-':
            print(self.a-self.b)

    def division(self):
        if symbol == '/':
            print(self.a/self.b)


calc1 = Calculator(first_number,second_number)
calc1.add()
calc1.multiply()
calc1.subract()
calc1.division()