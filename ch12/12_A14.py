from itertools import permutations

def solution(n, weak, dist):
    # '원형'으로 나열된 데이터를 길이를 2배 늘려 '일자' 형태로
    len_weak = len(weak)
    for i in range(len_weak):
        weak.append(weak[i] + 12)
    # 모든 친구를 나열하는 경우의 수
    per = list(permutations(dist, len(dist)))
    # 초기 answer 값은 주어진 친구 수보다 하나 더 큰 수로
    answer = len(dist) + 1
    # 모든 취약 지점을 하나씩 확인
    for w in range(len_weak):
        # 친구를 한 명씩 투입하여 확인
        for p in per:
            # 투입할 친구의 수
            count = 1
            # 해당 친구는 각 취약 지점부터 자신이 확인 가능한 거리까지 체크
            check = weak[w] + p[count - 1]
            # 시작 위치부터 모든 취약 지점 확인
            for i in range(w, w + len_weak):
                # 점검 후 남은 취약 지점이 있다면 한 명 더 추가
                if check < weak[i]:
                    count += 1
                    # 모든 친구를 불렀음에도 점검을 다 하지 못했다면
                    if count > len(dist):
                        break
                    # 시작 위치 변경
                    check = weak[i] + p[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
    
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))

#n = 12
#weak = [1, 3, 4, 9, 10]
#dist = [3, 5, 7]
#print(solution(n, weak, dist))
