import requests
id = input('Enter the id of product tha you want to delete: ')
endpoint = "http://127.0.0.1:8000/product/delete-product/{id}/"
response = requests.delete(endpoint)
print(response.status_code, response.status_code==204) 