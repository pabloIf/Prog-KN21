class Route:
    def __init__(self, start, end, areas):                      #<-- ctor
        self.start = start
        self.end = end
        self.areas = areas
    def __str__(self):
        return f"Route: {self.start} - {self.end}, length: {self.total_lenght()} km, halt: {self.amount_halt()}"
    def total_lenght(self):
        return sum(self.areas)
    def amount_halt(self):
        return len(self.areas) - 1
    def longest_area(self):
        return max(self.areas)
    
    def __lt__(self, other):                                    #<-- Operators
        return self.total_lenght() < other.total_lenght()
    def __gt__(self, other):
        return self.total_lenght() > other.total_lenght()
    def __le__(self, other):
        return self.total_lenght() <= other.total_lenght()
    def __ge__(self, other):
        return self.total_lenght() >= other.total_lenght()
    
def read_route(filename):                                       #<-- Read file
    routes = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(', ')
            start, end = parts[0], parts[1]
            arias = list(map(int, parts[2:]))
            routes.append(Route(start, end, arias))
    return routes
    
def max_stops(routes):                                          #<-- Route with max stops
    max_stops_route = routes[0]
    for route in routes:
        if route.amount_halt() >= max_stops_route.amount_halt():
            max_stops_route = route
    print(f"Max stops in: {max_stops_route}")

def max_area(routes):                                           #<-- Route with longest area
    max_area_route = routes[0]
    for route in routes:
        if route.longest_area() > max_area_route.longest_area():
            max_area_route = route
    print(f"The largest area: {max_area_route}")

def route_by_point(routes, point, start=True):                  #<-- Fint route by point
    for route in routes:
        if (start and route.start == point) or (not start and route.end == point):
            print(route)





if __name__ == "__main__":
    filename = "routes.txt"
    routes = read_route(filename)
    routes.sort()

    print("All routes sortred:")                                #<-- Print all sorted routes
    for route in routes:
        print(route)
    print("\n")

    max_stops(routes)                                           #<-- using all function
    print("\n")
    max_area(routes)
    print("\n")
    route_by_point(routes, "Кваси", start=True)
    print("\n")
    route_by_point(routes, "Буковель", start=False)
