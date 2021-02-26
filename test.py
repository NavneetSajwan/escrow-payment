import requests

requests.post(
    'https://api.escrow-sandbox.com/2017-09-01/transaction',
    auth=(admin_email, api_secret),
    json={
        "parties": [
            {
                "role": "buyer",
                "customer": "ns.chocoboy@gmail.com"
            },
            {
                "role": "seller",
                "customer": "keanu.reaves@test.escrow.com"
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
                "title": "2 movies posters",
                "description": "John Wick movie poster",
                "type": "general_merchandise",
                "inspection_period": 259200,
                "quantity": 2,
                "type": "paypal_deposit",
                "schedule": [
                    {
                        "amount": 3140.0,
                        "payer_customer": "ns.chocoboy@gmail.com",
                        "beneficiary_customer": "keanu.reaves@test.escrow.com"
                    }],
                "fees": [
                    {
                        "payer_customer": "ns.chocoboy@gmail.com",
                        "split": 0.5,
                        "type": "escrow"
                        },
                    {
                        "payer_customer": "keanu.reaves@test.escrow.com",
                        "split": 0.5,
                        "type": "escrow"
                        },   
                    ],
            },

            {
                "title":"Broker Fee",
                "description": "BF",
                "type": "broker_fee",
                "inspection_period": 259200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": 425.0,
                        "payer_customer": "ns.chocoboy@gmail.com",
                        "beneficiary_customer": "me"
                    }
                ],
            },
            {
                "title":"Broker Fee",
                "description": "BF",
                "type": "broker_fee",
                "inspection_period": 259200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": 260.0,
                        "payer_customer": "keanu.reaves@test.escrow.com",
                        "beneficiary_customer": "me"
                    }
                ],
            },
        ]
    },
)