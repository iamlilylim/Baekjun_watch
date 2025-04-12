#input
numbers = list(map(int, input().split()))

#analyse (1st: 각 수의 제곱을 sum)
total = 0
for i in numbers:
    total += i ** 2


#output

print(total%10)