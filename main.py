"""
Main Program - Café Billing System
Week 5 - Tutorial 5

This is the main entry point for the café billing system.
"""

# Import functions from utils.py
from utils import (
    display_welcome,
    get_customer_name,
    get_valid_quantity,
    calculate_total,
    print_receipt
)


def main():
    """
    Main program flow.
    Controls the sequence of operations for the billing system.
    """
    # Display welcome message
    display_welcome()
    
    # Get customer name with validation
    customer_name = get_customer_name()
    
    # Get quantities with validation for each item
    coffee_qty = get_valid_quantity("Coffee")
    tea_qty = get_valid_quantity("Tea")
    sandwich_qty = get_valid_quantity("Sandwich")
    
    # Calculate total bill
    total = calculate_total(coffee_qty, tea_qty, sandwich_qty)
    
    # Display receipt
    print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total)


# Run the program when this file is executed directly
if __name__ == "__main__":
    main()
