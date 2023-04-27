import pygame, process
from pygame.locals import*

pygame.int()
FPS = 30 #tốc độ khung hình
fpsClock = pygame.time.Clock() # Xây dựng giao diện

wScr, hScr = (800,660)  #thiết kế hàng dọc hàng ngang
win = pygame.display.set_mode((wScr, hScr))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('image/icon.png'))

#-------Get Image----------{
broadIMG = pygame.image.load('image/chess.jpg')
pos = pygame.image.load('image/pos.png')

knight = pygame.image.load('image/knight.png')


def is_valid_move(x, y, board):
    # Kiểm tra xem ô (x, y) trên bàn cờ có phải là ô hợp lệ hay không
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False
    if board[x][y] != -1:
        return False
    return True


def knight_tour_helper(x, y, move_count, board, x_move, y_move):
    if move_count == len(board) * len(board[0]):
        # Nếu đã đi hết tất cả các ô trên bàn cờ, trả về True để kết thúc thuật toán
        return True

    for i in range(8):
        next_x = x + x_move[i]
        next_y = y + y_move[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if knight_tour_helper(next_x, next_y, move_count + 1, board, x_move, y_move):
                return True
            board[next_x][next_y] = -1
    return False


def knight_tour():
    # Khởi tạo bàn cờ 5x5 với tất cả các ô chưa được đi qua (-1)
    board = [[-1 for j in range(5)] for i in range(5)]
    # Khởi tạo vị trí ban đầu của quân mã tại ô (0, 0) và đếm số lần di chuyển
    x, y = 0, 0
    move_count = 0
    # Tạo các bước di chuyển của quân mã
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    # Đánh dấu ô ban đầu đã được đi qua
    board[x][y] = move_count
    # Gọi đệ quy để tìm kiếm lời giải
    if knight_tour_helper(x, y, move_count + 1, board, x_move, y_move):
        # In ra bàn cờ với lời giải
        for row in board:
            print(row)
    else:
        print("Không tìm thấy lời giải")


# Chạy thuật toán để tìm kiếm lời giải
knight_tour()
