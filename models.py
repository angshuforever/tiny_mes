from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String, unique=True, index=True)
    machine_type = Column(String)
    operational_status = Column(String)  # Running, Idle, Maintenance, Down
    efficiency = Column(Float)  # OEE (Overall Equipment Effectiveness)
    last_maintenance = Column(DateTime)