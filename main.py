import json


def validate_event(event):
    try:
        body = json.loads(event['body'])
        if not all(key in body for key in ['name', 'age']):
            return {'statusCode': 400, 'body': 'Os campos "name" e "age" são obrigatórios.'}
        if not isinstance(body['name'], str):
            return {'statusCode': 400, 'body': 'O campo "name" deve ser uma string.'}
        if not isinstance(body['age'], int):
            return {'statusCode': 400, 'body': 'O campo "age" deve ser um inteiro.'}
        # Se todos os campos obrigatórios estiverem presentes e tiverem os tipos corretos, retorna None para indicar
        # que o evento é válido
        return None
    except None:
        # Se houver qualquer erro ao carregar o JSON do evento, retorna um erro de sintaxe JSON inválido
        return {'statusCode': 400, 'body': 'Sintaxe JSON inválida.'}


def lambda_handler(event, context):
    validation_error = validate_event(event)
    if validation_error is not None:
        return validation_error
    # Se o evento for válido, continue com o processamento normal da função
    # ...
