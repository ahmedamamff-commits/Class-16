try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
#using multiple "except" blocks for different types of errors

except ZeroDivisionError:
    print("Divison by zero is not allowed! It is a pesky error!!!!")

except SyntaxError:
    print("Comma is missing! That is another PESKY ERROR WHAT ARE YOU THINKING?????????????????????")

except:
    print("Wrong input")

else:
    print("No errors or exceptions...Man I really hate those pesky errors!!!!")

finally:
    print("This wil run no matter what...I really hate those pesky errors!!!!")