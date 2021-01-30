# 미래 도시 (p.259)

# 전형적인 플로이드 워셜 알고리즘 문제
# 현재 문제에서 N의 범위가 100 이하로 매우 한정적이므로 플로이드 워셜 알고리즘을 이용해도 빠르게 풀 수 있다.
# 이 문제의 핵심 아이디어는 '1번 노드 ~ X ~ K로 가는 최단 거리 = (1번 노드 ~ X의 최단 거리) + (X ~ K의 최단 거리)'라는 것이다.

# ---------------------------------------------------------------------------------------------------------------------
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
distance = graph[1][k] + graph[k][x]
if distance != INF:
    print(distance)
else:
    print(-1)