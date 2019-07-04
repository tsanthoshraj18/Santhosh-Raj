per,mov=map(int,input().split())
for k in range(per+1,mov):
  c=k
  fd=0
  while (k>0):
    r=k%10
    fd=fd+(r**3)
    k=k//10
    if(fd==c):
      print(fd,end=" ")