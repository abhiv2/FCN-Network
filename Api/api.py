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



# database connection
from pymongo import MongoClient
db= MongoClient(mongo_url).qt

###################
db.users.remove({})

db.users.insert_one({
    "pk": "qUUbMfSsUV7yoBVCRyZDAmEA594Gde1cZ2",
    "sk": "cMjPPe4dYbHibSvuxhqskhuKW4m23BaVLmcU9VTCYMsLboxcMauk",
    "balance": 1000
})

db.users.insert_one({
    "pk": "qHsrp2icawZignP7e5BPnnyzgpB3XBScUz", 
    "sk": "cV3VHikosgq84tj99nBgPafKHXL7N8x3jp4RE2qFe1CWHixkEXaK",
    "balance": 100
})

@app.route('/balances')
def balances():
    res = []
    users = db.users.find({}, {"_id" : False})
    for user in users:
        res.append(user)
    return jsonify({"result" : res})


@app.route('/orders')
def orders():
    res = []
    orders = db.orders.find({}, {"_id" : False})
    for order in orders:
        res.append(order)
    return jsonify({"result" : res})

@app.route('/orders', methods=['POST'])
def neworder():
    req = request.get_json()
    res = {}
    res['tokens'] = req['tokens']
    res['data'] = req['data']
    res['asker'] =  'qHsrp2icawZignP7e5BPnnyzgpB3XBScUz'
    res['renter'] = ''
    res['status'] = False
    db.orders.insert_one(res)
    return jsonify({"status" : True})


@app.route('/claim', methods=['POST'])
def claim():
    req = request.get_json()
    res = {}
    data = req['data']
    db.orders.update_one(
            {"data": data},
            {
                "$set": {
                    "status":True,
                    "renter" : 'qUUbMfSsUV7yoBVCRyZDAmEA594Gde1cZ2'
                }
            }
        )
    bidbal = db.orders.find_one( {"data": data})["tokens"]
    senderBal = db.users.find_one({'pk' : 'qHsrp2icawZignP7e5BPnnyzgpB3XBScUz' })["balance"] - bidbal
    recieverBal = db.users.find_one({'pk' : 'qUUbMfSsUV7yoBVCRyZDAmEA594Gde1cZ2'})["balance"] + bidbal
    db.users.update_one(
            {"pk": 'qHsrp2icawZignP7e5BPnnyzgpB3XBScUz'},
            {
                "$set": {
                    "balance": senderBal 
                }
            }
        )
    db.users.update_one(
            {'pk' : 'qUUbMfSsUV7yoBVCRyZDAmEA594Gde1cZ2'},
            {
                "$set": {
                    "balance" : recieverBal
                }
            }
        )
    
    return jsonify({"status" : True})
    


if __name__ == '__main__':
    api.run(debug=True, port=8000)
