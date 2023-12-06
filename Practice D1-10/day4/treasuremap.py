print("Welcome to treasure map")
row1=["😀","😀","😀"]
row2=["😀","😀","😀"]
row3=["😀","😀","😀"]
map=(f"{row1}\n{row2}\n{row3}")
print(map)
column = int(input("Where would you like to put your treasure column no.:"))
row = int(input("Where would you like to put your treasure column no.:"))
if column == 1:
    if row == 1:
        row1[0]="X"
    elif row == 2:
        row1[1]="X"
    else:
        row1[2]="X"
elif column == 2:
    if row == 1:
        row2[0]="X"
    elif row == 2:
        row2[1]="X"
    else:
        row2[2]="X"
elif column == 3:
    if row == 1:
        row3[0]="X"
    elif row == 2:
        row3[1]="X"
    else:
        row3[2]="X"
else:
    print("Pls enter a Value Ranging from 1-3")
map=(f"{row1}\n{row2}\n{row3}")
print(map)