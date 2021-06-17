# from typing import Optional
from fastapi import FastAPI
# from pydantic import BaseModel
########################DATABASE################
# import psycopg2
# Connect to your postgres DB
# conn = psycopg2.connect(dbname='test',user='test',password='test',host='test',port=5432)
# cur.execute("SELECT * FROM my_data")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


