from tkinter import *
import os

import canvas as canvas
from PIL import ImageTk


path_dir = "ImageBasic"
file_list = os.listdir(path_dir)
real_file_list = [x for x in file_list if(x.endswith(".JPG") or (x.endswith(".jpg")==True))]
print(real_file_list)

xn=0
root=Tk()
root.title("FaceList")
root.geometry("800x450+0+0")
root.resizable(0, 0)
image=ImageTk.PhotoImage(file="ImageBasic/" + real_file_list[xn])

def showimg():
	global xn
	global image
	xn+=1
	if(xn>=len(real_file_list)):
		xn=0
	image=ImageTk.PhotoImage(file="ImageBasic/" + real_file_list[xn])
	# canvas.create_image(20, 20, image=image, anchor=NW)
	label_2 = Label(root, image=image)
	label_2.place(x=210,y=100)

def quitFaceList():
	root.destroy()

btn = Button(root,text="다른사진보기",command=showimg,width=10,height=2)
label_1 = Label(root,text="등록된 얼굴",font="NanumGothic 20")
label_2 = Label(root, image=image)
label_1.place(x=340,y=10)
label_2.place(x=210,y=100)
btn.place(x=370,y=50)



quitBtn = Button(root, text="X", height=2, width=4, command=quitFaceList)
quitBtn.place(x=15, y=10)


print(xn)
root.mainloop()