def bmi_calculator():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = weight / (height * height)
        print("Your BMI is: " + str(round(bmi, 2)))
    except:
        print("Invalid input. Please enter numbers only.")

def tip_calculator():
    try:
        bill = float(input("Total bill amount: "))
        tip_percent = float(input("Tip percentage (e.g. 15): "))
        tip = bill * (tip_percent / 100)
        total = bill + tip
        print("Tip: " + str(round(tip, 2)))
        print("Total with tip: " + str(round(total, 2)))
    except:
        print("Invalid input. Please enter numbers only.")

def currency_converter():
    try:
        usd = float(input("Amount in GBP: "))
        rate = float(input("Conversion rate to your currency: "))
        converted = usd * rate
        print("Converted amount: " + str(round(converted, 2)))
    except:
        print("Invalid input. Please enter numbers only.")

def age_in_days():
    try:
        age = int(input("Enter your age in years: "))
        days = age * 365
        print("You are about " + str(days) + " days old.")
    except:
        print("Please enter a valid number for age.")

def show_menu():
    print("\n--- Python Multi-Tool Calculator ---")
    print("1. BMI Calculator")
    print("2. Tip Calculator")
    print("3. Currency Converter")
    print("4. Age in Days Calculator")
    print("5. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1 to 5): ")

    if choice == "1":
        bmi_calculator()
    elif choice == "2":
        tip_calculator()
    elif choice == "3":
        currency_converter()
    elif choice == "4":
        age_in_days()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
