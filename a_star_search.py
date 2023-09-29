from queue import PriorityQueue
from distance_calculator import haversine

def a_star_search(city_data, adjacency_data, start_city, end_city):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_city, [start_city]))
    actual_distance = 0

    while not priority_queue.empty():
        _, current_city, current_route = priority_queue.get()

        if current_city in visited:
            continue

        visited.add(current_city)

        if current_city == end_city:
            return current_route, actual_distance

        neighbors = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
        for neighbor in neighbors:
            if neighbor not in visited:
                new_route = current_route + [neighbor]
                lat1, lon1 = city_data[current_city]['latitude'], city_data[current_city]['longitude']
                lat2, lon2 = city_data[neighbor]['latitude'], city_data[neighbor]['longitude']
                distance = haversine(lat1, lon1, lat2, lon2)
                actual_distance += distance
                priority = actual_distance + haversine(
                    lat2, lon2, city_data[end_city]['latitude'], city_data[end_city]['longitude']
                )
                priority_queue.put((priority, neighbor, new_route))

    return [], 0