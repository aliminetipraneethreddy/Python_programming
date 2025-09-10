def StudentDetails():
    l1 = []
    for i in range(5):
        rno, name, marks = input("Enter roll number, name, marks separated by space: ").split()
        l1.append((rno, name, marks))
    return l1

students = StudentDetails()
print("Student details:")
for i in students:
    if i[2]>75:
        print(i[0])
max1=0
for i in students:
    if i[2]>max1:
        max1=i[2]
print(max1)
print(students)
