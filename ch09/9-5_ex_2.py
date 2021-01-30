# 전보 (p.262)

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# 도시의 개수 N, 통료의 개수 M, 메시지를 보내고자 하는 도시 C
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


# 개선된 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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


dijkstra(c)

# 가장 거리가 먼 도시에 따라 전보 시간이 결정됨
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        max_distance = max(max_distance, d)
        count += 1

print(count - 1, max_distance)

# 입력 예시
# 3 2 1
# 1 2 4
# 1 3 2
# 출력 예시
# 2 4
