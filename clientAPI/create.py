import requests

endpoint= "http://127.0.0.1:8000/product/create/"
response = requests.post(endpoint, json={'name':'melon', 'content':'', 'price':45})
print(response.json())
print(response.status_code)


