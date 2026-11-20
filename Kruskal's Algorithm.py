
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append([w, u, v])

edges.sort()

parent = [i for i in range(n)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a != b:
        parent[b] = a
        return True

    return False


cost = 0
count = 0

print("Kruskal MST:")

for w, u, v in edges:
    if union(u, v):
        print(u, "-", v, ":", w)
        cost += w
        count += 1

        if count == n - 1:
            break

if count == n - 1:
    print("Minimum Cost:", cost)
else:
    print("Graph is disconnected")
