from flask import Flask
from flask_restful import Resource, Api

tt = Flask(__name__)
api = Api(tt)

from flask import request
@tt.route("/datos",methods=['POST'])
def datos():
    values = request.get_json()
    respuesta = {'clase':'A','idLsm':1, 'idResult':3}
    return json.dumps(respuesta)

if __name__ == '__main__':
 tt.run(debug=True)



"""class Hello(Resource):
    def get(self, name):
        return {"Hello":"b"}


api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
 tt.run(debug=True)"""
