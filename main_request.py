import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# Configurar os dados de autenticação
client_id = 'SEU_CLIENT_ID'
client_secret = 'SEU_CLIENT_SECRET'
token_url = 'https://api.example.com/oauth/token'

# Criar uma sessão OAuth2 com o cliente de aplicativo back-end
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

# Configurar o cabeçalho de autorização com o token OAuth2
headers = {
    'Authorization': f'Bearer {token["access_token"]}',
    'Content-type': 'application/json'
}

# Configurar os dados JSON a serem enviados na solicitação POST
data = {
    'username': 'johndoe',
    'password': 'secret'
}

# Fazer uma solicitação HTTP POST com dados JSON e autenticação OAuth2
response = requests.post('https://api.example.com/posts', json=data, headers=headers)

# Verificar a resposta da solicitação
if response.status_code == 200:
    print(response.json())
else:
    print('Erro: ', response.status_code)
