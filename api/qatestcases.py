
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.qatestcase import QATestcases
from schemas.qatestcase import SchemaQATestcase

router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_qatestcases(db: Session = Depends(get_db)):
    qatestcase = db.query(QATestcases).all()
    return qatestcase

@router.get("/{Module}")
def get_qatestcasesbymodule(Module: str, db: Session = Depends(get_db)):
    qatestcase = db.query(QATestcases).filter(QATestcases.module == Module).all()

    if qatestcase is None:
        return {"message": "TestCases not found"}

    return qatestcase

@router.post("/")
def add_qatestcase(request: SchemaQATestcase, db: Session = Depends(get_db)):
    try:
     qatestcase = QATestcases(
        case_name=request.case_name,
        module=request.module,
        description=request.description,
        )
     db.add(qatestcase)
     db.commit()
     db.refresh(qatestcase)
    
     return qatestcase
    except Exception as e:
        return str(e)


@router.put("/{test_case_id}")
def update_qatestcase(test_case_id: int,request: SchemaQATestcase,db: Session = Depends(get_db)):
     try:
      qatestcase = db.query(QATestcases).filter(QATestcases.test_case_id == test_case_id).first()
      if qatestcase is None:
            raise HTTPException(status_code=404,detail="Test case not found")
      qatestcase.case_name = request.case_name
      qatestcase.module = request.module
      qatestcase.description = request.description
      db.commit()
      db.refresh(qatestcase)
    
      return qatestcase
     except Exception as e:
        return str(e)

@router.delete("/{test_case_id}")
def delete_qatestcase(test_case_id: int,db: Session = Depends(get_db)):
     try:
      qatestcase = db.query(QATestcases).filter(QATestcases.test_case_id == test_case_id).first()
      if qatestcase is None:
            raise HTTPException(status_code=404,detail="Test case not found")
      db.delete(qatestcase)
      db.commit()
      
    
      return {
            "message": "Test case deleted successfully",
            "test_case_id": test_case_id
        }
     except Exception as e:
        return str(e)
        