from flask import Flask
from flask_restx import Resource, Api
from apis.event_collect_controller import api as collect

app = Flask(__name__)
api = Api(
    app,
    version='0.1',
    title="Event Collect API Server",
)

api.add_namespace(collect, '/api')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)