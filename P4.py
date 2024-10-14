import math

def distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def bound(state, graph):
    """Calculate the lower bound for the current state"""
    if len(state) == len(graph):
        return 0
    else:
        min_dist = float('inf')
        for city in graph:
            if city not in state:
                dist = distance(state[-1], city)
                min_dist = min(min_dist, dist)
        return min_dist

def branch_and_bound(graph):
    """Implement the Branch and Bound algorithm for TSP"""
    num_cities = len(graph)
    best_path = []
    best_cost = float('inf')

    def recursive_search(state, cost):
        nonlocal best_path, best_cost
        if len(state) == num_cities:
            cost += distance(state[-1], state[0])
            if cost < best_cost:
                best_cost = cost
                best_path = state[:]
        else:
            for city in graph:
                if city not in state:
                    new_state = state + [city]
                    new_cost = cost + distance(state[-1], city)
                    if new_cost + bound(new_state, graph) < best_cost:
                        recursive_search(new_state, new_cost)

    recursive_search([graph[0]], 0)
    return best_path, best_cost

def main():
    num_cities = int(input("Enter the number of cities: "))
    graph = []
    for i in range(num_cities):
        x, y = map(int, input(f"Enter coordinates of city {i+1} (x, y): ").split())
        graph.append((x, y))

    path, cost = branch_and_bound(graph)
    print("Optimal path:", " -> ".join([f"({x}, {y})" for x, y in path]))
    print("Total distance:", cost)

if __name__ == "__main__":
    main()
