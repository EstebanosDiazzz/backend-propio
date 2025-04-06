from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.controlador.PatientCrud import (
    GetMedicationAdministrationById,
    WriteMedicationAdministration,
    UpdateMedicationAdministration,
    DeleteMedicationAdministration,
)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-propio-medicamentos.onrender.com"],  # Permitir solo este dominio
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Endpoints para Patient
@app.get("/patient/{patient_id}", response_model=dict)
async def get_patient_by_id(patient_id: str):
    status, patient = GetPatientById(patient_id)
    if status == 'success':
        return patient
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="Patient not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

@app.post("/patient", response_model=dict)
async def add_patient(request: Request):
    new_patient_dict = await request.json()
    status, patient_id = WritePatient(new_patient_dict)
    if status == 'success':
        return {"_id": patient_id}
    else:
        raise HTTPException(status_code=500, detail=f"Validating error: {status}")

# Endpoints para MedicationAdministration
@app.get("/medication_administration/{med_admin_id}", response_model=dict)
async def get_medication_administration_by_id(med_admin_id: str):
    status, med_admin = await GetMedicationAdministrationById(med_admin_id)
    if status == "success":
        return med_admin
    elif status == "notFound":
        raise HTTPException(status_code=404, detail="MedicationAdministration not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")


@app.post("/medication_administration", response_model=dict)
async def add_medication_administration(request: Request):
    new_med_admin_dict = await request.json()
    status, med_admin_id = WriteMedicationAdministration(new_med_admin_dict)
    if status == 'success':
        return {"_id": med_admin_id}
    else:
        raise HTTPException(status_code=500, detail=f"Validating error: {status}")

@app.put("/medication_administration/{med_admin_id}", response_model=dict)
async def update_medication_administration(med_admin_id: str, request: Request):
    updated_med_admin_dict = await request.json()
    status = UpdateMedicationAdministration(med_admin_id, updated_med_admin_dict)
    if status == 'success':
        return {"message": "MedicationAdministration updated successfully"}
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="MedicationAdministration not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

@app.delete("/medication_administration/{med_admin_id}", response_model=dict)
async def delete_medication_administration(med_admin_id: str):
    status = DeleteMedicationAdministration(med_admin_id)
    if status == 'success':
        return {"message": "MedicationAdministration deleted successfully"}
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="MedicationAdministration not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
