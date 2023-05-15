import requests

import json

def obter_token_e_fazer_post(client_id, client_secret, body, url_obter_token, url_requisicao):

    # Obter o token via STS POST usando o client id e o client secret

    token_response = requests.post(url_obter_token, data={

        'grant_type': 'client_credentials',

        'client_id': client_id,

        'client_secret': client_secret

    })

    # Verificar se a solicitação foi bem-sucedida e obter o token

    if token_response.status_code == 200:

        token = token_response.json()['access_token']

        # Fazer a solicitação POST com o token e o corpo

        headers = {

            'Authorization': f'Bearer {token}',

            'Content-Type': 'application/json'

        }

        response = requests.post(url_requisicao, headers=headers, data=json.dumps(body))

        # Verificar se a solicitação foi bem-sucedida e retornar a resposta

        if response.status_code == 200:

            return response.json()

        else:

            raise Exception('A solicitação POST falhou')

    else:

        raise Exception('Não foi possível obter o token')

# Exemplo de uso

client_id = 'seu_client_id'

client_secret = 'seu_client_secret'

body = {'nome': 'João', 'idade': 30}

url_obter_token = 'https://sua_api.com.br/token'

url_requisicao = 'https://sua_api.com.br/requisicao'

resultado = obter_token_e_fazer_post(client_id, client_secret, body, url_obter_token, url_requisicao)

print(resultado)

