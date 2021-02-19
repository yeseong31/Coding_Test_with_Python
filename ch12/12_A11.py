# 보드의 크기 n
n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
# 사과의 개수
k = int(input())
# 사과의 위치('1'로 표기)
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1
# 뱀의 방향 전환 횟수
l = int(input())
# 뱀의 방향 전환 정보
arr = []
for _ in range(l):
    x, c = input().split()
    arr.append((int(x), c))

# 방향 좌표(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 전환 함수
def rotation(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    return (direction + 1) % 4

x, y = 1, 1     # 뱀의 처음 시작 위치
board[x][y] = 2 # 뱀의 위치는 '2'로 표기
d = 0           # 뱀의 처음 시작 방향
sec = 0         # 게임 경과 시간
count = 0       # 회전 횟수
q = [(1, 1)]    # 초기의 뱀의 머리 좌표

while True:
    # 몸길이를 늘려 머리를 다음 칸에 위치
    nx = x + dx[d]
    ny = y + dy[d]
    sec += 1
    # 단, 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남
    if (nx < 1 or nx > n or ny < 1 or ny > n) or board[nx][ny] == 2:
        break
    # 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
    if board[nx][ny] != 1:
        board[nx][ny] = 2
        pop_x, pop_y = q.pop(0)
        board[pop_x][pop_y] = 0
    q.append((nx, ny))
    x, y = nx, ny
    # 방향을 전환할 때인지 확인
    if count < l and sec == arr[count][0]:
        d = rotation(d, arr[count][1])
        count += 1
        
print(sec)
