from flask import Flask, request
from flask_cors import CORS
from io import StringIO
import sys
import json

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET', 'POST'])
def ping():
    return  "PYTHON EXECUTOR WORKING FINE"


@app.route('/execute',methods=['POST'])
def executePython():
    #print('This is error output', file=sys.stderr)

    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    error= ""
    try:
        exec(json.loads(request.data))
    except Exception as e:
        sys.stdout = old_stdout
        error += ("\n ERRORS: \n" + repr(e))
    output = redirected_output.getvalue()
    output += error
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)