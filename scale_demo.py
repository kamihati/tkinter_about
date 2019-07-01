"""
缩放图形
"""

from tkinter import *
root = Tk()
cv = Canvas(root, bg='white', width=200, height=300)
rt1 = cv.create_rectangle(10, 10, 110, 110, outline='red', stipple='gray12', fill='green')
cv.pack()

rt2 = cv.create_rectangle(10, 10, 110, 110, outline='green', stipple='gray12', fill='red')

# y方向方法一倍
cv.scale(rt1, 0, 0, 1, 2)

# 缩小一半大小
cv.scale(rt2, 0, 0, 0.5, 0.5)

cv.pack()
root.mainloop()
