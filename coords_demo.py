"""
图形坐标操作
"""

from tkinter import *
root = Tk()
cv = Canvas(root)
# 把指定图片绘制到画板,
img1 = PhotoImage(file="img/bar_00.png")
img2 = PhotoImage(file="img/bar_01.png")
img3 = PhotoImage(file="img/bar_02.png")
rt1 = cv.create_image((100, 100), image=img1)
rt2 = cv.create_image((200, 100), image=img2)
rt3 = cv.create_image((300, 100), image=img3)

# 重新设置坐标，不能缩放
cv.coords(rt2, (200, 500))

# 正方形对象,可以缩放
rt4 = cv.create_rectangle(20, 140, 110, 220, outline='red', fill='green')
cv.coords(rt4, (100, 150, 300, 200))


cv.pack()
root.mainloop()
