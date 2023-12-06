s = input("Input a list of student heights:").split()
for n in range(0, len(s)):
    s[n] = int(s[n])
print(s)
total_height = 0
for height in s:
    total_height+=height
print(total_height)
total_students = 0
for students in s:
    total_students+=1
print(total_students)
ans=total_height/total_students
print(f"Avg Height of students is:{ans}")