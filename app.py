name = input("Enter Student Name: ")

python_mark = int(input("Enter Python Mark: "))
git_mark = int(input("Enter Git Mark: "))
docker_mark = int(input("Enter Docker Mark: "))

total = python_mark + git_mark + docker_mark
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

print("\nStudent Name:", name)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)