from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/test", methods=['POST'])
def process_request_string_to_cut():
    """ Return a JSON object with the key 'return_string' """
    if request.method == 'POST':
        string_to_cut = request.json['string_to_cut']
        c_string = cut_string(string_to_cut)
    else:
        return "Request is not correct"
    return json.dumps({"return_string": c_string})


def cut_string(string_to_cut):
    """
    Return a string containing every third letter from the original string
    """
    new_string = ""
    index = 0
    for letter in string_to_cut:
        index += 1
        if index == 3:
            new_string += letter
            index = 0
    return new_string


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)