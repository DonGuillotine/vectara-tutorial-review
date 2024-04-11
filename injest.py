import os
import requests
import http.client
import json


def create_corpus(api_key , customer_id ,corpus_name,corpus_description):
    conn = http.client.HTTPSConnection("api.vectara.io")
    payload = json.dumps({
        "corpus": {
            "name": corpus_name,  
            "description": corpus_description,  
            "enabled": True,  
            "swapQenc": False,  
            "swapIenc": False,  
            "textless": False,  
            "encrypted": True,  
            "encoderId": 1,  
            "metadataMaxBytes": 0,  
            "customDimensions": [],  
            "filterAttributes": []  
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'customer-id': customer_id,  
        'x-api-key': api_key  
    }
    conn.request("POST", "/v1/create-corpus", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    data_dict = json.loads(data.decode("utf-8"))
    corpus_number = data_dict["corpusId"]
    success_message = data_dict["status"]["statusDetail"]

    return corpus_number, success_message


def save_to_dir(uploaded_file):
    if uploaded_file is not None:
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path