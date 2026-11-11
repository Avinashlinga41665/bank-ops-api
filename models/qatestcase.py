
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class QATestcases(Base):
    __tablename__ = "QATestcases"

    test_case_id = Column("Test_Case_Id", Integer, primary_key=True, autoincrement=True)

    case_name = Column("Case_Name", String(100), nullable=False)

    module = Column("Module", String(100), nullable=False)

    description = Column("Description", String(300), nullable=False)


			