from typing import Union
import requests

from fastapi import FastAPI

import time


app = FastAPI()


@app.get("/")
def read_root():
    start = time.time()

    service_1_req = requests.get('http://gateway-nginx:81').json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    service_2_req = requests.get('http://gateway-nginx:82').json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    end = time.time()
    total_time = (end - start)

    return {
        'elapsed time': total_time,
        'json_first': service_1_req,
        'json_second': service_2_req
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}