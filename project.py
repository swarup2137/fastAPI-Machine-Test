from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, dependencies

router = APIRouter()

@router.post("/projects/")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(dependencies.get_db)):
    client = db.query(models.Client).filter(models.Client.id == project.client_id).first()
    if not client:
        raise HTTPException(404, "Client not found")

    users = db.query(models.User).filter(models.User.id.in_(project.users)).all()
    if len(users) != len(project.users):
        raise HTTPException(400, "Some users not found")

    new_project = models.Project(
        project_name=project.project_name,
        client_id=project.client_id
    )
    new_project.users = users

    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get("/projects/")
def get_projects(db: Session = Depends(dependencies.get_db)):
    return db.query(models.Project).all()

@router.delete("/projects/{id}", status_code=204)
def delete_project(id: int, db: Session = Depends(dependencies.get_db)):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(404, "Project not found")

    db.delete(project)
    db.commit()