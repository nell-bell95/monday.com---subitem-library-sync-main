from flask import Flask
from .services import DataReplicationService

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/design")
def replicate_data_route():
    DataReplicationService.replicate_data()
    return "Data replication initiated!"