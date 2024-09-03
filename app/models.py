from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class UtilityEnum(str, enum.Enum):
    avisame = "avisame"
    revisa = "revisa"
    actualiza = "actualiza"

class CronJob(Base):
    __tablename__ = "cronjobs"

    id = Column(Integer, primary_key=True, index=True)
    cron_expression = Column(String, index=True)
    name = Column(String, unique=True, index=True)
    utility = Column(Enum(UtilityEnum))
    llm = Column(String)
