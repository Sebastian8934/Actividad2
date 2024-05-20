import heapq

# Apartado -> Carepa -> Chigorodo -> Mutata 
# Apartado -> turbo -> Necoclí -> Arboletes

# Definimos el sistema de transporte
transport_system = {
    'Apartadó': {'Carepa': 16, 'Turbo': 49},
    'Carepa': {'Apartadó': 16, 'Chigorodó': 12},
    'Chigorodó': {'Carepa': 12, 'Mutata': 56},
    'Mutata': {'Chigorodó': 56},
    'Turbo': {'Apartadó': 49, 'Necoclí': 47},
    'Necoclí': {'Turbo': 47, 'Arboletes': 77},
    'Arboletes': {'Necoclí': 77}
}

# Implementamos el algoritmo de Dijkstra
def dijkstra(graph, start):
    # Inicialización de distancias y caminos
    distances = {city: float('inf') for city in graph}
    previous_nodes = {city: None for city in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_city]:
            continue
        
        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_city
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

# Función para reconstruir el camino más corto
def shortest_path(previous_nodes, start, end):
    path = []
    current_city = end
    while current_city is not None:
        path.append(current_city)
        current_city = previous_nodes[current_city]
    path = path[::-1]  # Revertir el camino
    return path

# Definimos la ciudad de inicio y los destinos
start_city = 'Apartadó'
destinations = ['Mutata']

# Ejecutamos el algoritmo de Dijkstra
distances, previous_nodes = dijkstra(transport_system, start_city)

# Imprimimos las rutas y distancias más cortas
for destination in destinations:
    path = shortest_path(previous_nodes, start_city, destination)
    print(f"La ruta más corta de {start_city} a {destination} es: {' -> '.join(path)} con una distancia de {distances[destination]} km")
