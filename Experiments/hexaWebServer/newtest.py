from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    # Assuming your python script is a function that returns a dictionary
    from ADCquery import main
    data = main()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')