from graph.graph import Graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


def bfs(node): #function for BFS
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue

  visited.append(node)
  queue.append(node)
  result = []  # Create a list to store the visited nodes in order

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    result.append(m)  # Append the current node to the result list
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return result

# Driver Code
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('5', '2')
    graph.add_edge('5', '0')
    graph.add_edge('4', '0')
    graph.add_edge('4', '1')
    graph.add_edge('2', '3')
    graph.add_edge('3', '1')
    result = bfs('5')

    print("Breadth-First Search Result:")
    print(result)