from flask import Flask, render_template, redirect,url_for,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!='admin' or request.form['password']!='admin':
            error='Try again'
        else:
            return redirect(url_for('secret'))

    return render_template('index.html', error=error)


@app.route('/secret')
def secret():
    return 'Secret'


@app.route('/form')
def form():
	return render_template('form_submit.html')

#form action
@app.route('/formresult', methods=['POST'] )
def action():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    lang = request.form.getlist('lang')
    print(lang)
    return render_template('form_action.html', firstname=firstname, lastname=lastname, email=email,lang=lang)


if  __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)