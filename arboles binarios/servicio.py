import sys
import logging
from flask               import Flask,jsonify,json, request
from flask_api           import status
from FacadeArbol import FacadeArbol

#### Flask object #######
app = Flask(__name__)

#### Constantes #########

OK 	 = 'OK'
FAIL = 'FAIL'

#### Log ################

logging.basicConfig(filename="test.log", level=logging.DEBUG)

@app.route('/create', methods=['POST'])
def createTree():
    try:
        _json_tree = request.get_json()
        logging.debug(_json_tree)
        facade = FacadeArbol()
        nombre_arbol, id = facade.createTree(_json_tree)
        return jsonify(nombre_arbol)  
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/ancestro', methods=['GET'])
def ancestro():
    try:
        _json_tree = request.args.get('arbol')
        primer_abs = request.args.get('abs1')
        segundo_abs = request.args.get('abs2')
        logging.debug(_json_tree)
        facade = FacadeArbol()
        nombre_arbol = facade.arbol_built(_json_tree, primer_abs, segundo_abs)
        return jsonify(OK)  
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

####### Main ############
if __name__ == '__main__':
    app.run()