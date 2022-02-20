from flask_restx import Api
from apis import create_app
from apis.event_search_controller import api as search

app = create_app()

api = Api(
    app,
    version='0.1',
    title="Event Search API Server",
)

api.add_namespace(search, '/api')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)