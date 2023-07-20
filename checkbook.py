# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +

"""
############################################################
#       Python Project                                     #
#     Command Line Checkbook Application                   #
#   Goal: create a command line checkbook application      #
#   that allows users to track their finances with         #
#   a command line interface.                              #
#                                                          #
#                                                          #
############################################################

"""


import csv # Imports a csv module 
import os # Imports OS module in Python for interacting with the operating system
from datetime import datetime # Supplies classes for manipulating dates and times

file_name = 'transactions.csv'

# Defining the function to create a new .CSV file if it doesn't exist in the os.path.exists() method 
def create_initial_file():
    if not os.path.exists(file_name):
        # Sample data for writing to the .CSV file
        data = [
            ['2023-07-20 13:32:37', 'Credit from client', 0, 500.00, 500.00],
            ['2023-07-20 14:42:22', 'Utilities bill', 50.00, 0, 450.00],
            ['2023-07-20 11:32:37', 'Groceries', 75.00, 0, 375.00],
            ['2023-07-20 10:52:37', 'Salary deposit', 0, 2000.00, 2375.00],
            ['2023-07-20 18:32:37', 'Dinner with friends', 60.00, 0, 2315.00],
            ['2023-07-20 08:32:38', 'Withdraw cash', 100.00, 0, 2215.00],
            ['2023-07-20 13:35:33', 'Online purchase', 50.00, 0, 2165.00],
            ['2023-07-20 16:32:37', 'Credit card payment', 0, 500.00, 2665.00],
            ['2023-07-20 19:32:27', 'Movie tickets', 30.00, 0, 2635.00],
            ['2023-07-20 23:32:13', 'Interest earned', 0, 15.00, 2650.00],
            ['2023-07-20 13:32:42', 'Shopping dress', 0, 45.00, 3640.00],
        ]

        # Open the file in write mode and create a csv.writer object
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write header row with field names
            writer.writerow(['Date_Time', 'Description', 'Debit', 'Credit', 'Balance'])

            # Write data to the CSV file
            for row in data:
                writer.writerow(row)

        print(f"The {file_name} file has been created with sample data.")
        
# Defining the function to read the current balance from the .CSV file
def get_current_balance():
    if not os.path.exists(file_name):
        create_initial_file()

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        balance = 0.0
        for row in reader:
            balance = float(row[4])  # Get the balance from the last row
        return balance


# Defining the function to append the current date, time and balance in the .CSV file   
def update_balance(new_balance):
    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_date, '', '', '', new_balance])
        
        
# Defining the function to record a debit transaction    
def record_debit(balance):
    debit_amount = float(input("\nHow much is the debit? $"))
    new_balance = balance - debit_amount
    update_balance(new_balance)
    print(f"\nYour new balance is ${new_balance:.2f}.")
    return new_balance

# Defining the function to record a credit transaction    
def record_credit(balance):
    credit_amount = float(input("\nHow much is the credit? $"))
    new_balance = balance + credit_amount
    update_balance(new_balance)
    print(f"\nYour new balance is ${new_balance:.2f}.")
    return new_balance

# Defining the function to view all historical transactions 
def view_transactions():
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        print("\n--- Historical Transactions ---")
        for row in reader:
            Date_Time, description, debit, credit, balance = row
            print(f"{Date_Time} - {description} - Debit: {debit}, Credit: {credit}, Balance: {balance}")

# Defining the function to exit from the program            
def endit():
    print("\nThanks, have a great day!")
    return True
    
    
# Defining the function to display the main menu to the user and prompt for their choice    
def display_menu():
    print("\n~~~ Welcome to your terminal checkbook! ~~~")
    print("\nWhat would you like to do?\n")
    print("1) View current balance")
    print("2) Record a debit (withdraw)")
    print("3) Record a credit (deposit)")
    print("4) View all historical transactions")
    print("5) Exit")
    return input("\nYour choice? ")

# The main() function is defined as the entry point of the program
def main():
    balance = get_current_balance()

    while True:
        choice = display_menu()

        if choice == '1':
            print(f"\nYour current balance is ${balance:.2f}.")
        elif choice == '2':
            balance = record_debit(balance)
        elif choice == '3':
            balance = record_credit(balance)
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            if endit():
                break 
            
            
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
















