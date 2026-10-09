def dfs(graph,start_node):
    visited =[]
    qeueu = []
    visited.append(start_node)
    qeueu.append(start_node)
    while qeueu!=[]:
        current_node = qeueu.pop()
        # print(current_node)
        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited:
                visited.append(neighbor)
                qeueu.append(neighbor)
    return visited

student_graph ={}

edge = int(input("enter number of edge:"))
print("Enter each edge sepreately bya space (e.g:A B)")
for i in range(edge):
    u,v = input(f"edge{i+1}:").split()

    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)
print(student_graph)
list = list(student_graph.keys())
start_node = list[0]

print(dfs(student_graph,start_node))



            

