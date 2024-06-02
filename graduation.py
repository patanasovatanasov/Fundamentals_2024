name = input()
grade = 0
stud_class = 1
failed = 0

while True:
    input_grade = float(input())
    if input_grade < 4:
        failed += 1
        if failed >= 2:
            print(f"{name} has been excluded at {stud_class} grade")
            break
        continue

    stud_class += 1
    grade += input_grade
    if stud_class > 12:
        break

if failed < 2:
    print(f"{name} graduated. Average grade: {grade / (stud_class - 1):.2f}")