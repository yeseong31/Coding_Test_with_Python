# 열쇠를 시계 방향으로 90도 회전하는 함수
def rotation(key, m):
    ret = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            ret[c][m - 1 - r] = key[r][c]
    return ret

# 자물쇠의 '중앙' 부분만을 확인하는 함수
def check(lock):
    lock_len = len(lock) // 3
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if lock[i][j] != 1:
                return False
    return True

# 자물쇠에 열쇠를 대입하면서 확인
def solution(key, lock):
    # 자물쇠 및 열쇠의 한 변의 길이 n, m
    n, m = len(lock), len(key)
    # 자물쇠 확장
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 자물쇠의 중앙 부분에 기존의 자물쇠 형태 삽입
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    # 한 칸씩 이동하며 자물쇠와 열쇠가 맞물리는지 확인
    for i in range(n * 2):
        for j in range(n * 2):
            # 돌려가면서 확인
            for _ in range(4):
                key = rotation(key, m)
                for a in range(m):
                    for b in range(m):
                        new_lock[i + a][j + b] += key[a][b]
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for a in range(m):
                    for b in range(m):
                        new_lock[i + a][j + b] -= key[a][b]
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
