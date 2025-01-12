from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, schemas
from datetime import datetime

app = FastAPI(title="Smart MES Machine Management")
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/machines/", response_model=schemas.Machine)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    db_machine = models.Machine(**machine.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine


@app.get("/machines/", response_model=List[schemas.Machine])
def read_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machines = db.query(models.Machine).offset(skip).limit(limit).all()
    return machines


@app.get("/machines/{machine_id}", response_model=schemas.Machine)
def read_machine(machine_id: int, db: Session = Depends(get_db)):
    machine = db.query(models.Machine).filter(models.Machine.id == machine_id).first()
    if machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine


@app.put("/machines/{machine_id}", response_model=schemas.Machine)
def update_machine(machine_id: int, machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    db_machine = db.query(models.Machine).filter(models.Machine.id == machine_id).first()
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")

    for key, value in machine.dict().items():
        setattr(db_machine, key, value)

    db.commit()
    db.refresh(db_machine)
    return db_machine


@app.delete("/machines/{machine_id}")
def delete_machine(machine_id: int, db: Session = Depends(get_db)):
    machine = db.query(models.Machine).filter(models.Machine.id == machine_id).first()
    if machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")

    db.delete(machine)
    db.commit()
    return {"message": "Machine deleted successfully"}