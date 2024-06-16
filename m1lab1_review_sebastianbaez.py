# -*- coding: utf-8 -*-

"""
Created on Mon Jun 10 15:11:21 2024
creating a loop with decision structure
6/10/2024
CSC121 m1Lab1– Review
Sebastian Baez
@author: sebas
"""
cost_per_item = 0
items = 0

def order():
    keep_going = True
    while keep_going:
        try:
            items = int(input("How many items? "))
            if items <= 0:
                print("invalid amount")
                continue 
            break
        except ValueError:
            print("invalid input")
            continue
    while keep_going:
        try:
            cost_per_item = float(input("Enter cost per item: "))
            if cost_per_item <= 0:
                print("invalid amount")
                continue      
            break
        except ValueError:
            print("invalid input")
            continue
    total = items * cost_per_item

    print("Total cost:",total)
    
    while keep_going:     
        continue_order = input("Do you want to continue? (y/n): ")
        
        if continue_order == 'n':
            keep_going = False
            break
        elif continue_order == 'y':
            order()
            break       
        else: 
            print("invalid choice, choose y to continue and n to finish.")
order()
