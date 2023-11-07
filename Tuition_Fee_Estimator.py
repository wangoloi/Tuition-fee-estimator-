import sys

print(
    "......................YOU ARE WELCOME TO THE UNIVERSITY SCHOLARSHIPS..............."
)
print(
    "\n....The following below, are the available scholarships for the students at this university at different levels...."
)
print(
    "\n1. Diploma = 50% of the tuition.\n2. Degree = 75% of the tuition.\n3. Masters = 100% of the tuition."
)

while True:
    try:
        select = int(input("Select your level either 1, 2 or 3: "))
        if select == 1:
            print("You qualify for a scholarship of 50% of your tuition.")
            diploma = float(input("Enter your fees structure: "))
            diploma_tuition = 50 / 100 * diploma
            diploma_balance = diploma - diploma_tuition
            print(f"Your supposed to pay shs {diploma_balance} as your tuition")
        elif select == 2:
            print("You qualify for a scholarship of 75% of your tuition.")
            degree = float(input("Enter your fees structure: "))
            degree_tuition = 75 / 100 * degree
            degree_balance = degree - degree_tuition
            print(f"Your supposed to pay shs {degree_balance} as your tuition")
        elif select == 3:
            print("You qualify for a scholarship of 100% of your tuition.")
            masters = float(input("Enter your fees structure: "))
            masters_tuition = 100 / 100 * masters
            masters_balance = masters - masters_tuition
            print(
                f" Congs Boss, Your supposed to pay shs {masters_balance} as your tuition, therefore , the University is paying for you full tuition. Thnx"
            )
        else:
            print("Invalid input. Please enter a valid input.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid input.")
        continue
    exit_choice = input("Do you want to exit? (yes/no): ")
    if exit_choice.lower() == "yes":
        sys.exit()
