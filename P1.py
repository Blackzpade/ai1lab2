import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def calculate_frequency(string):
    frequency = {}
    for char in string:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def build_heap(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)
    return heap

def merge_nodes(heap):
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

def build_codes_helper(root, current_code, codes):
    if root == None:
        return

    if root.char != None:
        codes[root.char] = current_code

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)

def build_codes(root):
    codes = {}
    build_codes_helper(root, "", codes)
    return codes

def huffman_encoding(string):
    frequency = calculate_frequency(string)
    heap = build_heap(frequency)
    merge_nodes(heap)

    root = heap[0]
    codes = build_codes(root)

    encoded_string = ""
    for char in string:
        encoded_string += codes[char]

    return encoded_string, root

def min_sum_of_products(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = float('inf')
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + arr1[k] * arr2[j - 1] * arr1[i - 1])

    return dp[n][m]

def kruskal(graph):
    vertices = list(graph.keys())
    edges = []
    for vertex1 in graph:
        for vertex2, weight in graph[vertex1].items():
            edges.append((weight, vertex1, vertex2))

    edges.sort()

    mst = []
    uf = UnionFind(vertices)

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if uf.find(vertex1) != uf.find(vertex2):
            uf.union(vertex1, vertex2)
            mst.append(edge)

    return mst

def prim(graph, start_vertex):
    vertices = list(graph.keys())
    edges = []
    for vertex1 in graph:
        for vertex2, weight in graph[vertex1].items():
            edges.append((weight, vertex1, vertex2))

    edges.sort()

    mst = []
    visited = set()
    visited.add(start_vertex)

    while len(visited) < len(vertices):
        for edge in edges:
            weight, vertex1, vertex2 = edge
            if vertex1 in visited and vertex2 not in visited:
                mst.append(edge)
                visited.add(vertex2)
                break

    return mst

def main():
    while True:
        print("Choose an algorithm:")
        print("1. Huffman coding")
        print("2. Minimum sum of products")
        print("3. Kruskal's minimum spanning tree ")
        print("4. Prim's minimum spanning tree")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            string = input("Enter a string: ")
            encoded_string, root = huffman_encoding(string)
            print("Encoded string:", encoded_string)
        elif choice == 2:
            arr1 = list(map(int, input("Enter the first array of numbers: ").split()))
            arr2 = list(map(int, input("Enter the second array of numbers: ").split()))
            result = min_sum_of_products(arr1, arr2)
            print("Minimum sum of products:", result)
        elif choice == 3:
            graph = {}
            num_vertices = int(input("Enter the number of vertices: "))
            for i in range(num_vertices):
                vertex = input("Enter vertex {}: ".format(i + 1))
                edges = {}
                num_edges = int(input("Enter the number of edges for vertex {}: ".format(vertex)))
                for j in range(num_edges):
                    edge_vertex, weight = input("Enter edge {} and weight: ".format(j + 1)).split()
                    edges[edge_vertex] = int(weight)
                graph[vertex] = edges
            mst = kruskal(graph)
            print("Minimum spanning tree:", mst)
        elif choice == 4:
            graph = {}
            num_vertices = int(input("Enter the number of vertices: "))
            for i in range(num_vertices):
                vertex = input("Enter vertex {}: ".format(i + 1))
                edges = {}
                num_edges = int(input("Enter the number of edges for vertex {}: ".format(vertex)))
                for j in range(num_edges):
                    edge_vertex, weight = input("Enter edge {} and weight: ".format(j + 1)).split()
                    edges[edge_vertex] = int(weight)
                graph[vertex] = edges
            start_vertex = input("Enter the start vertex: ")
            mst = prim(graph, start_vertex)
            print("Minimum spanning tree:", mst)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
