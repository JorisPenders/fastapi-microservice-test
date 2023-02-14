from typing import Union
import requests

from fastapi import FastAPI

import time


app = FastAPI()

s1 = requests.Session()
# establish connection
s1.get('https://gateway-nginx:81', verify=False)

s2 = requests.Session()
# establish connection
s2.get('https://gateway-nginx:81', verify=False)


@app.get("/session")
def read_root():
    start = time.time()

    service_1_req = s1.get('https://gateway-nginx:81', verify=False).json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    service_2_req = s2.get('https://gateway-nginx:82', verify=False).json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    end = time.time()
    total_time = (end - start)

    return {
        'elapsed time': total_time,
        'json_first': service_1_req,
        'json_second': service_2_req
    }



@app.get("/nosession")
def read_root():
    start = time.time()

    service_1_req = requests.get('https://gateway-nginx:81', verify=False).json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    service_2_req = requests.get('https://gateway-nginx:82', verify=False).json()

    # simulate network overhead
    # time.sleep(60 / 1000)

    end = time.time()
    total_time = (end - start)

    return {
        'elapsed time': total_time,
        'json_first': service_1_req,
        'json_second': service_2_req
    }
