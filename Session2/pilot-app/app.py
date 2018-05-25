# from flask import Flask, render_template, redirect, url_for
from flask import *
# from mongoengine import StringField, IntField, BooleanField, Document
from mongoengine import * # dài quá nên import * cho nhanh
from models.service import Service
from models.user import User

import mlab

app = Flask(__name__)

mlab.connect()


# #design database
# #create collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     # weight = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#
# service = Service(name = "Kiều Anh", yob = 1963, gender = 0, height = 165, phone = "0123456789", address = "Hai Bà Trưng - Hà Nội", status = True)
#
# service.save()


@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender = g, yob__lte = 2000)
    return render_template('search.html', all_service = all_service)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)


@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        print("Service not found")
    return service_id


@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob  = form['yob' ]

        #lưu service vào trong database
        new_service = Service(name = name, yob = yob)
        new_service.save()

        return redirect(url_for('admin'))


@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html', all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    if "loggedin" in session:
        service_detail = Service.objects.with_id(service_id)
        return render_template('detail.html', service_detail=service_detail)
    else:
        return redirect(url_for('login'))


@app.route('/update/<service_id>', methods=['GET', 'POST'])
def update(service_id):

    if request.method == 'GET':
        service_to_update = Service.objects.with_id(service_id)
        return render_template ('update.html', service_to_update=service_to_update)

    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        # status = form['status']
        description = form['description']
        measurements = form['measurements']
        image = form['image']

        service_to_update = Service.objects.with_id(service_id)
        service_to_update.update(set__name=name,
                                    set__yob=yob,
                                    set__gender=gender,
                                    set__height=height,
                                    set__phone=phone,
                                    set__address=address,
                                    # set__status=status,
                                    set__description=description,
                                    set__measurements=measurements,
                                    set__image=image)
        service_to_update.reload()
        return redirect(url_for('admin'))


@app.route('/signin', methods = ["GET", "POST"])
def signin():

    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']

    user = User(name = name,
                email = email,
                username = username,
                password = password)
    user.save()

    return redirect(url_for('service'))


@app.route('/user')
def user():
    all_user = User.objects()
    return render_template("user.html", all_user = all_user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        users = User.objects(username = username, password = password)
        if len(users) == 0:
            return redirect(url_for('signin'))
        else:
            session['loggedin'] = True
            return redirect(url_for('service'))

@app.route('/service-request')
def servicerequest():
    all_service = Service.objects()
    users = User.objects()
    request = Request(time = str(datetime.now()),
                      is_accepted = False)
    request.save()
    return "Đã gửi yêu cầu"

if __name__ == '__main__':
  app.run(debug=True)
