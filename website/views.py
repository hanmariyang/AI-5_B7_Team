# 각 import들이 하는 일
# Blueprint : 플라스크 app의 모든 url을 한 곳에서 관리하지 않아도 됨
# 여러곳에 뿌려진 url의 정의를 수집하여 한 곳을 모아줌
# redirect : 웹 브라우저가 요청한 URL을 다른 URL로 자동으로 전환해줌
# render_template : HTML을 렌더링하기 위해 필요한 데이터를 전달 후 렌더링한 결과를 반환
# request : 클라이언트가 전송한 HTTP 요청 메시지에 포함된 데이터를 읽을 수 있음
# flash : 다음 요청에서만 유효한 메시지 생성
# error, success, warning 등 여러가지 카테고리를 만들어 사용할 수 있음
# url_for : URL을 동적으로 생성할 때 라우트 함수의 이름을 사용
# login_required : flask에서 로그인이 필요한 페이지 만들기 위해서 사용
# current_user : 로그인된 사용자의 정보를 보여줌
# ObjectId : mongoDB에서 사용하는 ObjectId
# json_util : ObjectId는 jsonify로 불러올 수 없기 때문에 사용


# 필요한 것들 import
from flask import Blueprint, redirect, render_template, request, flash, url_for, jsonify
from bson import ObjectId

# init.py에서 정의한 db를 불러옴 init.py는 최상위 실행 파일이므로 from . 만 적어도 된다
from . import db


# Blueprint에 view.py를 정의하여 보여질 페이지와 경로를 정의
# 기존엔 app.py에서 app.route만 썼으나 여러 페이지를 사용하기 때문에
# route를 Blueprint에 저장 후 Blueprint에서 처리함
# '클라이언트 요청 > 서버의 응답'을 과정을 세부적이게 구현할 필요가 없음
# 반드시 Blueprint 등록 후엔 init.py에 가서 다음 코드를 적어야 한다
# from .views import views
# app.register_blueprint(views, url_prefix='/')
views = Blueprint("views", __name__)
# 사용의 편의 성을 위해 다른 파일에선 일괄적으로 views로 사용되게 정의한다.




@views.route("/")
def home():
    return render_template("home.html")


# 개인 프로필 창으로 이동
# 여기서 myo는 주소창의 5000/myo 의 주소이다
@views.route("/myo")
def myo_in():
    return render_template("myo_profile.html")


@views.route("/gmj")
def gjm_in():
    return render_template("gmj_profile.html")


@views.route("/wgw")
def wgw_in():
    return render_template("wgw_profile.html")


# 상세보기
@views.route("/detail")
def show_post():
    return render_template("detail.html")


# ===============민정님==================================



# ===============영오님==================================

# ↓미구현↓


# 좋아요 DB 보내기
@views.route("/like", methods=["POST"])
def member_post():
    like1_receive = request.form['like1_give']
    user_ip = request.remote_addr
    find_ip = db.ip_address.find_one({'like_user':like1_receive,'ip_address':user_ip})
    if find_ip:
         return jsonify({'msg':'동일 Ip에서 좋아요는 1번만 가능합니다!'})
    else:
        doc = {
            'like_user':like1_receive,
            "ip_address":user_ip
        }
        db.ip_address.insert_one(doc)
        db.likes.update_one({'user':like1_receive},{'$inc':{'count':1}})
        return jsonify({'msg':'좋아요 완료!'})
    # like1_receive = request.form['like1_give']
    # db.likes.update_one({'user':like1_receive},{'$inc':{'count':1}})
    # return jsonify({'msg':'POST 연결 완료!'})

# 좋아요 숫자 보이기
@views.route("/like", methods=["GET"])
def like_get():
    like1_count = list(db.likes.find({}, {'_id':False}))
    return jsonify({'result': like1_count})

# 좋아요 취소하기
@views.route("/unlike", methods=["POST"])
def hate():
    hate_receive = request.form['hate_give']
    user_ip = request.remote_addr
    find_ip = db.ip_address.find_one({'like_user':hate_receive,'ip_address':user_ip})
    if find_ip:
        db.ip_address.delete_one({'like_user':hate_receive,'ip_address':user_ip})
        db.likes.update_one({'user':hate_receive},{'$inc':{'count':-1}})
        return jsonify({'msg':'좋아요 취소 완료!'})
    else:
        return jsonify({'msg':'좋아요를 누르지 않으셨습니다!'})

# ↑미구현↑



# 메모 삭제
@views.route("/delete_comment", methods=["POST"])
def delete_note():
    note_id = request.form["note_id"]

    db.sbs_comment.delete_one({"_id": ObjectId(note_id)})

    return jsonify({'msg':'삭제완료!'})


# 메모 업데이트
@views.route("/update_note", methods=["POST"])
def update_note():
    title = request.form["title"]
    content = request.form["content"]
    note_id = request.form["note_id"]
    print(note_id)
    db.sbs_comment.update_one(
        {"_id": ObjectId(note_id)}, {"$set": {"title": title,"content": content}}
    )

    return redirect(url_for("views.memo"))





# ===============규원님==================================

# 댓글저장하기
@views.route("/sbs_comment", methods=["POST"])
def sbs_post():
    name_receive = request.form["name_give"]
    password_receive = request.form["password_give"]
    comment_receive = request.form["comment_give"]
    # user_ip = request.remote_addr

    doc = {
        "comment":comment_receive,
        "name": name_receive,
        "PW": password_receive,
        # "user_ip" : user_ip
    }
    # name=name_receive,
    # pw=password_receive,
    # comment=comment_receive
    # doc.save()

    db.sbs_comment.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

# 댓글불러오기
@views.route("/sbs_comment", methods=["GET"])
def sbs_get():
    sbs_data = list(db.sbs_comment.find({},{'_id':False}))
    return jsonify({'result':sbs_data})

# last_index=db.sbs.find().sort('_id',-1).limit(1)

# if db.sbs.count_documents({}) == 0:
#     index=1
# else:
#     index=last_index[0]['index']+1
# doc={
# 'index':index,
# 'id':id_receive,
# 'pw':pw_receive,
# 'comment':comment_receive
# }