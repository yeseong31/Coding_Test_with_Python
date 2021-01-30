# 전보 (p.262)

# 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있으므로 다익스트라 알고리즘을 이용하면 된다.
# N, M의 범위가 충분히 크기 때문에, 우선순위 큐를 이용하여 다익스트라 알고리즘을 작성해야 한다.

# ---------------------------------------------------------------------------------------------------------------------

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드 입력받기
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 잇는 노드 중에서, 가장 멀리 잇는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        max_distance = max(max_distance, d)
        count += 1

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)