def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer's age: "))

            if age <= 0:
                print("Age must be a positive number.")
                continue

            return age

        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Simulated eligibility age requirement
minimum_age = 18

try:
    customer_age = get_customer_age()

    if customer_age >= minimum_age:
        print("Customer is eligible for the promotion.")
    else:
        print("Customer is NOT eligible for the promotion.")

except NameError:
    print("A variable was referenced incorrectly. Please check your variable names.")