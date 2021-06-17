from fastapi import FastAPI
from pydantic import BaseModel
########################DATABASE################
import psycopg2
conn = psycopg2.connect(dbname='d70nok57ccpo3a',user='cwpzwvdrsdclqq',password='b3c6013b4a77be9f604e8208f619422b02f03042570bcea1d2edf0498ee033fb',host='ec2-54-242-43-231.compute-1.amazonaws.com',port=5432)

########################
app = FastAPI()
########################

class Person(BaseModel):
    name: str
    mobile: str
    message: str

########################
@app.get("/")
def read_root():
    cur = conn.cursor()
    cur.execute("SELECT * FROM ContactDetails")
    records = cur.fetchall()
    return records

########################

@app.post("/create_patient/")
async def create_person(person: Person):
    global conn
    sql = "SELECT * FROM ContactDetails;"
    cur = conn.cursor()
    cur.execute(sql)
    generated_id=1
    for record in cur:
        generated_id = generated_id + 1
    sql = (f"INSERT INTO ContactDetails (id, patient_name, patient_mobile, patient_message) VALUES ('%d','%s', '%s', '%s');"%(generated_id, person.name, person.mobile , person.message))
    cur.execute(sql)
    conn.commit()
    return person


########################


















###############################################EXAMPLE USER POST TO API

# {
#     "name": "Saswat",
#     "mobile": "8108413675",
#     "message": "Wonderful Experience At Fitphysio"
# }


