import networkx as nx
import random

# dutch railway stations
stations = ["Amsterdam Centraal", "Rotterdam Centraal", "Utrecht Centraal", "Den Haag Centraal",
            "Groningen", "Eindhoven", "Tilburg", "Breda", "Arnhem Centraal", "Nijmegen", "Amersfoort",
            "Enschede", "Haarlem", "Leiden Centraal", "Almere Centrum", "Delft"]

def generate_railway_graph():

    # generate graph
    G = nx.Graph()

    # add a node to represent each station
    G.add_nodes_from(stations)

    # add edges for each route
    G.add_edge("Amsterdam Centraal", "Haarlem")
    G.add_edge("Amsterdam Centraal", "Almere Centrum")
    G.add_edge("Amsterdam Centraal", "Utrecht Centraal")
    G.add_edge("Amsterdam Centraal", "Rotterdam Centraal")
    G.add_edge("Rotterdam Centraal", "Utrecht Centraal")
    G.add_edge("Rotterdam Centraal", "Delft")
    G.add_edge("Rotterdam Centraal", "Breda")
    G.add_edge("Utrecht Centraal", "Arnhem Centraal")
    G.add_edge("Utrecht Centraal", "Amersfoort")
    G.add_edge("Utrecht Centraal", "Groningen")
    G.add_edge("Utrecht Centraal", "Den Haag Centraal")
    G.add_edge("Den Haag Centraal", "Leiden Centraal")
    G.add_edge("Den Haag Centraal", "Delft")
    G.add_edge("Groningen", "Nijmegen")
    G.add_edge("Groningen", "Enschede")
    G.add_edge("Eindhoven", "Tilburg")
    G.add_edge("Eindhoven", "Nijmegen")
    G.add_edge("Tilburg", "Breda")
    G.add_edge("Breda", "Dordrecht")
    G.add_edge("Breda", "Eindhoven")
    G.add_edge("Arnhem Centraal", "Nijmegen")
    G.add_edge("Haarlem", "Leiden Centraal")
    G.add_edge("Almere Centrum", "Amersfoort")

    return G


"""
Select a random start station and find a random route of length
from min_route_size to max_route_size
"""
def generate_random_route(G, min_route_size, max_route_size):

    if min_route_size < 2:
        print("[ERROR] Minimum route size must be >1")
        exit(0)

    # select a random start station and make a route
    start_station = random.choice(stations)
    route = [start_station]
    current_station = start_station

    # traverse the graph to generate a random valid route
    route_length = random.randint(min_route_size-1, max_route_size)
    for i in range(route_length):

        destinations = list(G.neighbors(current_station))
        destinations = [d for d in destinations if d not in route]
        if not destinations:
            break
        next_station = random.choice(destinations)
        route.append(next_station)
        current_station = next_station

    return route
