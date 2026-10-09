flight_route = [("Baton Rouge, LA", "Nashville, TN"), ("Nashville, TN", "Indianapolis, IN"),
                ("Indianapolis, IN", "Cleveland, OH"), ("Cleveland, OH", "Boston, MA")]

def print_itinerary(route_list):
    for departure_city, arrival_city in route_list:
        print("Plane departs from", departure_city, "to", arrival_city)

print("Flight Itinerary:")
print_itinerary(flight_route)