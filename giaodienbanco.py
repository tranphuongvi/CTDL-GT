import turtle # vẽ đồ họa theo ý thích

sc = turtle.Screen() #trả về danh sách turtle trên màn hình
cb = turtle.Turtle() #tạo đối tg turle/ tạo nét vẽ

def draw():
    for i in range(4):
        cb.forward(30) #vẽ đoan thang dài 30cm
        cb.left(90) #xoay trái 90độ

    cb.forward(30)


if __name__ == "__main__":

    sc.setup(400, 600)

    cb.speed(100) #tăng tốc độ turle

    for i in range(8):

        cb.up()

        cb.setpos(-100, 30 * i)

        cb.down()

        for j in range(8):

            if (i + j) % 2 == 0: # ô chẵn thì tô màu đen
                col = 'black'

            else:
                col = 'white' # ngc lại thì màu trắng

            cb.fillcolor(col)

            cb.begin_fill()

            draw()
            cb.end_fill()

    cb.hideturtle()
    turtle.done()