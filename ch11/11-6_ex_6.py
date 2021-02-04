import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    queue = []
    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i + 1))

    cycle = len(queue)
    sum_time = 0
    prev = 0

    while k >= (queue[0][0] - prev) * cycle + sum_time:
        cur = heapq.heappop(queue)[0]
        sum_time += ((cur - prev) * cycle)
        cycle -= 1
        prev = cur

    result = sorted(queue, key=lambda x: x[1])
    return result[(k - sum_time) % len(queue)][1]


food_times = [8, 6, 4]
k = 15
print(solution(food_times, k))
