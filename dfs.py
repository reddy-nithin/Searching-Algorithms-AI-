def dfs(city_data, adjacency_data, start_city, end_city):
    def depth_first_search(current_city, visited_cities, path):
        visited_cities.add(current_city)
        path.append(current_city)

        if current_city == end_city:
            return path

        adjacent_cities = [neighbor[1] for neighbor in adjacency_data if neighbor[0] == current_city]
        for neighbor_city in adjacent_cities:
            if neighbor_city not in visited_cities:
                result = depth_first_search(neighbor_city, visited_cities, path.copy())
                if result:
                    return result

        return None

    # Initialize the path with the starting city
    path = depth_first_search(start_city, set(), [])
    return path if path else []