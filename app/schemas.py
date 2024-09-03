from pydantic import BaseModel
from enum import Enum

class UtilityEnum(str, Enum):
    avisame = "avisame"
    revisa = "revisa"
    actualiza = "actualiza"

class CronJobCreate(BaseModel):
    cron_expression: str
    name: str
    utility: UtilityEnum
    llm: str

class CronJob(BaseModel):
    id: int
    cron_expression: str
    name: str
    utility: UtilityEnum
    llm: str

    class Config:
        from_attributes = True
