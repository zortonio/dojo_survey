from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def new_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('user.html', name=name, location=location, language=language, comment=comment)

@app.route('/home')
def goBack():
    return redirect('/')

app.run(debug=True)
