from flask import Flask, render_template
import sys
import subprocess
app = Flask(__name__)

@app.route("/")


def index():
    def time():
        now = subprocess.check_output(['python','example.py'])
        return now
    templateData = {
        'title' : 'HELLO!',
        'time'  : time()
        }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)