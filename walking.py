goal = 10_000
total_steps = 0

while True:
    input_steps = input()
    if input_steps == "Going home":
        input_steps = int(input())
        total_steps += input_steps
        if total_steps >= goal:
            print("Goal reached! Good job!")
            print(f"{total_steps - goal} steps over the goal!")
            break
        elif total_steps < goal:
            print(f"{goal - total_steps} more steps to reach goal.")
            break
    input_steps = int(input_steps)
    total_steps += input_steps
    if total_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - goal} steps over the goal!")
        break
