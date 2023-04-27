def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    hanoi(n-1, auxiliary, target, source)


n = int(input('nhap kich thuoc '))
print(hanoi(n,'a','b','c'))