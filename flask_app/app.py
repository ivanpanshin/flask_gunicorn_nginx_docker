from flask import Flask
from flask import request, jsonify
from random import sample
import subprocess

server = Flask(__name__)

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

def run_faas_request():
    function = request.json['function']
    # ref xspdf.com/resolution/50942456.html
    process = subprocess.Popen(['export', 'OPENFAAS_URL=https://faasd.cthulu.tk', '&&', 'echo', '|', 'faas-cli', 'invoke', function], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    return 'STDOUT:{}'.format(stdout)


@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()

@server.route('/faas', methods=['GET', 'POST'])
def make_faas_request():
    if request.method == 'GET':
        return 'This is the faas route.  Send a POST request with json payload of the form { function: catapi }.'
    if request.method == 'POST':
        return run_faas_request()
