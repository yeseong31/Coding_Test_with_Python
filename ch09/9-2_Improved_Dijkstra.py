# <개선된 다익스트라 알고리즘>
# 최악의 경우에도 시간 복잡도 O(ElogV)를 보장하는 알고리즘 (E: 간선의 개수, V: 노드의 개수)
# 간단한 다익스트라 알고리즘에서 '최단 거리가 가장 짧은 노드를 선형적으로 찾는 것'을 개선하여 탐색 시간을 줄인 방법
# '힙 자료구조'를 사용하여 특정 노드까지의 최단 거리게 대한 정보를 힙에 담아 처리하므로
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

# ---------------------------------------------------------------------------------------------------------------------
# <힙 자료구조>
# '우선순위 큐'를 구현하기 위하여 사용하는 자료구조 중 하나
# LIFO의 '스택', FIFO의 '큐'와는 달리 '우선순위 큐'는 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다.
# 파이썬에서는 우선순위 큐가 필요할 때 PriorityQueue 혹은 heapq를 사용할 수 있는데, heapq가 더 빠르게 동작하므로 이를 사용하도록 한다.

# 우선순위 값을 표현할 때는 일반적으로 정수형 자료형의 변수가 사용된다.
# 또한 우선순위 큐를 구현할 때는 내부적으로 '최소 힙' 혹은 '최대 힙'을 이용한다.
# 파이썬 라이브러리에서는 기본적으로 최소 힙 구조를 이용하는데 다익스트라 최단 경로 알고리즘에서는 비용이 적은 노드를 우선하여 방문하므로
# 최소 힙 구조를 기반으로 하는 파이썬의 우선순위 큐 라이브러리를 그대로 사용하면 된다.
# 최소 힙을 최대 힙처럼 사용하기 위해서는 우선순위에 해당하는 값에 음수 부호(-)를 붙여 사용하면 된다.

# 힙 자료구조의 전체 연산 횟수에 대한 시간 복잡도는 O(NlogN)
# 힙 정렬 구현 소스코드는 ../appendixA/heapq_lib.py 를 참고하도록 하자.

# ---------------------------------------------------------------------------------------------------------------------
# <동작 원리>
# 최소 힙을 다익스트라 최단 경로 알고리즘에 적용하여 시작 노드로부터 '거리'가 짧은 노드 순서대로 큐에서 나올 수 있도록 할 것이다.
# 최단 거리를 저장하기 위한 1차원 리스트는 '단순한 다익스트라 알고리즘'에서 작성했던 것처럼 하고,
# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다고 보면 된다.

# [step 0]
# 1번 노드가 출발 노드인 경우를 고려해 보자. 출발 노드를 제외한 모든 노드의 최단 거리를 무한으로 설정한다.
# 이후 우선순위 큐에 1번 노드를 넣는다. 1번 노드로 가는 거리는 자기 자신까지 도달하는 거리이기 때문에 0이다.
# 파이썬에서는 간단히 튜플 (0, 1)을 우선순위 큐에 넣는다. (heapq 라이브러리는 튜플이 입력되면 '첫 번째 원소' 기준으로 우선순위 큐를 구성)
#     우선순위 큐: (거리 0:, 노드: 1)
# [step 1]
# 거리가 가장 짧은 노드를 선택하기 위해 우선순위 큐에서 노드를 꺼낸다.
# 우선순위 큐에서 노드를 꺼낸 뒤 해당 노드를 이미 처리한 적이 있다면 무시하면 되고, 아직 처리하지 않은 노드에 대해서만 처리하면 된다.
# 1번 노드 ~ 2번, 3번, 4번 노드의 최소 비용을 계산하고 리스트를 갱신한다. 이렇게 더 짧은 경로를 찾은 노드 정보들을 우선순위 큐에 넣는다.
#     우선순위 큐: (거리: 1, 노드: 4) (거리: 2, 노드 2) (거리: 5, 노드: 3)
# [step 2]
# 우선순위 큐에서 원소를 꺼내서 동일한 과정을 반복한다. (1, 4)의 값을 갖는 원소가 추출된다. 아직 4번 노드를 방문하지 않았으며,
# 현재 최단 거리가 가장 짧은 노드가 4번이다. 따라서 4번 노드를 기준으로 4번 노드와 연결된 간선들을 확인하고 구해진 최소 비용으로
# 리스트와 우선순위 큐를 갱신하면 된다.
#     우선순위 큐: (거리: 2, 노드: 2) (거리: 2, 노드: 5) (거리: 4, 노드: 3) (거리: 5, 노드: 3)
# ... 이하 생략


# ---------------------------------------------------------------------------------------------------------------------
# '단순한 다익스트라 알고리즘'의 소스코드와 비교했을 때 get_smallest_node()라는 함수를 작성할 필요가 없다는 것이 특징이다.
# '최단 거리가 가장 짧은 노드'를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문이다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
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

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, '무한'이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

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

# ---------------------------------------------------------------------------------------------------------------------
# 전체 다익스트라 최단 경로 알고리즘은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사하다고 볼 수 있다.
# 다익스트라 알고리즘의 경우 최대 E개의 간선 데이터를 힙에 넣었다가 다시 빼는 것으로 볼 수 있으므로 O(ElogE)이다.
# 이때 중복 간선을 포함하지 않는 경우, E는 항상 V^2보다 작다. 모든 노드끼리 서로 다 연결되어 있다고 했을 때 간선의 개수를 약 V^2로
# 볼 수 있고 E는 항상 V^2 이하이기 때문이다. 다시 말해 logE < log(V^2) = 2logV, 즉 O(logE) = O(logV)이다.
# 따라서 개선된 다익스트라 알고리즘의 전체 시간 복잡도를 O(ElogV)로 볼 수 있다.

# 다익스트라 최단 경로 알고리즘은 우선순위 큐를 이용한다는 점에서 우선순위 큐를 필요로 하는 다른 문제 유형과도 흡사하다는 특징이 있다.
# 예를 들어 그래프 문제로 유명한 최소 신장 트리 문제를 풀 때에도 일부 알고리즘(Prim 알고리즘)의 구현이 다익스트라 알고리즘의 구현과 비슷하다.