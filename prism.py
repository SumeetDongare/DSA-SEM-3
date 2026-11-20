
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[float('inf')] * n for i in range(n)]

for i in range(n):
    graph[i][i] = 0

print("Enter edges (u v weight):")
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

visited = [False] * n
visited[0] = True

cost = 0
count = 0

print("Prim MST:")

for i in range(n - 1):
    minimum = float('inf')
    x = -1
    y = -1

    for u in range(n):
        if visited[u]:
            for v in range(n):
                if not visited[v] and graph[u][v] < minimum:
                    minimum = graph[u][v]
                    x = u
                    y = v

    if y == -1:
        break

    print(x, "-", y, ":", minimum)

    visited[y] = True
    cost += minimum
    count += 1

if count == n - 1:
    print("Minimum Cost:", cost)
else:
    print("Graph is disconnected")
