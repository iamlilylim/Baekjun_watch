n = int(input())
numlist = list(input()) #str 받아서 indexing

sum = 0
for i in numlist:
    sum += int(i)

print(sum)
#for i in range(n):
#    sum += int(numlist[i])
#print(sum)