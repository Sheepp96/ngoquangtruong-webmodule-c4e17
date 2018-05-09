from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:w>/<int:h>')
def bmi_calc(w, h):
    h_m = float(h / 100)
    bmi = w / (h_m ** 2)

    if bmi < 16:
        result = 'severely underweight'
    elif 16 <= bmi < 18.5:
        result = 'underweight'
    elif 18.5 <= bmi < 25:
        result = 'normal'
    elif 25 <= bmi < 30:
        result = 'overweight'
    else:
        result = 'obese'

    return  "Your BMI is {0} and you are {1}".format(round(bmi,1), result)

if __name__ == '__main__':
  app.run(debug=True)
