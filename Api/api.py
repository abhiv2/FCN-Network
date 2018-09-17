import os

from flask import Flask, request, abort, jsonify, send_from_directory
import random

FILES_DIRECTORY = './files'
RESULTS_DIRECTORY = './results'
mongo_url = "mongodb://localhost"

from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

api = app
# List files
@api.route('/files')
def list_files():
    files = []
    for filename in os.listdir(FILES_DIRECTORY):
        path = os.path.join(FILES_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

# download a file
@api.route('/files/<path>')
def get_file(path):
    return send_from_directory(FILES_DIRECTORY, path, as_attachment=True)

# upload a file
@api.route('/newfiles')
def post_file():
    import subprocess
    
 

    filename = str(random.randint(1000,9999)) + '.zip'
    res = subprocess.check_output(["cp", "../demoData/demo.zip", "./files/" + filename ])

    if '/' in filename:
        abort(400, 'no subdirectories directories allowed')

    with open(os.path.join(FILES_DIRECTORY, filename), 'wb') as fp:
        fp.write(request.data)

    # Success
    return jsonify({"status" : True, "data" : filename}), 201

# List results
@api.route('/results')
def list_results():
    files = []
    for filename in os.listdir(RESULTS_DIRECTORY):
        path = os.path.join(RESULTS_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

# download a file
@api.route('/results/<path>')
def get_results(path):
    return send_from_directory(RESULTS_DIRECTORY, path, as_attachment=True)

# upload a file
@api.route('/results/<filename>', methods=['POST'])
def post_results(filename):

    if '/' in filename:
        abort(400, 'no subdirectories directories allowed')

    with open(os.path.join(RESULTS_DIRECTORY, filename), 'wb') as fp:
        fp.write(request.data)

    # Success
    return jsonify({"status" : True}), 201

# download a file
@api.route('/Scripts')
def script():
    return send_from_directory('./', 'Scripts.zip', as_attachment=True)




if __name__ == '__main__':
    api.run(debug=True, port=8000)
