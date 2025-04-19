a = int(input())
b = int(input())
c = int(input())

d = list(str(a*b*c)) # 세 수를 곱해서 리스트로 만듦

cnt =[0]*9
for i in d:
    cnt[int(i)] += 1

print(cnt)

for i in cnt:
    print(i)