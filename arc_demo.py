from tkinter import *
root = Tk()
cv = Canvas(root, bg='white')
# 使用默认参数创建一个圆弧，结果为90°的扇形
cv.create_arc((10, 10, 110, 110),)

# 扇形，弓形，弧形
d = {1: PIESLICE, 2: CHORD, 3: ARC}

for i in d:
    # 使用3种样式分别创建3种图形
    cv.create_arc((10, 10 + 60 * i, 110, 110 + 60 * i), style=d[i])
    print(i, d[i])


# 指定起始角度和角度偏移量（逆时针）
# start 影响的是角度起始绘制位置。
# extent。基于start度数为基准的度数。也就是最终度数。
# 例如这个例子就是初始为10度角。然后逆时针把这个扇形角度扩展到180度,
# 顺时针使用负数既可
cv.create_arc((150, 150, 250, 250),
              start=10,
              extent=120)

cv.pack()
root.mainloop()
