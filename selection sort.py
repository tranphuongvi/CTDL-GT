def selection_sort(arr):
    for i in range(len(arr)): # duyệt qua từng phần tử trong danh sách arr để tìm kiếm phần tử nhỏ nhất trong đoạn chưa được sắp xếp.
        # Tìm phần tử nhỏ nhất trong đoạn chưa được sắp xếp
        min_idx = i #  đại diện cho chỉ số của phần tử nhỏ nhất trong đoạn chưa được sắp xếp, ban đầu được gán bằng giá trị của biến i.
        for j in range(i + 1, len(arr)): # duyệt qua các phần tử của đoạn chưa được sắp xếp, bắt đầu từ vị trí ngay sau phần tử đang xét (i + 1).
            if arr[j] < arr[min_idx]:  # Nếu phần tử đang xét (arr[j]) nhỏ hơn phần tử nhỏ nhất hiện tại (arr[min_idx])
                min_idx = j  #  ta cập nhật lại chỉ số của phần tử nhỏ nhất

        # Sau khi tìm được phần tử nhỏ nhất trong đoạn chưa được sắp xếp, ta đổi chỗ phần tử này với phần tử đầu tiên của đoạn chưa được sắp xếp
        # (arr[i], arr[min_idx] = arr[min_idx], arr[i]), để đảm bảo rằng phần tử nhỏ nhất được đưa về đầu danh sách.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Sử dụng hàm selection_sort để sắp xếp danh sách các số nguyên
arr = [5, 2, 8, 12, 1, 7, 3]
selection_sort(arr)  # đoạn code arr = [5, 2, 8, 12, 1, 7, 3], selection_sort(arr),
print(arr)   # print(arr) được sử dụng để kiểm tra kết quả của thuật toán.
# Bạn sẽ thấy rằng danh sách các số nguyên ban đầu [5, 2, 8, 12, 1, 7, 3] đã được sắp xếp lại thành [1, 2, 3, 5, 7, 8, 12].