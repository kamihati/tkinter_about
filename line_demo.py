from tkinter import *
root = Tk()
cv = Canvas(root, bg='white', width=200, height=100)
# 绘制没有箭头的线段
cv.create_line(10, 10, 100, 10, arrow='none')
# 绘制起点有箭头的线段
cv.create_line(10, 20, 100, 20, arrow='first')
# 绘制终点有箭头的线段
cv.create_line(10, 30, 100, 30, arrow='last')
# 绘制两端有箭头的线段
cv.create_line(10, 40, 100, 40, arrow='both')
# 绘制虚线
cv.create_line(10, 50, 100, 100, width=3, dash=7)

cv.pack()
root.mainloop()
