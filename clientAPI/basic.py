import requests

# endpoint = "http://127.0.0.1:8000/api/"

# response = requests.get(endpoint)

# print(response.json())
# print(response.status_code)


endpoint = "http://127.0.0.1:8000/product/"
reponse = requests.get(endpoint)
print(reponse.json())
print(reponse.status_code)