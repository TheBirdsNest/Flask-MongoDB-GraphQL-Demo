from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
import os

from schema import schema

__DATABASE = "templates"
__PASSWORD = os.environ.get("MONGO_DEVELOPER_PASSWORD")

__client = connect(
    __DATABASE,
    host=f"mongodb+srv://developer:{__PASSWORD}@devcluster.25vmv.mongodb.net/{__DATABASE}?retryWrites=true&w=majority",
    alias="default"
)

app = Flask(__name__)
app.debug = True

app.add_url_rule('/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(port=5002)
