print("hello suraj")
marks = []
marks1 = int(input("Enter a numbers"))
marks.append(marks1)
marks2 = int(input("Enter a numbers"))
marks.append(marks2)
marks3 = int(input("Enter a numbers"))
marks.append(marks3)
marks4 = int(input("Enter a numbers"))
marks.append(marks4)
marks5 = int(input("Enter a numbers"))
marks.append(marks5)
marks6 = int(input("Enter a numbers"))
marks.append(marks6)
total = sum(marks)
print("total marks:", total)
perc = (total/600)*100
print("percent:", perc)
avg = sum(marks)/6
print("average:", avg)
marks.sort()
print("lowest:", marks[0])
print("highest:" , marks[-1])
if avg >= 90:
    print("Grade A")
elif avg >= 70:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
else:
    print("Fail")