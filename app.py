from flask import Flask, request, render_template
import json
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/get', methods=['POST'])
def form():
    # connect db
    # select data
    # 指定給 某某變數
    data = request.form['name']
    return render_template('abc.html', items=data)

@app.route("/")
def get():
    return render_template('abc.html')

if __name__ == '__main__':
    app.run()
