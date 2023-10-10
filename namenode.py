import flask
from flask import Flask, request
import threading
import requests

# Inicializar Flask para crear una API
app = Flask(__name__)

# Diccionario que mapea nombres de archivos a DataNodes URL
file_to_data_node_mapping = {}

# Diccionario para mapear una acción con una URL de DataNode
action_to_data_node_mapping = {
    'GET': 'http://datanode1_url',
    'PUT': 'http://datanode2_url',
}

# Endpoint para resolver la URL de DataNode para acciones GET y PUT
@app.route('/resolve', methods=['GET'])
def resolve_data_node():
    # Obtener la acción y el nombre del archivo de los parámetros de la URL
    action = request.args.get('action')
    file_name = request.args.get('file_name')
    
    # Si la acción es GET, devolver la URL de DataNode mapeada al archivo
    if action == 'GET':
        return file_to_data_node_mapping.get(file_name, "Archivo no encontrado"), 200
    
    # Si la acción es PUT, devolver una URL de DataNode basada en alguna lógica de selección
    elif action == 'PUT':
        # En este caso, simplemente devolvemos una URL predefinida. 
        # La lógica para seleccionar la URL de DataNode puede ser más compleja en un caso real.
        return action_to_data_node_mapping['PUT'], 200
    
    # En caso de una acción no reconocida, devolver un error
    else:
        return "Acción no reconocida", 400

# Endpoint para realizar búsquedas de archivos basadas en expresiones regulares
@app.route('/search', methods=['GET'])
def search():
    # Obtener la expresión regular de los parámetros de la URL
    regex = request.args.get('regex')
    
    # Buscar en todas las entradas del diccionario de mapeo que coinciden con la expresión regular
    matching_files = {k: v for k, v in file_to_data_node_mapping.items() if re.match(regex, k)}
    
    # Devolver los archivos coincidentes como una respuesta JSON
    return flask.jsonify(matching_files), 200

# Endpoint para listar todos los archivos
@app.route('/list', methods=['GET'])
def list_files():
    # Devolver todos los archivos como una respuesta JSON
    return flask.jsonify(list(file_to_data_node_mapping.keys())), 200

# Función para correr la aplicación Flask en un hilo separado
def run_app():
    app.run(port=5000)

# Iniciar la API en un hilo separado
if __name__ == "__main__":
    threading.Thread(target=run_app).start()
