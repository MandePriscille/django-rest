import requests
endpoint = "http://127.0.0.1:8000/product/update/1/"
response = requests.put(endpoint, json={'name':'tomate', 'content':'', 'price':74})
print(response.json())
print(response.status_code)