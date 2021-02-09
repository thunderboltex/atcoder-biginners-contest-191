H,W = map(int,input().split()) 

a = [input() for _ in range(H)]

ans = 0

for i in range(W - 1):
    for j in range(H - 1):
        count = 0

        if a[j][i] == '.':
            count += 1
        if a[j + 1][i] == '.':
            count += 1
        if a[j][i + 1] == '.':
            count += 1
        if a[j + 1][i + 1] == '.':
            count += 1

        if count == 1 or count == 3:
            ans += 1

print(ans)

        




    

