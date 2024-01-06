print("Love Calculator")
a = input("Enter Your Name:").lower()
b = input("Enter your Partner Name:").lower()
name1=int(a.count("t"))+int(a.count("r"))+int(a.count("u"))+int(a.count("e"))+(a.count("l"))+int(a.count("o"))+int(a.count("v"))+int(a.count("e"))
name2=int(b.count("t"))+int(b.count("r"))+int(b.count("u"))+int(b.count("e"))+(b.count("l"))+int(b.count("o"))+int(b.count("v"))+int(b.count("e"))
final = str(name1)+str(name2)
if int(final) < 10 or int(final) > 90:
    print("Dur Raho Ek dusre se")
if int(final) > 40 and int(final) < 50:
    print("Nibba-Nibbi")
else:
    print(f"Your love score is:{final}")