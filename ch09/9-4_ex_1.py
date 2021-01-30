# 미래 도시 (p.259)

INF = int(1e9)
start = 1

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 그래프(a와 b와 연결)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 ~ 자기 자신
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 연결된 노드 간 거리는 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 목적지, 소개팅 장소
x, k = map(int, input().split())

# 플로이드 워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[start][k] + graph[k][x]
if distance != INF:
    print(distance)
else:
    print(-1)

# 입력 예시
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 출력 예시
# 3
