#https://atcoder.jp/contests/abc191/tasks/abc191_b

N,X = (int(x) for x in input().split())




seisuu = list(map(int, input().split()))

for i in seisuu:
    if(i != X):
        print(i, end=' ')

