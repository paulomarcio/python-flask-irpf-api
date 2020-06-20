from flask import Flask
from flask_restful import Resource, Api

from resources.impostos.irpf import Irpf

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {}, 200

api.add_resource(Home, '/')
api.add_resource(Irpf, '/impostos/irpf')


if __name__ == '__main__':
    app.run(debug=True)
