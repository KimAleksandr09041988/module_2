import random

first = random.randrange(3,21)

def dif(first_):
    list_ = []
    for i in range(1, first_):
        for j in range(1, first_):
            if first_ % (i + j) == 0 and not (i == j) and len(list_) == 0:
                list_.append([i, j])
            elif first_ % (i + j) == 0 and not (i == j) and len(list_) > 0:
                check =True
                for item in list_:
                    if {i, j} == set(item):
                        check = False
                        break
                    else:
                        continue
                if check:
                    list_.append([i, j])
                else:
                    continue
    return list_

def concatenation(list_):
    res = ''
    for item in list_:
        for elem in item:
            res += str(elem)
    return res

result = int(concatenation(dif(first)))
print(first)
print(result)
