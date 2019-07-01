from tkinter import *

root = Tk()
cv = Canvas(root, bg='white', width=200, height=100)

# 指定矩形的填充色为红色，边框宽度为2
cv.create_rectangle(10, 10, 110, 110, width=2, fill='red')
# 指定举行的边框颜色为绿色,
cv.create_rectangle(120, 20, 180, 80, outline='green')
cv.pack()
root.mainloop()
