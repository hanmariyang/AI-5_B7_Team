from flask import Flask
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.haakbnc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
# 사용의 편의성을 위해 접속하고자 하는 db를 db라고 지칭한다
# views.py 에서 db라고 import 가능한 이유!


def create_app():
    app = Flask(__name__)
    app.secret_key ='nebecamp-miniproject-B7team'

    # 블루프린트 인스턴스 가져오기
    from .views import views
    from .auth import auth

    # 플라스크 앱에 등록하기
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


