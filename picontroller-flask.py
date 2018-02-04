from flask import Flask, render_template
#from gpiozero import Button
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html', name = "Farhan")


if __name__ == '__main__':
    app.run()
