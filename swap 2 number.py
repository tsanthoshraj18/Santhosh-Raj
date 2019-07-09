x1,y1=map(int,input().split())
temp=0
if(x1>y1) or (x1<y1):
    temp=x1
    x1=y1
    y1=temp
print(x1,y1)