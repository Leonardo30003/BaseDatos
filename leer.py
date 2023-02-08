from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

def consultar():
    try:
        ornadores=db.ordenador.find()
        print("Presentamos los datos obtenidos de la base de datos")
        for ordenador in ornadores:
            print(ordenador)
    except ImportError:
        platform_specific_module= None
        print(str(e))