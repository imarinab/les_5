n = 0
print('For exit enter "stop"')

while True:
    n += 1
    print(f'\nThis is the {n} try\n')

    first_number = input("Enter first number: ")
    if first_number == "stop":
        break
    action = input("Enter operator: ")
    if action == "stop":
        break
    second_number = input("Enter second number: ")
    if second_number == "stop":
        break

    if action == '+':
        print(f"Your result:\n {int(first_number)} + {int(second_number)} = {int(first_number) + int(second_number)}")
    elif action == '-':
        print(f"Your result:\n {int(first_number)} - {int(second_number)} = {int(first_number) - int(second_number)}")
    elif action == '*':
        print(f"Your result:\n {int(first_number)} * {int(second_number)} = {int(first_number) * int(second_number)}")
    elif action == '/':
        print(f"Your result:\n {int(first_number)} / {int(second_number)} = {round((int(first_number) / int(second_number)), 2)}")
    else:
        print("Something was going wrong. Try again")
