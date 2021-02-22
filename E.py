import heapq

N, M = map(int, input().split())

route = [{} for _ in range(N)]

for i in range(M):
    A, B, C = map(int, input().split())

    A -= 1
    B -= 1

    route[A][B] = min(C, route[A].get(B, float('inf')))
#ダイクストラ法
for j in range(N):
    hq = [(0, j)]

    seen = [0] * N

    dist = [float('inf')] * N

    while hq:
        p, q = heapq.heappop(hq)

        if dist[q] < p:
            continue
        if seen[q]:
            break

        seen[q] = 1

        for k in route[q]:
            if(k == j or not seen[k]) and p + route[q][k] < dist[k]:
                dist[k] = p + route[q][k]

                heapq.heappush(hq, (dist[k], k))

    print(-1 if dist[j] == float('inf') else dist[j])
