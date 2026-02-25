def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get valid inputs
units_sold = get_valid_number("Enter number of units sold: ", int)
price_per_unit = get_valid_number("Enter price per unit: ", float)

# Calculate total revenue
total_revenue = units_sold * price_per_unit

# Display result
print("Total Revenue: $", total_revenue)