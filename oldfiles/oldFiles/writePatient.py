import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para guardar un recurso FHIR en MongoDB
def save_fhir_resource_to_mongodb(resource_json, collection):
    try:
        # Convertir el JSON string a un diccionario de Python
        resource_data = json.loads(resource_json)

        # Insertar el documento en la colección de MongoDB
        result = collection.insert_one(resource_data)

        # Retornar el ID del documento insertado
        return result.inserted_id
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    uri = "mongodb+srv://Juanesdiaz123-:juanete@tareabioif.p9och.mongodb.net/?retryWrites=true&w=majority&appName=TAREABIOIF"
    db_name = "SamplePatientService"
    collection_name = "medication_administrations"

    collection = connect_to_mongodb(uri, db_name, collection_name)

    medication_administration_json = '''
    {
      "resourceType": "MedicationAdministration",
      "id": "medadmin001",
      "status": "completed",
      "medicationCodeableConcept": {
        "coding": [
          {
            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
            "code": "123456",
            "display": "Paracetamol 500mg tablet"
          }
        ],
        "text": "Paracetamol 500mg tablet"
      },
      "subject": {
        "reference": "Patient/123456789",
        "display": "Mario Enrique Duarte"
      },
      "effectiveDateTime": "2025-04-05T14:30:00-05:00",
      "performer": [
        {
          "actor": {
            "reference": "Practitioner/987654321",
            "display": "Dr. Juan Pérez"
          },
          "function": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/med-admin-perform-function",
                "code": "performer",
                "display": "Performer"
              }
            ]
          }
        }
      ],
      "dosage": {
        "text": "500mg vía oral cada 8 horas",
        "route": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
              "code": "PO",
              "display": "Oral"
            }
          ]
        },
        "dose": {
          "value": 500,
          "unit": "mg",
          "system": "http://unitsofmeasure.org",
          "code": "mg"
        }
      }
    }
    '''

    inserted_id = save_fhir_resource_to_mongodb(medication_administration_json, collection)

    if inserted_id:
        print(f"Recurso MedicationAdministration guardado con ID: {inserted_id}")
    else:
        print("No se pudo guardar el recurso MedicationAdministration.")
