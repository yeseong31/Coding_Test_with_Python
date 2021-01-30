# 간단한 다익스트라 최단 경로 알고리즘 -----------------------------------------
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 n, 간선 개수 m
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프
graph = [[] for _ in range(n + 1)]
# 방문 목록
visited = [False] * (n + 1)
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = 1
    return index


# 다익스트라
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INFINITY')

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4

# 개선된 다익스트라 최단 경로 알고리즘 -----------------------------------------
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 n, 간선 개수 m
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라
def dijkstra(start):
    q = []
    heapq.append(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INFINITY')

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4

# 플로이드 워셜 알고리즘 -------------------------------------------------------
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] != INF:
            print(graph[a][b], end=' ')
        else:
            print('INFINITY', end=' ')
    print()

# 입력 예시
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
# 출력 예시
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0