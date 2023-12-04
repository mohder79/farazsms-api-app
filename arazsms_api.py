import requests
import json

# API key for authentication
api_key = ""

class FarazSms:
    '''
    API documentation: https://docs.ippanel.com/
    '''

    def __init__(self, api_key):
        # Initialize the FarazSms class with the provided API key
        self.api_key = api_key
        self.base_url = 'https://api2.ippanel.com/api/v1/sms'
        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.api_key,
        }

    def _make_request(self, method, endpoint, data=None):
        # Make a generic HTTP request to the specified endpoint with the given method
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            return {"error": f"Request failed with status code {response.status_code}"}

        # Return the JSON response if successful
        return response.json()

    def send_message(self, number: list, msg: str):
        # Send a single SMS message to the specified recipient numbers
        endpoint = 'send/webservice/single'
        payload = json.dumps({
            "sender": "+985000125475",  # Specify the sender number
            "recipient": number,
            "message": msg,  # Message content
            "description": {
                "summary": 'summary',  # Summary description
                "count_recipient": f"{len(number)}"  # Count of recipients
            },
        })
        return self._make_request("POST", endpoint, data=payload)

    def credit(self):
        # Retrieve the current account credit information
        endpoint = 'accounting/credit/show'
        return self._make_request("GET", endpoint)

    def Delivery_check(self , bulk_id):
        '''
        Check the delivery status of a message with the given bulk ID
        
        The status key in response shows the last status of a recipient:
            2 => delivered
            4 => discarded
            1 => pending
            3 => failed
            0 => send
        '''
        endpoint = f'message/show-recipient/message-id/{bulk_id}'
        return self._make_request("GET", endpoint)

