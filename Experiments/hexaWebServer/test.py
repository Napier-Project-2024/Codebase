import flask
import subprocess
import time

app = flask.Flask(__name__)

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['python3 /home/team-member/ABElectronics_Python_Libraries/ADCPi/demos/demo_readvoltage.py'],  # Call any function
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(0.01)  # Add control to output
            yield line.rstrip() + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$

app.run(debug=True, port=5000, host='0.0.0.0')