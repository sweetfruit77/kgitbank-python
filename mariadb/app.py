from flask import Flask, render_template, redirect,url_for,request
import DBConn
app = Flask(__name__)

@app.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        uid = request.form.get('username')
        upw = request.form.get('password')

        row = DBConn.loginSQL(uid, upw)
        if row:
            return '로그인 되었습니다'
        else:
            return '로그인 실패'


if  __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)