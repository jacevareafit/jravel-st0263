from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola desde el servidor Flask!"

@app.route("/list_Files", methods=["GET"])
def list_Files():
    data = {"message": "Este es el resultado de la función GET 1"}
    return data

@app.route("/Find_Files", methods=["GET"])
def Find_Files():
    data = {"message": "Este es el resultado de la función GET 2"}
    return data

if __name__ == "__main__":
    app.run()