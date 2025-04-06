from fhir.resources.medicationadministration import MedicationAdministration
import json

# Ejemplo de uso
if __name__ == "__main__":
    # JSON string correspondiente al recurso MedicationAdministration de HL7 FHIR
    medication_administration_json = '''
    {
        "resourceType": "MedicationAdministration",
        "id": "medadminexample03",
        "status": "on-hold",
        "medicationReference": {
            "reference": "Medication/med0303"
        },
        "subject": {
            "reference": "Patient/pat1",
            "display": "Donald Duck"
        },
        "effectiveDateTime": "2015-01-15T14:30:00+01:00",
        "performer": [
            {
                "actor": {
                    "reference": "Practitioner/f007",
                    "display": "Patrick Pump"
                }
            }
        ],
        "reasonCode": [
            {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "28036006",
                        "display": "High blood pressure"
                    }
                ]
            }
        ],
        "note": [
            {
                "text": "Patient started Bupropion this morning - will administer in a reduced dose tomorrow"
            }
        ]
    }
    '''

    # Validar y crear el objeto MedicationAdministration
    med_admin = MedicationAdministration.parse_raw(medication_administration_json)
    print("JSON validado y convertido a objeto MedicationAdministration:")
    print(med_admin.json(indent=2))
