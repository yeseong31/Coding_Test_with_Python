# 뱀

# 보드의 크기 n x n
n = int(input())
board = [[0] * n for _ in range(n)]

# 사과의 위치
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 1

# 뱀의 방향 변환 횟수
l = int(input())
array = []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 동 남 서 북
for _ in range(l):
    s, d = map(str, input().split())
    array.append((int(s), d))


def turn(step, c):
    # 방향 전환(좌회전)
    if c == 'L':
        step = (step - 1) % 4
    else:
        step = (step + 1) % 4
    return step


# 뱀의 총 이동 시간
def solution():
    x, y = 1, 1     # 초기 뱀 위치
    step = 0        # 초기 뱀의 이동 방향(동쪽)
    second = 0      # 시간 측정
    idx = 0         # 회전할 정보
    board[x][y] = 2 # 뱀의 위치는 '2'로 표기
    q = [(1, 1)]

    while True:
        # 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
        nx = x + direction[step][0]
        ny = y + direction[step][1]
        q.append((nx, ny))
        # 뱀이 벽에 부딪히게 되면 게임 종료, 뱀의 머리가 자신의 몸통과 만났을 때에도 게임 종료
        if (nx < 1 or nx > n or ny < 1 or ny > n) and board[nx][ny] != 2:
            second += 1
            return second
        # 사과가 없다면, 이동 후에 꼬리 제거
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            board[px][py] = 0
        # 사과가 있다면 이동 후에 꼬리 그대로 두기
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            q.append((nx, ny))

        x, y = nx, ny
        second += 1
        # 시간이 다 되면 회전
        if idx < 1 and second == array[idx][0]:
            step = turn(step, array[idx][1])
            idx += 1
    return second


print(solution())

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D