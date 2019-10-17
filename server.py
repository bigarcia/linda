from flask import Flask
from flask_restful import Resource, Api
from json import dumps
from flask import abort
from flask import make_response
from flask import jsonify
from flask import request
import sys
from Controller import Controller

app = Flask(__name__)
api = Api(app)
     
@app.route('/blog', methods=['POST'])
def put():
	data = Controller.get_instance().add(request.form['tuple'])
	return make_response(jsonify({'response': data}), 200)  
	pass

@app.route('/blog/', methods=['GET'])
def get():
	#data = Controller.get_instance().read()
	publisher = request.args.get('publisher', default = str, type = str)
	topic = request.args.get('topic', default = str, type = str)
	message = request.args.get('message', default = str, type = str)
	data = Controller.get_instance().read((publisher,topic,message))
	return make_response(jsonify({'response': data}), 200)  	
	pass


@app.route('/blog', methods=['DELETE'])
def delete():
	publisher = request.args.get('publisher', default = str, type = str)
	topic = request.args.get('topic', default = str, type = str)
	message = request.args.get('message', default = str, type = str)
	if(publisher == str or topic == str or message == str):
		return make_response(jsonify({"response":"Missing parameter!!!"}), 400)  
	data = Controller.get_instance().remove((publisher,topic,message))
	return make_response(jsonify({'response': data}), 200)  
	pass

if __name__ == '__main__':
     port = 5000
     app.run(port=port)