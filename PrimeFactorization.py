import math
def f(n):
    lists = []
    store = n
    while n%2 == 0:
        n = n/2
        lists.append(2)
    for i in range(3,math.ceil((store/2)+1)):
        if n == 1:
            break
        while n%i == 0:
            n = n/i
            lists.append(i)
    storel = lists.copy()
    lists.clear()
    before = 0
    for x in storel:
        if before == x:
            continue
        count = storel.count(x)
        if count > 1:
            lists.append(str(x)+"^"+str(count))
        else:
            lists.append(str(x))
        before = x
    return " * ".join(lists)
