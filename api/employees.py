
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.employee import Employee

router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees


@router.get("/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()

    if employee is None:
        return {"message": "Employee not found"}

    return employee