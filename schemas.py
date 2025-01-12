from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MachineBase(BaseModel):
    machine_name: str
    machine_type: str
    operational_status: str
    efficiency: float
    last_maintenance: datetime


class MachineCreate(MachineBase):
    pass


class Machine(MachineBase):
    id: int

    class Config:
        orm_mode = True