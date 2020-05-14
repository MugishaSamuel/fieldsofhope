
from flask import Flask, render_template

from flask import Flask, render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', title="Homepage")


if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=3000, debug=True)


