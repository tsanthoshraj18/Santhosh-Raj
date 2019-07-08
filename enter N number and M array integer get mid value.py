import statistics
number=int(input())
lists=list(map(int,input().split()))
lists.sort()
for i in range(number):
    x=statistics.median(lists)
print(x)
