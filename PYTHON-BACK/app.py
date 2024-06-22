# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy 

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# permita acceder desde el frontend al backend
CORS(app)

# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/bd_productos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)


# Definir la tabla 
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))
    precio=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    imagen=db.Column(db.String(400))

    def __init__(self,descripcion,precio,cantidad,imagen):   #crea el  constructor de la clase
        self.descripcion=descripcion   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.cantidad=cantidad
        self.imagen=imagen


# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()


# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar productos'

# Crear un registro en la tabla Productos
@app.route("/registro", methods=['POST']) 
def registro():
   
    descripcion_recibido = request.json["descripcion"]
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    imagen=request.json['imagen']

    nuevo_registro = Producto(descripcion=descripcion_recibido,precio=precio,cantidad=cantidad,imagen=imagen)
    db.session.add(nuevo_registro)
    db.session.commit()

    return "Solicitud de post recibida"

# Retornar todos los registros en un Json
@app.route("/productos",  methods=['GET'])
def productos():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Producto.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "descripcion":objeto.descripcion, "precio":objeto.precio, "cantidad":objeto.cantidad, "imagen":objeto.imagen})

    return jsonify(data_serializada)

# Modificar un registro
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    # Buscar el registro a modificar en la tabla por su id
    producto = Producto.query.get(id)

    descripcion = request.json["descripcion"]
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    imagen=request.json['imagen']

    producto.descripcion=descripcion
    producto.precio=precio
    producto.cantidad=cantidad
    producto.imagen=imagen
    db.session.commit()

    data_serializada = [{"id":producto.id, "descripcion":producto.descripcion, "precio":producto.precio, "cantidad":producto.cantidad, "imagen":producto.imagen}]
    
    return jsonify(data_serializada)

@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    
    # Se busca a la productos por id en la DB
    producto = Producto.query.get(id)

    # Se elimina de la DB
    db.session.delete(producto)
    db.session.commit()

    data_serializada = [{"id":producto.id, "descripcion":producto.descripcion, "precio":producto.precio, "cantidad":producto.cantidad, "imagen":producto.imagen}]

    return jsonify(data_serializada)

if __name__ == "__main__":
    app.run(debug=True)