def bubble_sort(arr):  # Đây là khai báo hàm bubble_sort nhận đối số là một danh sách các số nguyên.
    n = len(arr)   # Biến n được gán với độ dài của danh sách arr.
    # Duyệt qua danh sách n - 1 lần
    for i in range(n-1):  # Vòng lặp này sẽ duyệt qua danh sách arr từ 0 đến n-2.
        # Vòng lặp này có nhiệm vụ làm cho phần tử lớn nhất "nổi" lên trên cùng của danh sách.
        # Duyệt qua từng cặp phần tử liền kề và đổi chỗ nếu cần thiết
        for j in range(0, n-i-1):  # Vòng lặp này sẽ duyệt qua từng cặp phần tử liền kề của danh sách.
            # Vòng lặp này có nhiệm vụ so sánh các phần tử liền kề và đổi chỗ nếu cần thiết.
            if arr[j] > arr[j+1]:  # Nếu phần tử thứ j lớn hơn phần tử thứ j+1, thì hai phần tử này sẽ được đổi chỗ.
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Dòng này đổi chỗ hai phần tử arr[j] và arr[j+1].

# Sử dụng hàm bubble_sort để sắp xếp danh sách các số nguyên
arr = [5, 2, 8, 12, 1, 7, 3]  # Đây là khởi tạo danh sách arr.
bubble_sort(arr)  # Gọi hàm bubble_sort để sắp xếp danh sách arr.
print(arr)  # In ra danh sách đã sắp xếp: [1, 2, 3, 5, 7, 8, 12]