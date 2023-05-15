import requests

def get_oauth2_token(client_id, client_secret, username, password, token_url):

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    data = {

        'grant_type': 'password',

        'client_id': client_id,

        'client_secret': client_secret,

        'username': username,

        'password': password

    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:

        token_data = response.json()

        access_token = token_data['access_token']

        return access_token

    else:

        return None

def make_authenticated_post_request(url, data, access_token):

    headers = {

        'Authorization': f'Bearer {access_token}',

        'Content-Type': 'application/json'

    }

    response = requests.post(url, json=data, headers=headers)

    return response

# Exemplo de uso

client_id = 'seu_client_id'

client_secret = 'seu_client_secret'

username = 'seu_username'

password = 'seu_password'

token_url = 'URL_para_obter_token'

api_url = 'URL_da_API'

# Obtém o token OAuth2

access_token = get_oauth2_token(client_id, client_secret, username, password, token_url)

if access_token:

    # Dados para a requisição POST

    data = {'key1': 'value1', 'key2': 'value2'}

    # Faz a requisição POST autenticada com o token

    response = make_authenticated_post_request(api_url, data, access_token)

    print(response.status_code)

    print(response.json())

else:

    print('Falha na obtenção do token OAuth2')

