# BMI CALCULATOR PROJECT

def get_details():
    print("\nEnter your details")
    print("----------------------------------------")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    return name, age, gender, height, weight


def calculate_bmi(height, weight):
    height = height / 100
    bmi = weight / (height * height)
    bmi = round(bmi, 2)

    return bmi, height


def show_result(name, age, gender, height, weight, bmi):

    print("\n========================================")
    print("              YOUR RESULT")
    print("========================================")

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height, "m")
    print("Weight:", weight, "kg")
    print("BMI:", bmi)

    print("----------------------------------------")

    if bmi < 18.5:
        print("Category: Underweight")
        print("Suggestion:")
        print("Try to eat a healthy and balanced diet.")

    elif bmi < 25:
        print("Category: Normal Weight")
        print("Suggestion:")
        print("Great! Keep maintaining a healthy lifestyle.")

    elif bmi < 30:
        print("Category: Overweight")
        print("Suggestion:")
        print("Try exercising regularly and eat healthy food.")

    else:
        print("Category: Obese")
        print("Suggestion:")
        print("Regular exercise and a balanced diet are important.")

    print("----------------------------------------")
    print("             BMI RANGE")
    print("----------------------------------------")

    print("Below 18.5  : Underweight")
    print("18.5 - 24.9 : Normal Weight")
    print("25 - 29.9   : Overweight")
    print("30 and above: Obese")

    print("========================================")

    if age < 13:
        print("Age Group: Child")
    elif age < 20:
        print("Age Group: Teenager")
    elif age < 60:
        print("Age Group: Adult")
    else:
        print("Age Group: Senior")

    print("========================================")


print("========================================")
print("          BMI CALCULATOR")
print("========================================")
print("Welcome to the BMI Calculator!")
print("Let's check your Body Mass Index.")
print("========================================")

while True:

    name, age, gender, height, weight = get_details()

    if height <= 0 or weight <= 0:
        print("\nPlease enter valid height and weight.")
        continue

    bmi, height = calculate_bmi(height, weight)

    show_result(name, age, gender, height, weight, bmi)

    choice = input("\nDo you want to calculate again? (yes/no): ")

    if choice.lower() == "yes":
        print("\nStarting a new calculation...")
        print("----------------------------------------")

    elif choice.lower() == "no":
        print("\n========================================")
        print("   THANK YOU FOR USING BMI CALCULATOR")
        print("          Stay Healthy!")
        print("========================================")
        break

    else:
        print("\nInvalid choice.")
        print("Program ended.")
        break
    