import requests
import json

# URL da API que você deseja acessar
url = "https://v2.jokeapi.dev/joke/Any?lang=pt"

# Se necessário, adicione a chave de acesso (API key)
#params = {
#    "api_key": "sua_api_key_aqui"
#}

# Faça a requisição GET
response = requests.get(url)

# Verifique se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # A resposta geralmente será em formato JSON
    dados = response.json()
        
    # Extrair apenas os campos "setup" e "delivery"
    setup = dados.get("setup", "")
    delivery = dados.get("delivery", "")

    # Criar um novo dicionário com os campos desejados
    campos_desejados = {
        "setup": setup,
        "delivery": delivery
    }

    # Formatar a saída com indentação
    formatted_response = json.dumps(campos_desejados, indent=4)

    # Imprimir a saída formatada
    print(formatted_response)
    
else:
    print("Falha na requisição. Código de status:", response.status_code)
