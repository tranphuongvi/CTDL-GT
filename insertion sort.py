def insertion_sort(arr):  # định nghĩa hàm sắp xếp chèn với tham số truyền vào là một danh sách số nguyên arr.
    for i in range(1, len(arr)):  # duyệt qua từng phần tử của danh sách arr, bắt đầu từ phần tử thứ hai.
        key = arr[i]  # lưu giá trị của phần tử hiện tại vào biến key.
        j = i - 1   # khởi tạo biến j có giá trị là chỉ số của phần tử liền trước phần tử hiện tại.
        while j >= 0 and arr[j] > key:  #  thực hiện vòng lặp cho đến khi j bằng hoặc nhỏ hơn 0 hoặc phần tử tại arr[j] nhỏ hơn hoặc bằng giá trị của key.
            arr[j + 1] = arr[j]    #  di chuyển phần tử tại chỉ số j sang phải một bậc để cấp cho phần tử key.
            j -= 1   # giảm giá trị của j xuống để tiếp tục kiểm tra các phần tử trước đó.
        arr[j + 1] = key   #  gán giá trị của key cho phần tử ngay sau phần tử tại chỉ số j.

# Sử dụng hàm insertion_sort để sắp xếp danh sách các số nguyên
arr = [5, 2, 8, 12, 1, 7, 3]
insertion_sort(arr)  #  chạy hàm insertion_sort với danh sách số nguyên arr
print(arr)  # in ra kết quả sau khi sắp xếp danh sách: [1, 2, 3, 5, 7, 8, 12]