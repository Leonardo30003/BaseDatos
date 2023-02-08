from pymongo import MongoClient

# crear las conexiones para establecer el enlace con mongo

cliente = MongoClient("localhost:27017")
db = cliente.TiendaInformatica

def delete():
    try:
        criteria: input("\nIngrese el registro del id del registtro a actualizar ")
        db.cliente.delete_many(
            {"id":float(criteria)}
        )
        print("registro",criteria,"Eliminado correctamente")
    except ImportError:
        plataform_specific_module = None
        print(str(e))
