ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
timkiem = [int(i) for i in input("Nhập các số cần tìm (mỗi số cách nhau một dấu cách):").split()]
dem = 0
print("Số lần xuất hiện:")
for i in range(len(timkiem)):
    for j in range(len(ls)):
        if ls[j] == timkiem[i]:
            dem+= 1
    print("(", timkiem[i],",", dem,")")
    dem = 0

demm = []
print("Vị trí các số xuất hiện")
for i in range(len(timkiem)):
    for j in range(len(ls)):
        if ls[j] == timkiem[i]:
            demm.append(j)
    print(timkiem[i],":",demm)
    demm = []