height= float(input("Enter your height in meters:"))
weight= int(input("Enter your weight in kg:"))
bmi=int(weight/(height**2))
if bmi < 18.5:
    print("Bahut Kamjor ho")
elif bmi < 25:
    print("Hero Lag Rahe Full")
elif bmi < 30:
    print("Khate Pite ghar se ho")
elif bmi < 35:
    print("Mote")
else:
    print("Patla Hoja Mote")