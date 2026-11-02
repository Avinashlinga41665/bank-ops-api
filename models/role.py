
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Role(Base):
    __tablename__ = "Role"

    role_id = Column("Role_ID", Integer, primary_key=True, autoincrement=True)
    role_name = Column("Role_Name", String(100), nullable=False)

    employees = relationship("Employee", back_populates="role")



