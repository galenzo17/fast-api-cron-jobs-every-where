from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cronjobs/", response_model=schemas.CronJob)
def create_cronjob(cronjob: schemas.CronJobCreate, db: Session = Depends(get_db)):
    return crud.create_cronjob(db=db, cronjob=cronjob)

@app.get("/cronjobs/", response_model=list[schemas.CronJob])
def read_cronjobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_cronjobs(db, skip=skip, limit=limit)

@app.delete("/cronjobs/{cronjob_id}", response_model=schemas.CronJob)
def delete_cronjob(cronjob_id: int, db: Session = Depends(get_db)):
    db_cronjob = crud.delete_cronjob(db, cronjob_id=cronjob_id)
    if db_cronjob is None:
        raise HTTPException(status_code=404, detail="CronJob not found")
    return db_cronjob
