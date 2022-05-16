from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import database, models
from .routers import auth, budget, user

# models.Base.metadata.create_all(bind=database.engine)


# Create an FastApı object
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(budget.router)
app.include_router(user.router)
app.include_router(auth.router)

# Test sqlalchemy
# @app.get("/sqlalchemy")
# def test_budgets(db: Session = Depends(get_db)):
#    rows = db.query(models.Budget).all()
#    return {"status": rows}
#
#
# Connect postgresql with python
# while True:
#    try:
#        conn = psycopg2.connect(
#            host="localhost",
#            database="homebudget",
#            user="postgres",
#            password="root",
#            cursor_factory=RealDictCursor,
#        )
#        cursor = conn.cursor()
#        print("Database connection was succesful!")
#        break
#    except:
#        print("Connecting to db failed!")
#        time.sleep(2)
#
#
# your_budget = [{"budget": "9000"}]


@app.get("/")
async def root():
    return {"message": "Welcome to HomeBudget Project!!!"}
