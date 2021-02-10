# 기둥과 보 설치

# 조건을 만족하는지 확인하는 함수
# 1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
# 2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
def check(answer):
    for ans in answer:
        x, y, a = ans
        # 기둥 체크
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer \
                    or [x, y-1, 0] in answer:
                continue
            return False
        # 보 체크
        elif a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer \
                    or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame  # x, y: 좌표 / a: 기둥(0), 보(1) / b: 삭제(0), 설치(1)
        if b == 0:
            answer.remove([x, y, a])    # 일단 삭제해 보고
            if not check(answer):
                answer.append([x, y, a])  # 불가능하다면 원래대로
        else:
            answer.append([x, y, a])    # 일단 설치해 보고
            if not check(answer):
                answer.remove([x, y, a])    # 불가능하다면 원래대로

    answer.sort()
    return answer


n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

# n = 5
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))

# build_frame의 원소는 [x, y, a, b]의 형태이다.
#     x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표
#     a는 설치 또는 삭제할 구조물의 종류. 0은 기둥, 1은 보
#     b는 구조물을 설치할 지, 혹은 삭제할 지를 나타냄. 0은 삭제, 1은 설치
