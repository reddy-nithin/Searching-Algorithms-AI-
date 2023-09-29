from collections import deque

def bfs(city_data, adjacency_data, start_city, end_city):
    visited = set()
    queue = deque([(start_city, [start_city])])

    while queue:
        current_city, path = queue.popleft()
        if current_city == end_city:
            return path  # Found a route

        if current_city not in visited:
            visited.add(current_city)
            adjacent_cities = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
            for neighbor_city in adjacent_cities:
                if neighbor_city not in visited:
                    new_path = path + [neighbor_city]
                    queue.append((neighbor_city, new_path))

    return []  # No route found