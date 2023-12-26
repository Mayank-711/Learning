try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    c = a/b
except ValueError:
    print('Pls enter a number')
except ZeroDivisionError:
    print("Dont give number as 0")