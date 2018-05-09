from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:w>/<int:h>')
def bmii_calc(w, h):
    h_m = float(h / 100)
    bmi = w / (h_m ** 2)

    if bmi < 16:
        result = 'Severely underweight'
    elif 16 <= bmi < 18.5:
        result = 'Underweight'
    elif 18.5 <= bmi < 25:
        result = 'Normal'
    elif 25 <= bmi < 30:
        result = 'Overweight'
    else:
        result = 'Obese'

    post = [round(bmi,1), result]
    return render_template('index1.html', post = post)

if __name__ == '__main__':
  app.run(debug=True)
