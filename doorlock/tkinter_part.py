"""
    Tkinter, Pillow - 디스플레이

    최종 수정일 : 2021/08/07
    작성자 : 한규, 박주영
    최종 수정 내용 : 전체적인 코드에 주석 추가
"""
# 화면 구성을 위한 Tkinter
import tkinter.font as tkFont
from tkhtmlview import HTMLLabel
from tkinter import *

import openWeatherMap # OpenWeatherMap.py 가져옴

from PIL import ImageTk, Image # 이미지 처리를 위한 Pillow
import cv2 as cv # 영상처리를 위한 OpenCV
import os

# 날짜와 시간을 가져오는 datatime / time
import time



text = openWeatherMap.city

"""

    함수및 이벤트 정의
    (Function and Event Definition)

"""


def transDay(day): # 숫자로 받아온 요일을 한글로 변경
    if day == 0:
        return "월"
    elif day == 1:
        return "화"
    elif day == 2:
        return "수"
    elif day == 3:
        return "목"
    elif day == 4:
        return "금"
    elif day == 5:
        return "토"
    else:
        return "일"

def getWeather(text): # 화면에 날씨를 나타내주는 부분

    now = time.localtime() # 오늘 날짜를 가져옴
    city = openWeatherMap.weather(text) # OpenWeatherMap.py애서 도시 이름을 가져옴

    # 화면에 나타낼 정보를 선언
    msg = f"""
{now.tm_year}-{now.tm_mon}-{now.tm_mday} / {transDay(now.tm_wday)}

도시 : {city[0]}

최저온도 : {city[2]}°C

최고온도 : {city[3]}°C

습도 : {city[4]}%

    날씨 : {city[1]}
            """

    label['text'] = msg
    win.update()

def add_Face(event): # 얼굴 등록 이벤트
    newf = Tk() # 얼굴 등록 창을 만들어줌

    newf.title("Add Face") # 창의 이름을 Add Face로 설정
    newf.geometry('800x450+0+0') # 창의 크기를 800x450, 위치를 0,0으로 설정
    newf.resizable(False, False) # 창의 크기 변경 불가

    frm = Frame(newf, bg="white", width=480, height=320)  # 프레임 너비, 높이 설정
    frm.place(x=20, y=60)  # 격자 행, 열 배치

    cap = cv.VideoCapture(0)  # VideoCapture 객체 정의



    def video_play():  # 카메라 화면을 불러오는 부분
        ret, frame = cap.read()  # 프레임이 올바르게 읽히면 ret은 True
        if not ret:
            cap.release()  # 작업 완료 후 해제
            return
        frame = cv.resize(frame, (480, 340)) # 영상의 크기를 480x340으로 조정
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # BGR 방식을 RGB로 변환
        img = Image.fromarray(frame)  # Image 객체로 변환
        imgtk = ImageTk.PhotoImage(image=img, master=newf)  # ImageTk 객체로 변환 (master로 이미지가 사용될 창의 이름을 정해줘야함) -> 위에서 사용된 창의 이름은 newf
        # OpenCV 동영상
        lbl1.imgtk = imgtk
        lbl1.configure(image=imgtk) # image속성을 imgtk로 변경
        lbl1.after(10, video_play) # 10ms 이후에 video_play를 실행

    # def close_addFace():
    #     if messagebox.askokcancel("종료", "등록을 종료하시겠습니까?"):
    #         newf.destroy()

    def captureFace(text):
        path = r'C:\Users\adwin\PycharmProjects\pythonProject\doorlock\ImageBasic'  # 사진 저장 위치 ( 자신의 위치로 바꿔줘야함 )

        text_eng = ["Mom", "Dad", "Child", "GrandMa", "GrandFa"]

        if text == '엄마':
            text = text_eng[0]
        elif text == '아빠':
            text = text_eng[1]
        elif text == '자녀':
            text = text_eng[2]
        elif text == '할머니':
            text = text_eng[3]
        elif text == '할아버지':
            text = text_eng[4]

        if text == "Child":
            text = "Child1"

        for i in range(0, 1):
            success, cap_img = cap.read() # 프레임을 가져옴

            resize = cv.resize(cap_img, (400, 300))

            img = text + '.jpg'  # 일단 임시로 파일 이름은 시간으로 정해줌

            cv.imwrite(os.path.join(path, img), resize) # 이미지 저장

    capBtn = Button(newf, text="엄마", height=5, width=9, command = lambda: captureFace(capBtn['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn.place(x=510, y=100)  # capBtn의 위치 설정

    capBtn1 = Button(newf, text="아빠", height=5, width=9, command=lambda: captureFace(capBtn1['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn1.place(x=610, y=100)  # capBtn의 위치 설정

    capBtn2 = Button(newf, text="자녀", height=5, width=9, command=lambda: captureFace(capBtn2['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn2.place(x=710, y=100)  # capBtn의 위치 설정

    capBtn3 = Button(newf, text="할머니", height=5, width=9, command=lambda: captureFace(capBtn3['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn3.place(x=560, y=200)  # capBtn의 위치 설정

    capBtn4 = Button(newf, text="할아버지", height=5, width=9, command=lambda: captureFace(capBtn4['text']))  # 사진캡쳐 버른 생성 및 이벤트 추가
    capBtn4.place(x=660, y=200)  # capBtn의 위치 설정


    lbl1 = Label(frm)
    lbl1.place(x=0, y=0)
    video_play() # video_play 실행

    def quitAddFace():
        newf.destroy()
        cap.release()

    quitBtn = Button(newf, text="X", height=2, width=4,command=quitAddFace)
    quitBtn.place(x=15, y = 10)


    # newf.protocol("WM_DELETE_WINDOW", close_addFace)


    newf.mainloop() # newf 창 활성화


def copy_phone_num(num):
    return num


def listFace(event):
    os.system(f'py {"C:/Users/adwin/PycharmProjects/pythonProject/doorlock/tk_image.py"}')



def setting_win(event):
    snw = Tk()
    snw.title("Phone Setting")
    snw.geometry('800x450+0+0')

    def button_pressed(value):
        number_entry.insert("end", value)  # 텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
        print(value, "pressed")

    def clear(event):  # C 버튼과 Esc 키를 위한 함수 입니다.
        number_entry.delete(0, END)

    def save_phone(event):

        phone_num = number_entry.get()
        openWeatherMap.fb_phoneUp(phone_num)

    def quitSetting():
        snw.destroy()

    entry_value = StringVar(snw, value='')

    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    lbl1 = Label(snw, text="010을 제외한 8자리를 입력해주세요!", font=fontStyle)
    lbl1.place(x=180, y = 60, width=300, height=40)

    number_entry = Entry(snw, textvariable=entry_value)
    number_entry.place(x=200, y=120, width=260, height=30)

    btn1 = Button(snw, text="1", width=7, height=4, command=lambda: button_pressed('1'))
    btn1.place(x=550, y=70)

    btn2 = Button(snw, text="2", width=7, height=4, command=lambda: button_pressed('2'))
    btn2.place(x=630, y=70)

    btn3 = Button(snw, text="3", width=7, height=4, command=lambda: button_pressed('3'))
    btn3.place(x=710, y=70)

    btn4 = Button(snw, text="4", width=7, height=4, command=lambda: button_pressed('4'))
    btn4.place(x=550, y=160)

    btn5 = Button(snw, text="5", width=7, height=4, command=lambda: button_pressed('5'))
    btn5.place(x=630, y=160)

    btn6 = Button(snw, text="6", width=7, height=4, command=lambda: button_pressed('6'))
    btn6.place(x=710, y=160)

    btn7 = Button(snw, text="7", width=7, height=4, command=lambda: button_pressed('7'))
    btn7.place(x=550, y=250)

    btn8 = Button(snw, text="8", width=7, height=4, command=lambda: button_pressed('8'))
    btn8.place(x=630, y=250)

    btn9 = Button(snw, text="9", width=7, height=4, command=lambda: button_pressed('9'))
    btn9.place(x=710, y=250)

    btn10 = Button(snw, text="저장", width=7, height=4)
    btn10.bind('<Button-1>', save_phone)
    btn10.place(x=550, y=340)

    btn11 = Button(snw, text="0", width=7, height=4, command=lambda: button_pressed('0'))
    btn11.place(x=630, y=340)

    btn12 = Button(snw, text="지우기", width=7, height=4)
    btn12.bind('<Button-1>', clear)
    btn12.place(x=710, y=340)

    quitBtn = Button(snw, text="X", height=2, width=4, command=quitSetting)
    quitBtn.place(x=15, y=10)


    snw.mainloop()
    # snw.bind('<Escape>', clear)


""" 

    디스플레이 화면
    (Display)

"""

win = Tk()  # 창을 하나 만들어줌

win.title("AI DoorLock")  # 창의 이름을 AI DoorLock으로 설정
win.geometry("800x450+0+0")  # 창의 크기를 800x450으로 창의 위치를 0, 0으로 설정
win.resizable(False, False)  # 사이즈 변경 불가


lower_frame = Frame(win, bg='#80c1ff', bd=10) # 날씨 정보를 나타내줄 프레임 생성
label = Label(lower_frame, font=("휴먼매직체", 13)) # 라벨을 프레임에 붙혀줌
html_label = HTMLLabel(win, html="<img src='https://storage.googleapis.com/ai-doorlock.appspot.com/map3.png'></img>", width=70, height=27.5)

#
btn1 = Button(win, text="얼굴 등록", height=3, width=30) # 메인 화면에 얼굴 등록 버튼 생성
btn1.place(x=50, y=5) # 얼굴 등록 버튼 위치 설정
btn1.bind("<Button-1>", add_Face) # 얼굴 등록 버튼 이벤트 설정
btn2 = Button(win, text="등록된 얼굴", height=3, width=30) # 메인화면에 얼굴 검색 버튼 생성
btn2.place(x=285, y=5) # 얼굴 검색 버튼 위치 설정
btn2.bind("<Button-1>", listFace)

def on_closing():
    # if messagebox.askokcancel("종료", "종료하시겠습니까?"):
    win.destroy()


lower_frame.place(relx=0.8, rely=0.15, relwidth=0.3, relheight=0.8, anchor='n') # 날씨 정보 프레임의 크기와 위치 설정
label.place(relwidth=1, relheight=1, y = 0) # 라벨의 위치 설정
html_label.place(x = 10, y = 65)


setting = Button(win, text="설정", height=3, width=30)
setting.place(x=520, y=5)
setting.bind("<Button-1>", setting_win)


getWeather(text) # getWeather 실행


win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()  # GUI 시작

