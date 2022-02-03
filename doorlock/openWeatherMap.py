"""
    OpenWeatherMap API - 날씨 정보

    최종 수정일 : 2021/08/02
    작성자 : 한규, 박주영
    최종 수정 내용 : 전체적인 코드에 주석 추가
"""

import json # JSON을 사용하기 위한 라이브러리

import firebase_admin # firebase DB를 사용하기 위한 라이브러리
import requests # HTTP 요청을 보내기 위한 라이브러리
from firebase_admin import firestore, credentials # firebase의 firestore를 사용하기 위해 추가

#=======================================================)) Firebase Part

cred = credentials.Certificate("./ai-doorlock-firebase-adminsdk-q5d33-06c23dd0af.json") # firebase API를 사용하기 위한 정보가 들어있는 JSON 파일을 가져옴
firebase_admin.initialize_app(cred, {
  'projectId': 'ai-doorlock',
})

db = firestore.client()

users_ref = db.collection(u'city')
docs = users_ref.stream()

for doc in docs:
   a = doc.to_dict()['city']

# OpenWeatherMap API

apikey = "8a3fc945e29c098f001f7788c574a2af" # OpenWeatherMap API의 apikey를 지정
global city
city = a
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}" # request할 url을 지정
k2c = lambda k: k - 273.15 # 람다 함수 사용하여 켈빈 온도를 섭씨로 변환

def wDescEngToKor(w_id): # 영어로 되어있는 서비스를 한글로 변경
    w_id_arr = [201, 200, 202, 210, 211, 212, 221, 230, 231, 232,
                300, 301, 302, 310, 311, 312, 313, 314, 321, 500,
                501, 502, 503, 504, 511, 520, 521, 522, 531, 600,
                601, 602, 611, 612, 615, 616, 620, 621, 622, 701,
                711, 721, 731, 741, 751, 761, 762, 771, 781, 800,
                801, 802, 803, 804, 900, 901, 902, 903, 904, 905,
                906, 951, 952, 953, 954, 955, 956, 957, 958, 959,
                960, 961, 962]

    w_kor_arr = ["천둥구름", "천둥구름", "천둥구름", "약한 천둥구름",
                 "천둥구름", "강한 천둥구름", "불규칙적 천둥구름", "천둥구름", "천둥구름",
                 "천둥구름", "가벼운 안개비", "안개비", "강한 안개비", "가벼운 적은비", "적은비",
                 "강한 적은비", "소나기와 안개비", "안개비", "소나기", "악한 비", "중간 비", "강한 비",
                 "매우 강한 비", "극심한 비", "우박", "약한 소나기 비", "소나기 비", "강한 소나기 비", "소나기 비",
                 "가벼운 눈", "눈", "강한 눈", "진눈깨비", "소나기 진눈깨비", "약한 비와 눈", "비와 눈", "약한 소나기 눈",
                 "소나기 눈", "강한 소나기 눈", "박무", "연기", "연무", "모래 먼지", "안개", "모래", "먼지", "화산재", "돌풍",
                 "토네이도", "맑은 하늘", "약간 구름이 낀 하늘", "구름이 낀 하늘", "구름이 없는 하늘",
                 "흐린 하늘", "토네이도", "태풍", "허리케인", "한랭", "고온", "바람부는", "우박", "바람이 거의 없는",
                 "약한 바람", "부드러운 바람", "중간 세기 바람", "신선한 바람", "센 바람", "센 바람", "돌풍",
                 "심각한 돌풍", "폭풍", "강한 폭풍", "허리케인"]

    for i in range(0, len(w_id_arr)):
        if w_id_arr[i] == w_id:
            return w_kor_arr[i]
            break
    return "none"

def weather(city): # Tkinter 화면에 날씨 정보를 출력

    url = api.format(city=city, key=apikey) # API에 요청할 URL 생성
    r = requests.get(url) # API에 요청후 받은 데이터 추출
    data = json.loads(r.text) # 받은 데이터를 JSON 형태로 변환

    # 결과를 각 변수에 지정
    name = data["name"]
    weather = data["weather"][0]["id"]
    weather = wDescEngToKor(weather)
    minTemp = round(k2c(data["main"]["temp_min"]), 1)
    maxTemp = round(k2c(data["main"]["temp_max"]), 1)
    humidity = data["main"]["humidity"]

    # 변환된 도시 이름을 firebase DB에 저장
    doc_ref = db.collection(u'city').document(u'city')
    doc_ref.set({
        u'city': city
    })

    # 위의 변수를 튜플 형태로 리턴
    return name, weather, minTemp, maxTemp, humidity

weather(city)

def changeCityKorToEng(taken): # 한글로 받은 도시 이름을 영어로 변경 [ 도시 변경 부분이 한글로 되어있기 때문에 변환 ]

    c_id_arr = ["Seoul, KR", "Incheon, KR", "Daejeon, KR", "Daegu, KR", "Gwangju, KR", "Ulsan, KR"]

    # 도시 이름을 한글에서 영어로 변환
    if taken == '서울':
        city = c_id_arr[0]
    elif taken == '인천':
        city = c_id_arr[1]
    elif taken == '대전':
        city = c_id_arr[2]
    elif taken == '대구':
        city = c_id_arr[3]
    elif taken == '광주':
        city = c_id_arr[4]
    elif taken == '울산':
        city = c_id_arr[5]

    # 변환된 도시 이름을 firebase DB에 저장
    doc_ref = db.collection(u'city').document(u'city')
    doc_ref.set({
        u'city': city
    })

def fb_phoneUp(phone_num):
    doc_ref = db.collection(u'phone').document('phone')
    doc_ref.set({
        u'phone' : phone_num
    })

def fb_phoneDown():
    users_ref = db.collection(u'phone')
    docs = users_ref.stream()

    for doc in docs:
        a = doc.to_dict()['phone']

    return a
    
    # DB에 저장이 되었는지 확인하는 부분
     
    # users_ref = db.collection(u'city')
    # docs = users_ref.stream()

    # for doc in docs:
    #     a = doc.to_dict()['city']
    # weather(a)