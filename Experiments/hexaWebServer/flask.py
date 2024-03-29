from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/main', methods=['POST'])
def main():
    # Get the script name from the POST data
    script_name = request.json['ADCquery.py']

    # Run the script and get the output
    result = subprocess.check_output(['python', script_name])

    # Convert the output to JSON
    output = json.loads(result)

    # Return the output as JSON
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)