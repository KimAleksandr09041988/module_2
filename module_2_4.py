numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in numbers:
    bool_ = True
    for j in range(2, i):
        if i % j == 0:
            bool_ = False
    if bool_:
        print(i)