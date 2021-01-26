# '인접 리스트 방식'
# 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
# 파이썬은 기본 자료형인 리스트 자료형이 append()와 메소드를 제공하므로,
# 인접 리스트를 이용해 그래프를 표현하고자 할 때에도 단순히 2차원 리스트를 이용하면 된다.

#         0
#  7--- /   \ --- 5
#      1     2
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)