from flask import Flask
from flask.ext import restful

import wsme
from wsme import types as wtypes
from wsmeext.flask import signature


app = Flask(__name__)
api = restful.Api(app)

class Info(wsme.types.Base):
    message = wsme.types.text

class HelloWorld(restful.Resource):

    @signature(Info)
    def get():
        return Info(message="hello")

    @signature(None, body=Info)
    def post(self, info):
        print("Got a message: %s" % info.message)

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)

