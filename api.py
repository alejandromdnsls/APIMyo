from flask import Flask
from flask_restful import Resource, Api
import json


tt = Flask(__name__)
api = Api(tt)

from flask import request
@tt.route("/datos",methods=['POST'])
def datos():
    print (request.is_json)
    values = request.form.to_dict()
    print(request.headers)
    print(values)

    #print(json.loads(values))
    respuesta = {'clase':'A','idLsm':1, 'idResult':3}
    return json.dumps(respuesta)

if __name__ == '__main__':
 tt.run('0.0.0.0', 5000, debug=True)



"""class Hello(Resource):
    def get(self, name):
        return {"Hello":"b"}


api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
 tt.run(debug=True)"""
