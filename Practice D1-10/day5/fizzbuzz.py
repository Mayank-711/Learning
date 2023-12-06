
for i in range(0,100):
    if i%3==0 and i%5==0:
        i="FrizzBuzz"
        print(i)
    elif i%3==0:
        i="Frizz"
        print(i)
    elif i%5==0:
        i="Buzz"
        print(i)
    else:
        print(i)