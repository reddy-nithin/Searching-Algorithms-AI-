import math

# Radius of the Earth in kilometers
EARTH_RADIUS = 6371.0

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = EARTH_RADIUS * c
    return distance

def heuristic(city_data, current_city, end_city):
    if current_city not in city_data or end_city not in city_data:
        return 0  # Handle invalid city names

    # Extract latitude and longitude coordinates of current_city and end_city
    lat1, lon1 = city_data[current_city]['latitude'], city_data[current_city]['longitude']
    lat2, lon2 = city_data[end_city]['latitude'], city_data[end_city]['longitude']

    # Calculate the Haversine distance between the coordinates
    distance = haversine(lat1, lon1, lat2, lon2)

    return distance

# Function to calculate total distance given a route and city data
def calculate_total_distance(city_data, route):
    total_distance = 0
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]

        # Extract latitude and longitude coordinates of current and next city
        lat1, lon1 = city_data[current_city]['latitude'], city_data[current_city]['longitude']
        lat2, lon2 = city_data[next_city]['latitude'], city_data[next_city]['longitude']

        # Calculate the Haversine distance between current and next city
        distance = haversine(lat1, lon1, lat2, lon2)

        total_distance += distance

    return total_distance
