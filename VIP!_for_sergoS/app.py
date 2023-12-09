from flask import (Flask, request, render_template, url_for)

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/count', methods=["GET", "POST"])
def count():
    if request.method == 'POST':
        x = request.form['function_1']

        return render_template('count.html', result=x)
    else:
        return render_template('count.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
