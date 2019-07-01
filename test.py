"""
1. 绘制直线
2. 绘制矩形
3. 设置tag
4. 根据tag获取图形对象
5. 设置对象边框
"""

from tkinter import *

# 初始化窗体
root = Tk()

# 在窗体内初始化画布。窗体尺寸改变默认并不会影响画布尺寸.
cv = Canvas(root, bg='white', width=400, height=300)
# 绘制直线
line_1 = cv.create_line(10, 10, 100, 80, width=2, dash=7, tags=("l1", 'r2', "l3"))

rt = cv.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))

result = cv.find_withtag('r2')
# tuple
print(type(result))
# 2。tag可重复使用
print(len(result))

# 显示画布
cv.pack()

# r3 为tag的第二个矩形
cv.create_rectangle(20, 20, 80, 80, tags='r3')

# 设置对应item边框的颜色为蓝色
for item in cv.find_withtag('r3'):
    cv.itemconfig(item, outline='blue')

root.mainloop()
