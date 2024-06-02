juri_count = int(input())
average = 0
average_sum = 0
exam_counter = 0

while True:
    presentation = input()
    if presentation == "Finish":
        print(f"Student's final assessment is {average_sum / exam_counter:.2f}.")
        break
    for _ in range(juri_count):
        ocenka = float(input())
        average += ocenka
    else:
        average /= juri_count
    print(f"{presentation} - {average:.2f}.")
    exam_counter += 1
    average_sum += average
    average = 0