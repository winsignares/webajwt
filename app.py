import json
from urllib import response
from common.token import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def obtenertoken():
    #var_request = json.loads(event["body"])   
    datatoken = generar_token("William", 123)
    var_Token = datatoken["token"]
    response = {"statusCode": 200, "body": json.dumps(var_Token)}    
    return jsonify(response)

@app.route('/verificartoken', methods=['GET'])
def verificartoken():
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    print("token =>", token)
      # Call the function to validate token
    vf = verificar_token(token)
    print("vf =>", vf)
    return jsonify(vf)

#Iniciamos app para que se ejecute en un puerto#
if __name__ == "__main__":
    app.run(debug=True)