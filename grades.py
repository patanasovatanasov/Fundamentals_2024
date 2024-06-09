def grades(grade):
    if 2 <= grade <= 2.99:
        word = "Fail"
    elif 3 <= grade <= 3.49:
        word = "Poor"
    elif 3.50 <= grade <= 4.49:
        word = "Good"
    elif 4.50 <= grade <= 5.49:
        word = "Very Good"
    elif 5.50 <= grade <= 6:
        word = "Excellent"
    return word


grade_data = float(input())
print(grades(grade_data))