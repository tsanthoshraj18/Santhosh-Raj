san = int(input())
t = list(map(int,input().split()))
t.sort()
for i in range(san):
  print(t[i],end=" ")