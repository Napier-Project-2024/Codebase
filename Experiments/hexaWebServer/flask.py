import flask
import subprocess
import json

app = flask.Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    # Get the script name from the POST data
    script_name = flask.request.json['ADCquery']

    # Run the script and get the output
    result = subprocess.check_output(['python', script_name])

    # Convert the output to JSON
    output = json.loads(result)

    # Return the output as JSON
    return flask.jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
