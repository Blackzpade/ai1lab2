import numpy as np

class TSP:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.n = len(distance_matrix)
        self.final_res = float('inf')
        self.final_path = []

    def tsp(self):
        # Create a 2D array to store the minimum cost of visiting all cities
        visited = [False] * self.n
        visited[0] = True  # Start from the first city
        self.travelling_salesman(0, 1, 0, visited, [0])

    def travelling_salesman(self, curr_pos, count, cost, visited, path):
        # Base case: If all cities are visited and we are back to the start
        if count == self.n and self.distance_matrix[curr_pos][0]:
            total_cost = cost + self.distance_matrix[curr_pos][0]
            if total_cost < self.final_res:
                self.final_path = path + [0]
                self.final_res = total_cost
            return

        # Try to visit the next city
        for i in range(self.n):
            if not visited[i] and self.distance_matrix[curr_pos][i]:
                # Mark the city as visited
                visited[i] = True
                # Recur to visit the next city
                self.travelling_salesman(i, count + 1, cost + self.distance_matrix[curr_pos][i], visited, path + [i])
                # Backtrack: Mark the city as unvisited
                visited[i] = False

    def get_result(self):
        return self.final_res, self.final_path

def input_distance_matrix():
    n = int(input("Enter the number of cities: "))
    distance_matrix = []

    print("Enter the distance matrix (row-wise):")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        distance_matrix.append(row)

    return distance_matrix

if __name__ == "__main__":
    distance_matrix = input_distance_matrix()

    tsp_solver = TSP(distance_matrix)
    tsp_solver.tsp()
    result, path = tsp_solver.get_result()

    print("Minimum cost:", result)
    print("Path taken:", path)

