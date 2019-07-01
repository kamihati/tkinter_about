from tkinter import *
root = Tk()
cv = Canvas(root, bg='white', width=200, height=100)
# anchor: 文字对象的位置,w左对齐,e右对齐,n顶对齐,s底对齐,nw左上对齐,sw左下对齐,se右下对齐,ne右上对齐,center居中对齐,默认center
# justify: 设置文本对齐方式: left，左对齐,right右对齐，center居中,默认居中(和anchor的区别?未发现
cv.create_text((10, 10), text='Hello Python', fill='red', anchor='nw')
cv.create_text((200, 50), text='你好 Python', fill='blue', anchor='se')

txt = cv.create_text((10, 80), text='中原工学院计算机学院', fill='red', anchor='nw')
# 设置文本的起始位置
cv.select_from(txt, 5)
# 设置选中文本的结束位置(选中计算机学院五个字)
cv.select_to(txt, 9)
cv.pack()
root.mainloop()
