import requests

resp = requests.post(
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
            },
        ],
        "currency": "usd",
        "description": "The sale of Burj Khalifa",
        "items": [
            {
                "title": "Biggest sale",
                "description": "BK",
                "type": "general_merchandise",
                "inspection_period": 43200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": 2201.0,
                        "payer_customer": buyer_email,
                        "beneficiary_customer": seller_email
                    }
                ],
                "extra_attributes": {
                    "image_url": "https://i.ebayimg.com/images/g/RicAAOSwzO5e3DZs/s-l1600.jpg",
                    "merchant_url": "https://www.ebay.com"
                }
            },
                        {
                "title": "Broker Fee",
                "description": "HG",
                "type": "broker_fee",
                "inspection_period": 43200,
                "quantity": 1,
                "schedule": [
                    {
                        "amount": 425.0,
                        # "payer_customer": buyer_email,
                        "split": 0.5,
                        "beneficiary_customer": "me"
                    }
                ],
            }
        ],
        "fees": [
                {
                    "amount": 100.0,
                    # "payer_customer": "john.wick@test.escrow.com",
                    "split": 0.5,
                    "type": "escrow"
                }
            ],
        "type": 'paypal_deposit'
    },
)