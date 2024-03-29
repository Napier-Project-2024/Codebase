#!/usr/bin/env python


from flask import Flask, render_template
from ADCquery import main
import datetime

app = Flask(__name__)

# web interface

@app.route("/")

def index():

    return render_template('index.html')


# API returns a JSON

@app.route('/returnVals')
def returnVals():
    
    data = main()
    return data


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')