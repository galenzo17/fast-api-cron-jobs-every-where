from sqlalchemy.orm import Session
from . import models, schemas

def create_cronjob(db: Session, cronjob: schemas.CronJobCreate):
    db_cronjob = models.CronJob(**cronjob.dict())
    db.add(db_cronjob)
    db.commit()
    db.refresh(db_cronjob)
    return db_cronjob

def get_cronjobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CronJob).offset(skip).limit(limit).all()

def delete_cronjob(db: Session, cronjob_id: int):
    db_cronjob = db.query(models.CronJob).filter(models.CronJob.id == cronjob_id).first()
    db.delete(db_cronjob)
    db.commit()
    return db_cronjob
