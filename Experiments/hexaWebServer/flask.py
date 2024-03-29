from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    # Get the script name from the POST data
    script_name = request.json['ADCquery']

    # Run the script and get the output
    result = subprocess.check_output(['python', script_name])

    # Convert the output to JSON
    output = json.loads(result)

    # Return the output as JSON
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
