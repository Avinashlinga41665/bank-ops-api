
from fastapi import FastAPI
from api import employees
from api import qatestcases


app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Bank Dashboard API is running"}


app.include_router(
    employees.router,
    prefix="/api/employees",
    tags=["Employees"]
)
app.include_router(
    qatestcases.router,
    prefix="/api/qatestcases",
    tags=["QATestCases"]
)
