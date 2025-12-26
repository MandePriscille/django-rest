import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/'
username = input('entre votre username: \n')
password = getpass("entre votre password: \n")

auth_response = requests.post(endpoint, json={'username':username, 'password':password})

print('voir le token: ',auth_response.json())
print('statut code token: ',auth_response.status_code)

if auth_response.status_code == 200:

    endpoint= "http://127.0.0.1:8000/product/list-product/"
    headers = {
        'Authorization': 'Token 499161350f9261113f9966bf2a8cd5113ffb5160',
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)


