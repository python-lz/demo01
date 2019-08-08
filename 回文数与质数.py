##
result = []
for a in range(1,100000):
    b = str(a)
    list1 = list(b)
    list2 = list1.copy()
    list2.reverse()
    if list1 == list2:
        result.append(b)
result2 = []
#筛选质数
for n in result:
    s = int(n)
    for num in range(2,s):
        if s%num ==0:
            break
        if num == s-1:
            result2.append(n)
print(result2)
