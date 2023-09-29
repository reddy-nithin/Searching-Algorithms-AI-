from queue import PriorityQueue

def best_first_search(city_data, adjacency_data, start_city, end_city, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_city, [start_city]))
    heuristic_distance = 0  # Initialize heuristic distance

    while not priority_queue.empty():
        _, current_city, current_route = priority_queue.get()

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == end_city:
            return current_route, heuristic_distance  # Return both route and heuristic distance

        neighbors = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
        for neighbor in neighbors:
            if neighbor not in visited:
                priority = heuristic(city_data, neighbor, end_city)
                heuristic_distance += priority  # Accumulate heuristic distance
                new_route = current_route + [neighbor]
                priority_queue.put((priority, neighbor, new_route))

    return [], 0  # Return an empty list and 0 heuristic distance if no route found

'''from queue import PriorityQueue

def best_first_search(city_data, adjacency_data, start_city, end_city, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_city))
    heuristic_distance = 0  # Initialize heuristic distance

    while not priority_queue.empty():
        _, current_city = priority_queue.get()

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == end_city:
            return list(visited), heuristic_distance  # Return heuristic distance as well

        neighbors = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
        for neighbor in neighbors:
            if neighbor not in visited:
                priority = heuristic(city_data, neighbor, end_city)
                heuristic_distance += priority  # Accumulate heuristic distance
                priority_queue.put((priority, neighbor))

    return [], 0 ''' # Return an empty list and 0 heuristic distance if no route found