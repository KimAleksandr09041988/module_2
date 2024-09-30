first, second, third = int(input('ввежите первое число: ')), int(input('ввежите второе число: ')), int(input('ввежите третье число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)