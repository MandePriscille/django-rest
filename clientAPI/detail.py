import requests



endpoint = "http://127.0.0.1:8000/product/detail/1/"
# reponse = requests.get(endpoint)
reponse = requests.get(endpoint)
print(reponse.json()) 
print(reponse.status_code)