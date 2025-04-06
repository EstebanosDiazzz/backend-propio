from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from fhir.resources.medicationadministration import MedicationAdministration
import json
import logging

# Configuración del cliente de MongoDB
MONGO_DETAILS = "mongodb+srv://Juanesdiaz123-:juanete@tareabioif.p9och.mongodb.net/?retryWrites=true&w=majority&appName=TAREABIOIF"
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["SamplePatientService"]
collection = db["medication_administrations"]     

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_medication_administration_by_id(med_admin_id: str):
    try:
        med_admin = await collection.find_one({"_id": ObjectId(med_admin_id)})
        if med_admin:
            med_admin["_id"] = str(med_admin["_id"])
            return "success", med_admin
        return "notFound", None
    except Exception as e:
        logger.error(f"Error al obtener la administración de medicación: {e}")
        return "error", None

async def write_medication_administration(med_admin_dict: dict):
    try:
        med_admin = MedicationAdministration(**med_admin_dict)
        validated_med_admin_json = json.loads(med_admin.json())
        result = await collection.insert_one(validated_med_admin_json)
        if result.inserted_id:
            return "success", str(result.inserted_id)
        else:
            return "errorInserting", None
    except Exception as e:
        logger.error(f"Error al validar o insertar la administración de medicación: {e}")
        return f"errorValidating: {str(e)}", None
# Al final de PatientCrud.py

GetMedicationAdministrationById = get_medication_administration_by_id
WriteMedicationAdministration = write_medication_administration

async def update_medication_administration(med_admin_id: str, updated_dict: dict):
    try:
        result = await collection.update_one(
            {"_id": ObjectId(med_admin_id)},
            {"$set": updated_dict}
        )
        if result.matched_count == 0:
            return "notFound"
        return "success"
    except Exception as e:
        logger.error(f"Error actualizando administración de medicación: {e}")
        return f"error: {str(e)}"

async def delete_medication_administration(med_admin_id: str):
    try:
        result = await collection.delete_one({"_id": ObjectId(med_admin_id)})
        if result.deleted_count == 0:
            return "notFound"
        return "success"
    except Exception as e:
        logger.error(f"Error eliminando administración de medicación: {e}")
        return f"error: {str(e)}"

UpdateMedicationAdministration = update_medication_administration
DeleteMedicationAdministration = delete_medication_administration

