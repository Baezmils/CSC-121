# -*- coding: utf-8 -*-
"""
Spyder Editor
creating a modularized menu for calculating cost
6/15/2024
CSC121 m2lab - function review
Sebastian Baez
This is a temporary script file.
"""
def calcCost(count):
    
    price_per_item = 1.00
    total_cost_before_discount = count * price_per_item

    if count >= 10:
        discount = total_cost_before_discount * 0.05
    else:
        discount = 0.0

    total_cost_after_discount = total_cost_before_discount - discount
    return total_cost_after_discount

def displayLine(label, amount):
   
    print(f"{label}: ${amount:.2f}")

def display(cost, tax):
    
    total_cost_after_tax = cost + tax
    displayLine("Total cost before tax", cost)
    displayLine("Sales tax", tax)
    displayLine("Total cost after tax", total_cost_after_tax)
    print("")

def main():
   while True:
    try:
        print("")
        num_items = int(input("Enter the number of items purchased: "))
        print("")
        if num_items < 0:
            print("invalid input.")
            continue
    except ValueError:
        print("")
        print("Invalid input.")
    
    else:
        pre_tax_cost = calcCost(num_items)
        sales_tax_rate = 0.075
        sales_tax = pre_tax_cost * sales_tax_rate
        display(pre_tax_cost, sales_tax)
        break
    
def menu():
    while True:
        print("menu","-"*15, sep="")
        print("1) Calculate cost")
        print("2) Exit")
        print("-"*19)
        choice = input("Enter your choice: ")
           
        if choice == '1':
            main()
        elif choice == '2':
            print("done")
            break
        else:
            print("")
            print("invalid input.")
            print("")
menu()       
