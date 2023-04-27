def solveKT(n,xstart=0,ystart=0):
# Khởi tạo ma trận bằng 0
  sol = [[-1 for x in range(n)] for y in range(n)]
# Khởi tạo các bước di chuyển của mã
  xmove = [2, 1, -1, -2, -2, -1, 1, 2]
  ymove = [1, 2, 2, 1, -1, -2, -2, -1]
# Đặt quân mã vào ô đầu tiên
  sol[xstart][ystart] = 0
# Bắt đầu di chuyển
  if not solveKTUtil(xstart, ystart, 1 , sol, xmove, ymove):
    print("Không tìm thấy lời giải")
  else:
    print(sol)
# Hàm trợ giúp để giải quyết bài toán Mã đi tuần
def solveKTUtil(x, y, movei, sol, xmove, ymove):
  n = len(sol)
# Nếu tất cả các ô đều đã được thăm, trả về True
  if movei == n*n:
    return True
# Thử các bước di chuyển khác nhau
  for k in range(8):
    next_x = x + xmove[k]
    next_y = y + ymove[k]
    if isSafe(next_x, next_y, sol): #check if this move is safe ie. not out of bound or step into old moves
        sol[next_x][next_y] = movei
        if solveKTUtil(next_x, next_y, movei+1, sol, xmove, ymove): #searching for further move
            return True
        else:
            sol[next_x][next_y] = -1
# Trả về lại giá trị false nếu không tìm thấy giải pháp
  return False
# Hàm kiểm tra xem ô có an toàn để di chuyển hay không
def isSafe(x, y, sol):
  n = len(sol)
  if (x >= 0 and x < n and y >= 0 and y < n and sol[x][y] == -1):
     return True
  return False



