bad_scores = int(input())
bad_scores_counter = 0
problem_counter = 0
grades_total = 0
last_problem = None


while True:
    problem = input()
    if problem != "Enough":
        score = float(input())
        last_problem = problem
        problem_counter += 1
        grades_total += score
        if score <= 4:
            bad_scores_counter += 1
        if bad_scores_counter == bad_scores:
            break
    else:
        break
if problem == "Enough":
    print(f"Average score: {grades_total / problem_counter:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem}")
if bad_scores_counter == bad_scores:
    print(f"You need a break, {bad_scores} poor grades.")