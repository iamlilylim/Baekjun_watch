n = int(input())
if n%4 == 0 and n%100 != 0 or n%400 ==0:
    print(1)
else:
    print(0)

#관계연산자 >, >=, <, <=, ==, !=
#논리연산자  and or not
#if((n%4 == 0) and (n%100 != 0) or (n%400 == 0)):
 #    print('1')
#else:
 #  print('0')

#print('1') if ((n%4 == 0) and (n%100 != 0)) or (n%400 == 0) else print('0')