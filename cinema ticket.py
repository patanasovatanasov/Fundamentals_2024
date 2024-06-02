student = 0
standard = 0
kid = 0
total_sits = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    total_sits = int(input())
    taken_stud = 0
    taken_stan = 0
    taken_kid = 0

    for _ in range(total_sits):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            taken_stud += 1
        elif ticket_type == "standard":
            taken_stan += 1
        elif ticket_type == "kid":
            taken_kid += 1

    total_tickets = taken_stud + taken_stan + taken_kid
    percent = (total_tickets / total_sits) * 100
    print(f"{movie_name} - {percent:.2f}% full.")

    student += taken_stud
    standard += taken_stan
    kid += taken_kid

print(f"Total tickets: {student + standard + kid}")
print(f"{(student / (student + standard + kid)) * 100:.2f}% student tickets.")
print(f"{(standard / (student + standard + kid)) * 100:.2f}% standard tickets.")
print(f"{(kid / (student + standard + kid)) * 100:.2f}% kids tickets.")
