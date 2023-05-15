def heapify(arr, n, i):
    # Khởi tạo chỉ số phần tử lớn nhất là i
    largest = i
    # Tính chỉ số của nút con bên trái
    l = 2 * i + 1
    # Tính chỉ số của nút con bên phải
    r = 2 * i + 2

    # So sánh giá trị của nút con bên trái và phần tử lớn nhất
    # Nếu giá trị của nút con lớn hơn phần tử lớn nhất, gán largest = l
    if l < n and arr[i] < arr[l]:
        largest = l

    # So sánh giá trị của nút con bên phải và phần tử lớn nhất
    # Nếu giá trị của nút con lớn hơn phần tử lớn nhất, gán largest = r
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Nếu phần tử lớn nhất khác với chỉ số ban đầu của nó (i)
    # Hoán đổi giá trị của phần tử lớn nhất và phần tử hiện tại (arr[i])
    # Và tiếp tục đệ qui để kiểm tra tính chất heap của cây con
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr): # Định nghĩa hàm heapSort(arr) nhận vào một mảng arr cần sắp xếp.
    n = len(arr)   # Khởi tạo biến n với giá trị bằng độ dài của mảng arr.
    for i in range(n // 2 - 1, -1, -1):  # Lặp từ phần tử cuối cùng trong nửa đầu của mảng cho đến phần tử đầu tiên để xây dựng một heap hợp lệ với cây gốc tại vị trí i.
        heapify(arr, n, i)  # Gọi hàm heapify(arr, n, i) để xây dựng một heap hợp lệ tại vị trí i trong mảng arr.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Lặp từ phần tử cuối cùng của mảng đến phần tử đầu tiên và hoán đổi phần tử đầu tiên với phần tử cuối cùng của mảng.
        heapify(arr, i, 0)  # Gọi hàm heapify(arr, i, 0) để xây dựng một heap hợp lệ tại vị trí 0 trong mảng arr.x`


arr = [12, 11, 13, 5, 6, 7]   # Khởi tạo một mảng arr với các giá trị đã cho.
heapSort(arr)  # Gọi hàm heapSort(arr) để sắp xếp mảng arr theo thứ tự tăng dần bằng thuật toán Heap Sort.
n = len(arr)  # Lấy độ dài của mảng arr bằng hàm len() và gán vào biến n.
print("Sorted array is")  # In ra chuỗi "Sorted array is".
for i in range(n):  # Sử dụng vòng lặp for để duyệt qua từng phần tử trong mảng.
    print("%d" % arr[i])  # Trong mỗi lần lặp, in ra giá trị của phần tử tại vị trí i trong mảng arr.
    # Việc định dạng giá trị được hiển thị trong chuỗi thông qua phương thức %d.