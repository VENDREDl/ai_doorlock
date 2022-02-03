"""
    Firebase ( DB )

    최종 수정일 : 2021/08/08
    작성자 : 한규
    최종 수정 내용 : 전체적인 코드에 주석 추가
"""


# Firebase
from uuid import uuid4 # 고유성이 보장되는 id를 만들기 위한 라이브러리
import firebase_admin # firebase를 사용하기 위한 라이브러리
from firebase_admin import credentials, storage
from os import system

PROJECT_ID = "ai-doorlock" # firebase에서 설정해준 프로젝트의 이름

cred = credentials.Certificate("./ai-doorlock-firebase-adminsdk-q5d33-06c23dd0af.json") # Firebase 정보가 들어있는 파일 위치
default_app = firebase_admin.initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com" # 프로젝트에 접근할수 있는 URL
})

bucket = storage.bucket() 

def fileUpload(file):
    blob = bucket.blob(file) # 파일을 업로드 하기 위해 버킷을 만들어줌
    new_token = uuid4() # 고유한 id를 만들어줌
    metadata = {"firebaseStorageDownloadTokens": new_token} # 위에서 만든 id를 DownloadToken으로 설정
    blob.metadata = metadata # 

    blob.upload_from_filename(filename=file, content_type='img/jpg') # 파일 이름을 file 형식을 img/jpg로 업로드
    print(blob.public_url) # 파일에 접근할수 있는 URL 확인
