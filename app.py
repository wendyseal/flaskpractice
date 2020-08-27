from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/form', methods=['POST'])
def form():
    # connect db
    # select data
    # 指定給 某某變數
    data = [
        {
            'name': 'Audrin',
            'place': 'kaka',
            'mob': '7736'
        },
        {
            'name': 'Stuvard',
            'place': 'Goa',
            'mob': '546464'
        }
    ]
    return render_template('abc.html', items=data)

if __name__ == '__main__':
    app.run()
