from typing import Union

from fastapi import FastAPI
from random import randint
from time import sleep
import time


app = FastAPI()

import psycopg2

# Establishing a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="192.168.68.114",
    database="sportsdb",
    user="postgres",
    password="postgres"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/db")
def get_db():
    st = time.time()

    # Creating a cursor object
    cur = conn.cursor()

    # Executing a SELECT query
    cur.execute("SELECT * FROM public.baseball_event_states LIMIT 1")

    # Fetching all rows from the result set
    rows = cur.fetchall()

    # Closing the cursor and connection
    cur.close()

    et = time.time()

    print(f"Succesful request to the database: {rows}")
    print(f"Call took: {(et - st) * 1000:.2f} ms")

    return {
        'results': rows,
        'query_time_to_db': (et - st) * 1000
    }

@app.post("/")
def read_root_2():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}