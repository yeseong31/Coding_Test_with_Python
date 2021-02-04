# 모험가 길드

# 공포도를 오름차순으로 정렬하여, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하도록 하면 된다.
# 이는 최대한 많은 그룹이 구성되는 방법이므로, 항상 최적의 해를 찾을 수 있다.

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1          # 현재 그룹에 해당 모험가를 포함시킴
    if count >= i:      # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1     # 총 그룹의 수 증가시키기
        count = 0       # 현재 그룹에 포함된 모험가의 수 초기화

print(result)