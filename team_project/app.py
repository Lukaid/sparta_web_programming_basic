from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/Q_1', methods=['POST'])
def question1():
    Q1_give_receive = request.form.getlist('Q1_give[]')
    print(Q1_give_receive)
    return {'msg': Q1_give_receive}

@app.route('/Q_2', methods=['POST'])
def question2():
    Q2_give_receive = request.form.getlist('Q2_give[]')
    print(Q2_give_receive)
    return {'msg': Q2_give_receive}

@app.route('/Q_3', methods=['POST'])
def question3():
    Q3_give_receive = request.form.getlist('Q3_give[]')
    print(Q3_give_receive)
    return {'msg': Q3_give_receive}

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)