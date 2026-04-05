from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, dependencies

router = APIRouter()

@router.post("/clients/")
def create_client(client: schemas.ClientCreate, db: Session = Depends(dependencies.get_db)):
    new_client = models.Client(client_name=client.client_name, created_by="admin")
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@router.get("/clients/")
def get_clients(db: Session = Depends(dependencies.get_db)):
    return db.query(models.Client).all()

@router.get("/clients/{id}")
def get_client(id: int, db: Session = Depends(dependencies.get_db)):
    client = db.query(models.Client).filter(models.Client.id == id).first()
    if not client:
        raise HTTPException(404, "Client not found")
    return client

@router.put("/clients/{id}")
def update_client(id: int, client: schemas.ClientCreate, db: Session = Depends(dependencies.get_db)):
    db_client = db.query(models.Client).filter(models.Client.id == id).first()
    if not db_client:
        raise HTTPException(404, "Client not found")

    db_client.client_name = client.client_name
    db.commit()
    return db_client

@router.delete("/clients/{id}", status_code=204)
def delete_client(id: int, db: Session = Depends(dependencies.get_db)):
    client = db.query(models.Client).filter(models.Client.id == id).first()
    if not client:
        raise HTTPException(404, "Client not found")

    db.delete(client)
    db.commit()