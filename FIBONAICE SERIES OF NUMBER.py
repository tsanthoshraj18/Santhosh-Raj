a=int(input())
b=1
c=1
d=0
print()
while a!=0:
	b=c
	c=d
	d=b+c
	print(d,end=' ')
	a=a-1