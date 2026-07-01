"""
Utils Module - Café Billing System
Week 5 - Tutorial 5

This module contains all the logic functions for the billing system.
"""

# Constants
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee, tea, sandwich):
    """
    Calculate the total bill amount.
    
    Args:
        coffee (int): Quantity of coffee ordered
        tea (int): Quantity of tea ordered
        sandwich (int): Quantity of sandwich ordered
    
    Returns:
        float: Total bill amount in RM
    """
    # Calculate subtotal for each item
    coffee_subtotal = coffee * COFFEE_PRICE
    tea_subtotal = tea * TEA_PRICE
    sandwich_subtotal = sandwich * SANDWICH_PRICE
    
    # Calculate total
    total = coffee_subtotal + tea_subtotal + sandwich_subtotal
    
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    """
    Print a formatted receipt for the customer.
    
    Args:
        customer_name (str): Name of the customer
        coffee (int): Quantity of coffee ordered
        tea (int): Quantity of tea ordered
        sandwich (int): Quantity of sandwich ordered
        total (float): Total bill amount
    """
    print("\n====== RECEIPT =======")
    print(f"Customer: {customer_name}")
    print(f"Coffee: {coffee}")
    print(f"Tea: {tea}")
    print(f"Sandwich: {sandwich}")
    print("----------------------")
    print(f"Total = RM {total:.2f}")
    print("======================")


def get_valid_quantity(item_name):
    """
    Get and validate quantity input from user.
    
    Args:
        item_name (str): Name of the item (e.g., 'Coffee', 'Tea', 'Sandwich')
    
    Returns:
        int: Validated non-negative integer quantity
    """
    while True:
        try:
            quantity = int(input(f"{item_name} quantity: "))
            if quantity >= 0:
                return quantity
            print("Invalid input. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_customer_name():
    """
    Get and validate customer name input.
    
    Returns:
        str: Validated customer name (non-empty)
    """
    while True:
        customer_name = input("Customer name: ").strip()
        if customer_name:
            return customer_name
        print("Error: Name cannot be empty. Please try again.")


def display_welcome():
    """Display welcome message."""
    print("Welcome to the Café Billing System")
    print("------------------------------")
