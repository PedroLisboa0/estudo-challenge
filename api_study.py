import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    usuarios = response.json()
    for u in usuarios:
        print(f"Name: {u["name"]}, email: {u["email"]}")
else:
    print("Erro ao acessar a API.")
