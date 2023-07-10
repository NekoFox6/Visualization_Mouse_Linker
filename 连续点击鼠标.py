from pynput.mouse import Button, Controller
from PIL import ImageTk, Image
import time
import os
import tkinter as tk
mouse = Controller()
def click_left_button(duration):
    time.sleep(1)
    end_time = time.time() + duration
    while time.time() < end_time:
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.01)  # 可根据需要调整点击间隔时间
    print("鼠标左键执行完毕")

def click_right_button(duration):
    time.sleep(1)
    end_time = time.time() + duration
    while time.time() < end_time:
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.01)  # 可根据需要调整点击间隔时间
    print("鼠标右键执行完毕")

def mr():
    a1=int(entry1.get())
    click_right_button(1)
    click_right_button(a1)
    result_label.config(text="成功执行了"+str(a1)+"秒")
def ml():
    a1=int(entry1.get())
    click_left_button(a1)
    result_label.config(text="成功执行了"+str(a1)+"秒")
    
window = tk.Tk()
window.title("连点程序的测试")

# 创建大标题标签
title_label = tk.Label(window, text="连点器",font=("Arial", 16, "bold"))
base_path=os.path.dirname(os.path.abspath(__file__));imagename="cat.gif"
imagepath=os.path.join(base_path,imagename)

# 创建按钮
button1 = tk.Button(window, text="点击鼠标右键", command=mr)
button2 = tk.Button(window, text="点击鼠标左键", command=ml)

default_value = tk.IntVar(value=1)

label1 = tk.Label(window, text="输入时间(默认1秒)")
entry1 = tk.Entry(window,textvariable=default_value)

# 创建标签用于显示结果
result_label = tk.Label(window, text="执行结果:")

# 将组件放置在窗口上
title_label.pack(pady=10)
if os.path.exists(imagepath):
    image=Image.open(imagepath)
    imagewidth=300;imageheight=300;image=image.resize((imagewidth,imageheight))
    photo=ImageTk.PhotoImage(image)
    labelimage=tk.Label(window,image=photo)
    labelimage.pack()
else:
    labelimage=tk.Label(window,text="图片丢失")
    labelimage.pack()
label1.pack()
entry1.pack()
button1.pack()
button2.pack()
result_label.pack()

# 进入消息循环
window.mainloop()