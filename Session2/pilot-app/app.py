# from flask import Flask, render_template, redirect, url_for
from flask import *
# from mongoengine import StringField, IntField, BooleanField, Document
from mongoengine import * # dài quá nên import * cho nhanh
from models.service import Service


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
    service_detail = Service.objects.with_id(service_id)
    return render_template('detail.html', service_detail=service_detail)

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


if __name__ == '__main__':
  app.run(debug=True)
