from tkinter import *
root = Tk()
cv = Canvas(root)
# 把指定图片绘制到画板
img1 = PhotoImage(file="img/bar_00.png")
img2 = PhotoImage(file="img/bar_01.png")
img3 = PhotoImage(file="img/bar_02.png")
cv.create_image((100, 100), image=img1)
cv.create_image((200, 100), image=img2)
cv.create_image((300, 100), image=img3)

# python内置的位图名称
d = {1: 'error',
     2: 'info',
     3: 'question',
     4: 'hourglass',
     5: 'questhead',
     6: 'warning',
     7: 'gray12',
     8: 'gray25',
     9: 'gray50',
     10: 'gray75'}

cv.create_bitmap((10, 220), bitmap=d[1])

for i in d:
    cv.create_bitmap((20 * i, 20), bitmap=d[i])
cv.pack()
root.mainloop()
