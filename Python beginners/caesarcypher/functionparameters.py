h = int(input("Height of wall:"))
w = int(input("Width of wall:"))
c = int(5)
def no_of_cans(h,w,c):
    cans = (h*w)/c
    print(f"No. of cans required:{cans}")

no_of_cans(h,w,c)