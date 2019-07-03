o=input()
o=o.split()
st=int(o[0])
end=int(o[1])
for i in range(st+1,end+1):
  if(i%2!=0):
    print(i, end=' ')