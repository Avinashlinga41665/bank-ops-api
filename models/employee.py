
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "Employee"

    emp_id = Column(
        "Emp_ID", Integer, primary_key=True, autoincrement=True
    )

    emp_name = Column("Emp_Name", String(100), nullable=False)

    emp_email = Column("Emp_Email", String(100), nullable=False)

    emp_status = Column(
        "Emp_Status", Boolean, nullable=False, default=True
    )

    role_id = Column(
        "Role_ID",
        Integer,
        ForeignKey("Role.Role_ID"),
        nullable=False
    )

    role = relationship("Role", back_populates="employees")
