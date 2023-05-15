def quick_sort(arr):
    if len(arr) <= 1:   # Nếu danh sách chỉ có 0 hoặc 1 phần tử, trả về danh sách đó
        return arr
    else:
        pivot = arr[0]   # Chọn phần tử đầu tiên của danh sách làm pivot
        left = []        # Khởi tạo danh sách các phần tử nhỏ hơn pivot
        right = []       # Khởi tạo danh sách các phần tử lớn hơn pivot
        for i in arr[1:]: # Duyệt từ phần tử thứ 2 đến cuối danh sách
            if i < pivot: # Nếu phần tử hiện tại nhỏ hơn pivot, thêm vào danh sách left
                left.append(i)
            else:         # Ngược lại, thêm vào danh sách right
                right.append(i)
        # Đệ quy gọi hàm quick_sort cho danh sách left và right, sau đó nối kết kết quả với pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

# Sử dụng hàm quick_sort để sắp xếp danh sách các số nguyên
arr = [5, 2, 8, 12, 1, 7, 3]
arr = quick_sort(arr)
print(arr)