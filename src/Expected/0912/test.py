from collections import deque

R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
maze = [list(input()) for h in range(R)]

sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1

dist = [[10**4 for i in range(C)] for j in range(R)] # 各マスの最小手数

for r in range(R):
    for c in range(C):
        if maze[r][c] == '#':
            dist[r][c] = -1 # 壁は-1

dist[sx][sy] = 0

que = deque()
que.append([sx, sy])
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 移動方向のリスト

# 幅優先探索
while que:
    x, y = que.popleft() # キューから取り出し

    # 現在位置から上下左右に探索
    for i, j in d:
        if x+i >= R or x+i < 0 or y+j >= C or y+j < 0: # 範囲外
            continue
        if maze[x+i][y+j] == '#': # 壁
            continue
        if dist[x+i][y+j] != 10**4: # すでに最小手数確定済み
            continue

        dist[x+i][y+j] = dist[x][y] + 1

        que.append([x+i, y+j]) # 次のマスをキューに格納

print(dist[gx][gy])