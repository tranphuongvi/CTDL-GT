# mã nguồn tìm ước chung lớn nhất của 2 số
import math
a=int(input('a= '))
b=int(input('b= '))
if b == 0:
    print(a)
else:
    print(math.gcd (b, a % b))


#cách 1: sử dụng tính chất nếu a và b cùng chia hết cho
#một số thì a-b cũng chia hết cho số đó, còn gọi là quy tắc trừ
def uscln(a, b):
    temp1 = a
    temp2 = b
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2
        else:
            temp2 -= temp1
    uscln = temp1
    return uscln
