from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def nqt():
    post = {
        'name': 'Ngô Quang Trường',
        'age' : 22,
        'work': 'Barista at Dingtea 98 Vũ Trọng Phụng',
        'school': 'Thăng Long University',
        'hobbies': 'Football, Game',
        'dog': 'His name is Bông and he is a miniature pinscher'
    }
    return render_template('index2.html', post = post)

    
@app.route('/school')
def school():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
  app.run(debug=True)
