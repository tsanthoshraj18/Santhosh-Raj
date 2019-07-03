n,k=map(int,input().split())
q=list(map(int,input().split()))
p=0
for i in range(k):
    p=p+q[i]
print(p)