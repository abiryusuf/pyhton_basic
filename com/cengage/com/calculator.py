
# Created by Abir Yusuf
class Calculater:
    def sum(self, x, y):
        return x + y

    def diff(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x // y


def main():
    cal = Calculater()
    print("Welcome to Abir Yusuf Pyhton Calculator, please select from the menu below:")
    print("Main Menu \n1: Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n Enter a choice: ")
    n = eval(input())
    x = eval(input("Enter number 1: "))
    y = eval(input("Enter number 2: "))
    # z = eval(input("The Answer is: "))

    if(n == 1):
        print(cal.sum(x, y))
    elif(n == 2):
        print(cal.diff(x, y))
    elif(n == 3):
        print(cal.mul(x, y))
    elif (n == 4):
        print(cal.div(x, y))
    else:
        print("Exit")


main()
print("Exiting... \nThank you for using the python Calculator")