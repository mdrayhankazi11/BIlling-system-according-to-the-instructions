# WEEK 5 - TUTORIAL 5

A small café wants a simple program to calculate customer bills.

The café sells:

| Item    | Price (RM) |
|---------|------------|
| Coffee    | 8.50    |
| Tea    | 6.00    |
| Sandwich    | 12.00    |

The cashier currently calculates everything manually.

Your task is to build a Python program that helps calculate the customer's bill automatically.

---

## 1. Problem Definition

### 1.1. Problem Statement
The café cashier manually calculates customer bills, which is time-consuming and prone to errors. We need a Python program that automatically calculates the total bill based on the quantities of coffee, tea, and sandwich ordered by a customer, and prints a receipt.

### 1.2. Inputs
- Customer name (string)
- Quantity of coffee (integer)
- Quantity of tea (integer)
- Quantity of sandwich (integer)

### 1.3. Outputs
- A receipt showing:
  - Customer name
  - Quantity of each item ordered
  - Total bill in RM (Malaysian Ringgit)

### 1.4. Typical Process Flow
1. Greet the user.
2. Ask for customer name.
3. Ask for quantities of coffee, tea, and sandwich.
4. Validate inputs (ensure non-negative integers).
5. Calculate total = (coffee_qty * 8.50) + (tea_qty * 6.00) + (sandwich_qty * 12.00).
6. Display the receipt with all details and the total.

### 1.5. Constraints
- Quantities must be non-negative integers.
- Prices are fixed (RM 8.50 for coffee, RM 6.00 for tea, RM 12.00 for sandwich).
- Total must be formatted to two decimal places.
- The program should handle invalid input gracefully (e.g., non-numeric entries).

---

## 2. Decomposition into Smaller Tasks

1. **Get user input** – prompt for customer name and item quantities.
2. **Validate input** – ensure quantities are valid integers >= 0.
3. **Calculate total** – multiply quantities by prices and sum them.
4. **Display receipt** – print formatted receipt with customer name and item quantities.
5. **Main program flow** – tie all functions together and handle errors.

---

## 3. Pseudocode
