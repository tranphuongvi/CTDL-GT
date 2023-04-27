w = int(input("Nhập số phần tử của dãy số : "))
v = []
for i in range(w):
   a = int(input('Nhập một số: '))
   v.append(a)
print('dãy số nguyên',v)
n=len(v)
for i in range(0, n - 1):
  for j in range(i+1, n):
    if v[i] > v[j]:
      v[i], v[j] = v[j], v[i]
print('sắp xếp',v)

#tìm kiếm
b = int(input('Nhập slg số cần tìm: '))
x = []
for i in range(b):
    x1 = int(input("Nhập phần tử cần tìm của dãy số : "))
    x.append(x1)
count = 0
vitri = []
for i in range(len(v)):
    if v[i] == x:
        vitri.append(i)
        count += 1
print('so lan xuat hien')
print(len(vitri))
print('vi tri xuat hien')
print(vitri)
if count == 0:
    print('không tìm thấy số n')
