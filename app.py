import requests

resp = requests.post(
    'https://api.escrow-sandbox.com/2017-09-01/transaction',
    auth=(admin_email, api_secret),
    json={
        "parties": [
            {
                "role": "broker",
                "customer": "me"
            },
            {
                "role": "buyer",
                "customer": buyer_email
            },
            {
                "role": "seller",
                "customer": seller_email
            }
        ],
        "currency": "usd",
        "description": "The sale of Netflix",
        "items": [
            {
                "title": "netflix.com",
                "description": "NFX",
                "type": "general_merchandise",
                "inspection_period": 43200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": 1284.0,
                        "payer_customer": buyer_email,
                        "beneficiary_customer": seller_email
                    }
                ]
            },
            {
                "type": "broker_fee",
                "schedule": [
                    {
                        "amount": 55.0,
                        "payer_customer": buyer_email,
                        "beneficiary_customer": "me"
                    }
                ]
            },
            # {
            #     "type": "broker_fee",
            #     "schedule": [
            #         {
            #             "amount": 35.0,
            #             "payer_customer": seller_email,
            #             "beneficiary_customer": "me"
            #         }
            #     ]
            # }
        ]
    },
)