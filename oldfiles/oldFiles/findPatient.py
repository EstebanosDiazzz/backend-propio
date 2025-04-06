from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para buscar administraciones de medicamentos por identificador de paciente
def find_medication_administrations_by_patient_identifier(collection, identifier_system, identifier_value):
    try:
        # Consultar los documentos que coincidan con el identificador del paciente
        query = {
            "subject.identifier": {
                "system": identifier_system,
                "value": identifier_value
            }
        }
        medication_administrations = collection.find(query)
        
        # Retornar la lista de administraciones de medicamentos encontradas
        return list(medication_administrations)
    except Exception as e:
        print(f"Error al buscar en MongoDB: {e}")
        return None

# Función para mostrar los datos de las administraciones de medicamentos
def display_medication_administrations(medication_administrations):
    if medication_administrations:
        for med_admin in medication_administrations:
            print("Administración de Medicamento:")
            print(f"  ID: {med_admin.get('_id')}")
            print(f"  Estado: {med_admin.get('status', 'Desconocido')}")
            medication = med_admin.get('medicationReference', {}).get('reference', 'Desconocido')
            print(f"  Medicamento: {medication}")
            effective_time = med_admin.get('effectiveDateTime', 'Desconocido')
            print(f"  Fecha y hora de administración: {effective_time}")
            print("-" * 30)
    else:
        print("No se encontraron administraciones de medicamentos para el paciente especificado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://Juanesdiaz123-:juanete@tareabioif.p9och.mongodb.net/?retryWrites=true&w=majority&appName=TAREABIOIF"

    # Nombre de la base de datos y la colección
    db_name = "SamplePatientService"
    collection_name = "medication_administrations"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Identificador específico del paciente a buscar (reemplaza con los valores que desees)
    identifier_system = "http://hospital.org/patient-identifiers"
    identifier_value = "1020713756"
    
    # Buscar las administraciones de medicamentos por identificador de paciente
    medication_administrations = find_medication_administrations_by_patient_identifier(collection, identifier_system, identifier_value)
    
    # Mostrar los datos de las administraciones de medicamentos encontradas
    display_medication_administrations(medication_administrations)
