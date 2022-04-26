graph= {
  'S' : ['1','2','3','4'],
  '1' : ['5','6','7'],
  '2' : ['8','9'],
  '3' : ['10','11'],
  '4' : ['12','13','14'],
  '5' : ['15'],
  '6' : ['16'],
  '7' : [],
  '8' : ['17'],
  '9' : ['18'],
  '10' : ['19'],
  '11' : ['20'],
  '12' : ['21'],
  '13' : [],
  '14' : ['22'],
  '15' : [],
  '16' : [],
  '17' : [],
  '18' : [],
  '19' : [],
  '20' : ['D'],
  '21' : [],
  '22' : [],
  'D':[]
}
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
             dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'S')




# visited = [] # List for visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node): #function for BFS
#   visited.append(node)
#   queue.append(node)

#   while queue:          # Creating loop to visit each node
#     m = queue.pop(0) 
#     print (m, end = " ") 

#     for neighbour in graph[m]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# print("Following is the Breadth-First Search")
# bfs(visited, graph, 'S')    # function calling
