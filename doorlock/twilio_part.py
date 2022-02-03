"""
    Twilio API - 메세지 전송

    최종 수정일 : 2021/08/02
    작성자 : 한규
    최종 수정 내용 : 전체적인 코드에 주석 추가
"""

from twilio.rest import Client # 메시지를 보내기 위한 Twilio 라이브러리를 가져옴
# import tkinter_part

import firebase_admin
from firebase_admin import firestore, credentials

account_sid = 'AC9e54d727d7d30c12d7ad0741d4ab3918' # Twilio API를 사용하기 위한 계정 번호
auth_token = 'd7b68f4678b6a3758395c9c1a80188a3' # Twilio API를 사용하기 위한 인증 번호
client = Client(account_sid, auth_token)


db = firestore.client()

users_ref1 = db.collection(u'phone')
docs1 = users_ref1.stream()

for doc in docs1:
    phone_num = doc.to_dict()['phone']


def sendMessage(img): # Twilio API에 메시지 형식을 보내줌

    phone_num1 = phone_num

    message = client.messages \
        .create(
        body=f'{img}', # 얼굴인식 부분에서 캡쳐된 사진 URL 주소
        from_='',  # Twilio API에서 제공해준 전화번호
        to='+8210' + phone_num1 # 메시지를 받을 사람의 전화번호 ( 추후에 초기설정으로 추가할 수 있도록 바꿀 예정 )
    )
    print(message.sid) # 메시지가 제대로 보내졌는지 확인
