# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:19:55 2024
making a table of routes and calculating the fastest route
6/10/2024
CSC121 m1Lab2– Review
Sebastian Baez
@author: sebas
"""

def calculate_time(distance, speed):    
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60
    return time_in_minutes

def main():
    routes = []
    keep_going = True
    
    while keep_going:
        while True:
            try:
                distance = float(input("Enter the distance in miles: "))
                if distance <= 0:
                    print("Distance must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input.")
        
        while True:
            try:
                speed = float(input("Enter the speed in miles per hour: "))
                if speed <= 0:
                    print("Speed must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input.")
        
        routes.append((distance, speed))
        
        while True:
            continue_prompt = input("Do you want to enter another route? (y/n): ")
            if continue_prompt == 'n':
                keep_going = False
                break
            elif continue_prompt == 'y':
                break
            else:
                print("Invalid input.")
    
    first_route = routes[0]
    fastest_time = calculate_time(first_route[0], first_route[1])
    fastest_route_index = 0
    
    for index, (distance, speed) in enumerate(routes):
        time = calculate_time(distance, speed)
        if time < fastest_time:
            fastest_time = time
            fastest_route_index = index

    
    print(f"{fastest_route_index + 1}is fastest, {fastest_time:.2f} minutes.")

main()
