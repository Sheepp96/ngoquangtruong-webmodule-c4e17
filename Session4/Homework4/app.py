from flask import Flask, render_template
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
  app.run(debug=True)
