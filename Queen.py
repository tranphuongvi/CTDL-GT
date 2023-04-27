def solve_n_queens(n):
    # Khởi tạo bàn cờ
    board = [['.' for i in range(n)] for j in range(n)]

    # Thực hiện giải quyết bài toán
    if solve_n_queens_helper(n, board, 0) == False:
        print("Không tìm thấy giải pháp!")
    else:
        print_board(board)


def solve_n_queens_helper(n, board, row):
    # Nếu đã đặt hậu được n quân thì trả về True
    if row == n:
        return True

    # Thử các vị trí cho quân hậu trên hàng hiện tại
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            # Nếu có giải pháp, trả về True
            if solve_n_queens_helper(n, board, row + 1) == True:
                return True

            # Nếu không có giải pháp, quay lại và thử các vị trí khác
            board[row][col] = '.'

    return False


def is_safe(board, row, col):
    n = len(board)

    # Kiểm tra hàng ngang
    for i in range(n):
        if board[row][i] == 'Q':
            return False

    # Kiểm tra cột dọc
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Kiểm tra đường chéo trái
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Kiểm tra đường chéo phải
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def print_board(board):
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    print(solve_n_queens(8))

