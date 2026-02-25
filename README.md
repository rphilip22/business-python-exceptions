# Business Python Exceptions

## Exercise 1 – Revenue Calculator with Input Validation

### Description:
This program calculates total revenue based on the number of units sold and price per unit. It ensures that the user enters valid numeric inputs using exception handling.

### Features:
- Uses a reusable function for input validation.
- Handles invalid numeric inputs using `try` and `except`.
- Supports both integer and float inputs.
- Calculates and displays total revenue.

### How the Program Works:
1. The function `get_valid_number()` repeatedly prompts the user until valid input is entered.
2. The user enters:
   - Number of units sold (integer)
   - Price per unit (float)
3. The program calculates total revenue by multiplying the two values.
4. The result is displayed.

### Sample Run

**Input:**
```
Enter number of units sold: 10
Enter price per unit: 25.5
```

**Output:**
```
Total Revenue: $ 255.0
```

---

## Exercise 2 – Inventory Threshold Checker

### Description:
This program checks whether current inventory levels meet a minimum reorder threshold and alerts the user if inventory is low.

### Features:
- Handles invalid integer input.
- Prevents division by zero errors.
- Calculates inventory percentage relative to threshold.
- Displays reorder alert when needed.

### How the Program Works:
1. The user enters:
   - Current inventory level
   - Minimum reorder threshold
2. The program calculates the percentage of inventory compared to threshold.
3. If inventory is below threshold, it displays a reorder alert.
4. Exception handling manages invalid input and zero division errors.

### Sample Run

**Input:**
```
Enter current inventory level: 40
Enter minimum reorder threshold: 50
```

**Output:**
```
Inventory is 80.0 % of the threshold.
Reorder Alert: Inventory below threshold!
```

---

## Exercise 3 – Customer Promotion Eligibility

### Description:
This program determines whether a customer is eligible for a promotion based on age requirements.

### Features:
- Validates age input.
- Ensures age is a positive number.
- Uses exception handling for invalid entries.
- Checks eligibility against minimum age requirement.

### How the Program Works:
1. The function `get_customer_age()` ensures valid age input.
2. The minimum age requirement is set to 18.
3. The program compares the entered age with the requirement.
4. It displays eligibility status.

### Sample Run

**Input:**
```
Enter customer's age: 20
```

**Output:**
```
Customer is eligible for the promotion.
```

---

## Exercise 4 – Profit Margin Calculator

### Description:
This program calculates profit margin as a percentage of revenue while handling possible errors.

### Features:
- Handles invalid numeric input.
- Prevents division by zero.
- Uses `try`, `except`, and `else` blocks.
- Calculates profit margin percentage.

### How the Program Works:
1. The user enters:
   - Profit amount
   - Revenue amount
2. The program calculates the ratio (profit / revenue).
3. If no exception occurs, it calculates and prints the profit margin percentage.
4. The loop continues until valid inputs are entered.

### Sample Run

**Input:**
```
Enter profit amount: 200
Enter revenue amount: 1000
```

**Output:**
```
Profit Margin: 20.0 %
```

---

## Exercise 5 – Salary Adjustment Calculator

### Description:
This program calculates a new salary based on an adjustment percentage provided by the user.

### Features:
- Validates float input.
- Ensures adjustment percentage is between 0 and 100.
- Uses functions to structure the program.
- Calculates salary increase accurately.

### How the Program Works:
1. The function `get_valid_float()` ensures valid numeric input.
2. The user enters:
   - Current salary
   - Adjustment percentage
3. The program validates the percentage range.
4. It calculates and displays the new salary.

### Sample Run

**Input:**
```
Enter current salary: 50000
Enter adjustment percentage (0-100): 10
```

**Output:**
```
New Salary: 55000.0
