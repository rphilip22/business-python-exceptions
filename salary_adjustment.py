def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    salary = get_valid_float("Enter current salary: ")
    adjustment = get_valid_float("Enter adjustment percentage (0-100): ")

    if adjustment < 0 or adjustment > 100:
        print("Adjustment percentage must be between 0 and 100.")
        return

    new_salary = salary + (salary * adjustment / 100)

    print("New Salary:", new_salary)


main()