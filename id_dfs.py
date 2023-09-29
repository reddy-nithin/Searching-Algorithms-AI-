def id_dfs(city_data, adjacency_data, start_city, end_city, max_depth=100):
    for depth in range(max_depth):
        result = dfs(city_data, adjacency_data, start_city, end_city, max_depth=depth)
        if result:
            return result
    return []

def dfs(city_data, adjacency_data, current_city, end_city, max_depth, visited_cities=None, path=None):
    if visited_cities is None:
        visited_cities = set()
    if path is None:
        path = []

    visited_cities.add(current_city)
    path.append(current_city)

    if current_city == end_city:
        return path

    if max_depth <= 0:
        return None

    adjacent_cities = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
    for neighbor_city in adjacent_cities:
        if neighbor_city not in visited_cities:
            result = dfs(city_data, adjacency_data, neighbor_city, end_city, max_depth - 1, visited_cities.copy(), path.copy())
            if result:
                return result

    return None