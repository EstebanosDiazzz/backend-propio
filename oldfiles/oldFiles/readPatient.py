import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para leer todas las administraciones de medicamentos de la colección
def read_medication_administrations_from_mongodb(collection):
    try:
        # Consultar todos los documentos en la colección
        medication_administrations = collection.find()
        
        # Convertir los documentos a una lista de diccionarios
        medication_administration_list = list(medication_administrations)
        
        # Retornar la lista de administraciones de medicamentos
        return medication_administration_list
    except Exception as e:
        print(f"Error al leer desde MongoDB: {e}")
        return None

# Función para mostrar los datos de las administraciones de medicamentos
def display_medication_administrations(medication_administration_list):
    if medication_administration_list:
        for med_admin in medication_administration_list:
            print("Administración de Medicamento:")
            print(f"  ID: {med_admin.get('_id')}")
            print(f"  Estado: {med_admin.get('status', 'Desconocido')}")
            medication = med_admin.get('medicationReference', {}).get('reference', 'Desconocido')
            print(f"  Medicamento: {medication}")
            subject = med_admin.get('subject', {}).get('reference', 'Desconocido')
            print(f"  Paciente: {subject}")
            effective_time = med_admin.get('effectiveDateTime', 'Desconocido')
            print(f"  Fecha y hora de administración: {effective_time}")
            print("-" * 30)
    else:
        print("No se encontraron administraciones de medicamentos en la base de datos.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://Juanesdiaz123-:juanete@tareabioif.p9och.mongodb.net/?retryWrites=true&w=majority&appName=TAREABIOIF"

    # Nombre de la base de datos y la colección
    db_name = "SamplePatientService"
    collection_name = "medication_administrations"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Leer las administraciones de medicamentos de la colección
    medication_administrations = read_medication_administrations_from_mongodb(collection)
    
    # Mostrar los datos de las administraciones de medicamentos
    display_medication_administrations(medication_administrations)
