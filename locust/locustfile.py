from locust import HttpUser, between, task
import json

# sample_body =   [
#     {
#         "acct_id": "NL21RABO0301234567",
#         "acct_ccy": "EUR",
#         "ntry_seq_nb": 1001,
#         "ctpty_acct_id_iban": "",
#         "bookg_dt_tm_gmt": "1503446400",
#         "ctpty_nm": "Appie 1",
#         "tx_tp": "bc",
#         "dtld_tx_tp": 2,
#         "rmt_inf_ustrd1": "Betaalautomaat 10:52",
#         "bookg_cdt_dbt_ind": "DBIT",
#         "bookg_amt_nmrc": 1920,
#         "bookg_amt": "19.20",
#         "ctpty_acct_id_bban": None
#     }
# ]

# sample_json = json.dumps(sample_body)

# # url = 'https://fnapp-dev-eu-periodicity-paas.azurewebsites.net/api/sequence_detector'

class WebsiteUser(HttpUser):
    # wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get(
            '/',
            # data=sample_json,
            verify=False
        )
