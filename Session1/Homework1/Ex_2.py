from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    user_info = {
        'truong': {
            "name": "Ngô Quang Trường",
            "age" : 22,
            "gender": 1,
            "work": "barista"
        },
        'thao': {
            "name": "Phạm Thu Thảo",
            "age" : 23,
            "gender": 0,
            "work": "CEO at MBGB - Tteokbokki"
        },
        'tuananh': {
            "name": "Huỳnh Tuấn Anh",
            "age" : 23,
            "gender": 1,
            "work": "student at Bach Khoa University and teacher at techkids"
        },
        'don': {
            "name": "Phạm Quý Đôn",
            "age" : 22,
            "gender": 1,
            "work":"student at Thang Long University and assistant for teachers at techkids"
        }
    }

    if username in user_info.keys():
        user = user_info[username]
        return render_template('index3.html', user = user)
    else:
        return "User infomation not found"


if __name__ == '__main__':
  app.run(debug=True)
