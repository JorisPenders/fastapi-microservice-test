from typing import Union
import requests
from fastapi import FastAPI
import time
from pydantic import BaseModel

app = FastAPI()

# class Transaction(BaseModel):
#     amount: float
#     description: str
#     direction: str
#     counterparty: str
#     current: str
#     transaction_type: str
#     date: date
#     payment_reference: str
#     currency: str
#     payment_method: str
#     status: str
#     processing_fee: float
#     sender_name: str
#     sender_account: str
#     recipient_name: str
#     recipient_account: str
#     memo: str
#     authorization_code: str
#     routing_number: str
#     batch_id: str

s1 = requests.Session()
# establish connection
s1.get('https://gateway-nginx:81', verify=False)

s2 = requests.Session()
# establish connection
s2.get('https://gateway-nginx:82', verify=False)


trx_sample = {
  "amount": 500.00,
  "description": "Monthly Rent",
  "direction": "Outgoing",
  "counterparty": "XYZ Property Management",
  "current": "1234567890",
  "transaction_type": "Electronic Transfer",
  "date": "2023-05-31",
  "payment_reference": "RNT202305",
  "currency": "USD",
  "payment_method": "Bank Transfer",
  "status": "Pending",
  "processing_fee": 5.00,
  "sender_name": "John Doe",
  "sender_account": "987654321",
  "recipient_name": "Jane Smith",
  "recipient_account": "543216789",
  "memo": "Payment for May rent",
  "authorization_code": "ABCDE12345",
  "routing_number": "123456789",
  "batch_id": "BATCH202305"
}
set_of_trx = [trx_sample] * 25


@app.get("/session")
def read_root():
    start = time.time()

    # loading stuff
    time.sleep(150 / 1000)


    service_1_req = s1.post('https://gateway-nginx:81', json=set_of_trx, verify=False).json()

    # simulate network overhead
    time.sleep(60 / 1000)

    service_2_req = s2.post('https://gateway-nginx:82', json=set_of_trx, verify=False).json()

    # simulate network overhead
    time.sleep(60 / 1000)

    end = time.time()
    total_time = (end - start)

    return {
        'elapsed time in ms': total_time * 1000,
        'json_first': service_1_req,
        'json_second': service_2_req,
        'trx': set_of_trx
    }



@app.get("/nosession")
def read_root():
    start = time.time()

    print('yo')

    # loading stuff
    time.sleep(150 / 1000)

    service_1_req = s1.post('https://gateway-nginx:81', json=set_of_trx, verify=False).json()

    # simulate network overhead
    time.sleep(60 / 1000)

    service_2_req = s2.post('https://gateway-nginx:82', json=set_of_trx, verify=False).json()

    # simulate network overhead
    time.sleep(60 / 1000)

    end = time.time()
    total_time = (end - start)

    return {
        'elapsed time': total_time,
        'json_first': service_1_req,
        'json_second': service_2_req
    }
