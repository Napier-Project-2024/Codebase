from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/returnVals')
def returnVals():
    from ADCquery import main
    data = main()
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')