

V,T,S,D = (int(x) for x in input().split())

a = V * T
b = V * S
if(a > D or b < D):
    print("Yes")
else:
    print("No")

