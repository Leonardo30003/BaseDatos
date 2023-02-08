from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

# crear una funcion que permita actualizar los valores deuna coleccion


def update():
    try:
        criteria = input("\n Ingrese el id del registro a actualizar \n")

         # ingresar los datos de la coleccion a actualizar
        cedula_ruc = input("ingrese la cedula correcto: ")
        nombre = input("ingrese el nombre correcto: ")
        apellidos = input("ingrese el apellido correcto: ")

         # vamos a utilzar la coleccion correcta para almacenar la data
        db.cliente.update_one(
            {"id": float(criteria)},
            {
                "$set":{"ceduela_ruc":cedula_ruc,
                "nombre":nombre,
                "apellido": apellidos,
                }
            }
            
         )
        print
        ("""
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !REGISTRO ACTUALIZADO CORECCTAMENTE!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """)
    except ImportError:
        plataform_specific_module = None
        print(str(e))
        print("No se localizo el registro ")
