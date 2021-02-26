from flask import Flask, request, render_template
app = Flask(__name__)

import requests

from  config import api_secret

seller_email = 'navneet@metaorigins.com'
buyer_email = 'iamnavneet619@gmail.com'
admin_email = 'navneetsinghsajwan@gmail.com'
base_url = 'https://api.escrow-sandbox.com/2017-09-01/transaction'
def create_json(amount, seller_broker_fee, buyer_broker_fee):
    # print(buyer_email)
    return {
        "parties": [
            {
                "role": "buyer",
                "customer": buyer_email
            },
            {
                "role": "seller",
                "customer": seller_email
            },
            {
                "role": "broker",
                "customer": "me"
            }
        ],
        "currency": "usd",
        "description": "2 Original signed copies of a movie poster for John Wick",

        "items": [
            {
                "title": "2 Lenovo Laptops",
                "description": "Old and damaged",
                "type": "general_merchandise",
                "inspection_period": 259200,
                "quantity": 2,
                "schedule": [
                    {
                        "amount": amount,
                        "payer_customer": buyer_email,
                        "beneficiary_customer": seller_email
                    }
                    ],
                "fees": [
                    {
                        "payer_customer": buyer_email,
                        "split": 0.5,
                        "type": "escrow"
                        },
                    {
                        "payer_customer": seller_email,
                        "split": 0.5,
                        "type": "escrow"
                        },   
                    ]
            },

            {
                "title":"Broker Fee",
                "description": "BF",
                "type": "broker_fee",
                "inspection_period": 259200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": buyer_broker_fee,
                        "payer_customer": buyer_email,
                        "beneficiary_customer": "me"
                    }
                ],
                 "fees": [
                    {
                        "payer_customer": buyer_email,
                        "split": 0.5,
                        "type": "escrow"
                        },
                    {
                        "payer_customer": seller_email,
                        "split": 0.5,
                        "type": "escrow"
                        },   
                    ]
            },
            {
                "title":"Broker Fee",
                "description": "BF",
                "type": "broker_fee",
                "inspection_period": 259200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": seller_broker_fee,
                        "payer_customer": seller_email,
                        "beneficiary_customer": "me"
                    }],
                "fees": [
                    {
                        "payer_customer": buyer_email,
                        "split": 0.5,
                        "type": "escrow"
                        },
                    {
                        "payer_customer": seller_email,
                        "split": 0.5,
                        "type": "escrow"
                        },   
                    ]
            },
        ]
    }

@app.route('/', methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        amount = float(request.form.get("amount"))
        seller_broker_fee = float(0.1 * amount)
        buyer_broker_fee = float(0.1 * amount)
        print(amount, seller_broker_fee, buyer_broker_fee)
        json = create_json(amount, seller_broker_fee, buyer_broker_fee)
        print(json)
        resp = requests.post(base_url, 
                        auth=(admin_email, api_secret),
                        json = json)
        print(amount)
        print(str(resp.status_code))
        if str(resp.status_code) == "201":
            return str("Escrow has been created! Check your email for further proceedings.")
        else:
            return str(resp.status_code)
    return render_template("form.html")


if __name__=='__main__': 
   app.run(port = 8000, debug=True) 