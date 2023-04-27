def giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua
print(' giá trị phép tính giai thừa là ', giai_thua(5))
