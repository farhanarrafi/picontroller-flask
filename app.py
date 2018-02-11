from flask import Flask, render_template
from app.model import Components
from app.controller import FirebaseController

app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return render_template('love.html', name = "Farhan")

@app.route('/pi')
def pi_home():
    fireB = FirebaseController()
    #component_list = json.loads(components.get_all())
    return render_template('home.html', component_list = fireB.getAll())


if __name__ == '__main__':
    app.run(debug=True, port=9999, host='0.0.0.0')
