sen=input()
count=0
for i in range(0,len(sen)):
    if(sen[i].isdigit()==1):
        count=count+1
print(int(count))