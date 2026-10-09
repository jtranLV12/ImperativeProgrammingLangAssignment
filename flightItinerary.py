#Flight Itinerary from Baton Rouge, LA to Boston, MA with stops in between
flight_route = [("Baton Rouge, LA", "Nashville, TN"), ("Nashville, TN", "Indianapolis, IN"),
                ("Indianapolis, IN", "Cleveland, OH"), ("Cleveland, OH", "Boston, MA")]

def print_itinerary(route_list):
    print("Flight Itinerary:")
    for departure_city, arrival_city in route_list:
        print("Plane departs from", departure_city, "to", arrival_city)

print_itinerary(flight_route)