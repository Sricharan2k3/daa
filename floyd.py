def floyd_marshall(N, connections):
    INF = float('inf')
    distances = [[INF] * N for _ in range(N)]

    # Initialize distances with direct connections
    for D1, D2, L in connections:
        distances[D1][D2] = L
        distances[D2][D1] = L

    # Update distances using the Floyd-Warshall algorithm
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j])

    return distances


def minimum_wire_length(N, connections):
    distances = floyd_marshall(N, connections)
    print(distances)
    min_distances = [max(distances[i]) for i in range(N)]

    minimum_length = min(min_distances)

    return minimum_length


# Example usage
N = 4  # Number of devices
connections = [
    (0, 1, 3),  # D0 connected to D1 with wire length 2
    (0, 2, 4),  # D0 connected to D2 with wire length 3
    (0, 3, 2),  # D1 connected to D3 with wire length 1
    (1, 0, 3),  # D2 connected to D3 with wire length 4
    (1, 2, 2),  # D2 connected to D4 with wire length 5
    (2, 0, 4),
    (2, 1, 2),
    (2, 3, 1),
    (3, 0, 2),
    (3, 2, 1)
]

minimum_length = minimum_wire_length(N, connections)
print(f"The minimum wire length to connect all devices is: {minimum_length}")
