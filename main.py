import csv
import sys
import time

#Importing searching Algorithms
from bfs import bfs
from dfs import dfs
from id_dfs import id_dfs
from best_first_search import best_first_search
from a_star_search import a_star_search

#Importing distance calculator
from distance_calculator import heuristic, haversine, calculate_total_distance

# Read city data (names, latitude, and longitude)
city_data = {}
with open('coordinates_excel.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        city_data[row[0]] = {'latitude': float(row[1]), 'longitude': float(row[2])}


# Read adjacency information
adjacency_data = set()
with open('Adjacencies.txt', 'r') as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespaces
        city1, city2 = line.split()  # Split the line into two words
        adjacency_data.add((city1, city2))
        adjacency_data.add((city2, city1))  # Make adjacency symmetric


#Main Program
while True:
    start_city = input("Enter the starting city: ")
    end_city = input("Enter the ending city: ")


    if start_city not in city_data or end_city not in city_data:
        print("Invalid city names. Please try again.")
        continue

    while True:
        print("Select a search method:")
        print("1. Brute Force Search")
        print("2. Best-First Search")
        print("3. A* Search")
        method = input("Enter the method (1/2/3): ")

        if method == '1':
            #Sub-categories inside Brute Force
            while True:
                print("Select a sub-category for Brute Force:")
                print("1. Breadth-First Search (Brute Force)")
                print("2. Depth First Search (Brute Force)")
                print("3. ID Depth First Search (Brute Force)")
                sub_category = input("Enter the sub-category (1/2/3): ")
                if sub_category == '1':
                    start_time = time.time()
                    route = bfs(city_data, adjacency_data, start_city, end_city)
                    total_distance = calculate_total_distance(city_data, route)
                    end_time = time.time()
                    break
                elif sub_category == '2':
                    start_time = time.time()
                    route = dfs(city_data, adjacency_data, start_city, end_city)
                    total_distance = calculate_total_distance(city_data, route)
                    end_time = time.time()
                    break
                elif sub_category == '3':
                    start_time = time.time()
                    route = id_dfs(city_data, adjacency_data, start_city, end_city)
                    total_distance = calculate_total_distance(city_data, route)
                    end_time = time.time()
                    break
                else:
                    print("Invalid sub-category. Please try again.")

        elif method == '2':
            start_time = time.time()
            route, heuristic_distance = best_first_search(city_data, adjacency_data, start_city, end_city, heuristic)
            total_distance = calculate_total_distance(city_data, route)
            end_time = time.time()
        elif method == '3':
            start_time = time.time()
            route, actual_distance = a_star_search(city_data, adjacency_data, start_city, end_city)
            total_distance = calculate_total_distance(city_data, route)
            end_time = time.time()
        else:
            print("Invalid method. Please try again.")
            continue

        if not route:
            print("No route found.")
        else:
            print("Route:", " -> ".join(route))
            print("Total Distance:", len(route) - 1)
            print("Actual Total Distance: {:.2f} kilometers".format(total_distance))
            if method in ['5']:
                print("Heuristic Distance:", heuristic_distance)
            print("Total Time:", end_time - start_time, "seconds")

        search_again = input("Do you want to search again with other methods? (yes/no): ").lower()
        if search_again != 'yes':
            break

    choice = input("Do you want to search again for other inputs? (yes/no): ")
    if choice.lower() != 'yes':
        print("\nThank you. Now you can go back to your Boring Life!")
        sys.exit(0)
