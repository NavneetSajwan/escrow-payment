import requests

requests.post(
    'https://api.escrow-sandbox.com/2017-09-01/transaction',
    auth=(admin_email, api_secret),
    json={
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
                        "amount": 3140.0,
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
                        "amount": 50.0,
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
                        "amount": 50.0,
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
    },
)