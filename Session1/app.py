from flask import Flask, render_template
app = Flask(__name__) #tạo ra 1 sever/app - app này đc làm bằng flask


@app.route('/')
def index():
    posts = [
    {
        "title": "Thơ con cóc",
        "content": "Watermelon",
        "author": "Tuấn Anh",
        "gender": 1
    },
    {
        "title": "Thơ trà sữa",
        "content": "Strawberry",
        "author": "Thu Thảo",
        "gender": 0
    }

    ]
    return render_template("index.html", posts = posts)

    # title = "Thơ con cóc"
    # content = '''Hôm nay trăng lên cao quá
    #              Anh muốn hôn em vào má'''
    # author = "By: Tuấn Anh"

    # return render_template("index.html", post_title = title, post_content = content, post_author = author)
    # return render_template("index.html", post_title = "Thơ con cóc", post_content = "Hôm nay trăng lên cao quá. Anh muốn hôn em vào má", post_author = "By: Tuấn Anh")

@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/say-hello/<name>/<age>')
def sayhello(name, age):
    return "Hi {0}, you are {1} years old".format(name, age)

@app.route('/sum/<int:a>/<int:b>')

def sum(a, b):
    return "{0} + {1} = {2}".format(a, b, (a+b))

if __name__ == '__main__':
  app.run(debug=True) #khởi động sever
