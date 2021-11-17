from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def ping():
    return  "PYTHON EXECUTOR WORKING FINE"


@app.route('/execute',methods=['POST'])
def executePython():
    data = request.json
    code = data['code']
    print(code)

    return jsonify(code)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)