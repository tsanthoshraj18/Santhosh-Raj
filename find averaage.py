num = int(input())
total_sum = 0
for n in range(num):
    numbers = int(input())
    total_sum += numbers
avg = int(total_sum/num)
print(avg)