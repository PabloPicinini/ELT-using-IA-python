import openai
import unicodedata
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# Chave da OpenIA
openai_api_key = config['Config']['api_key']
openai.api_key = openai_api_key


def generate_ai_travel_guide(dados):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "Você é um especialista de Guia de Viagens."
                },
            {
                "role": "user", 
                "content": f"""Crie um Guia turístico de {dados['travel_time']} dias, baseado na idade de {dados['age']} anos, para a cidade {dados['city_desired']} para o cliente {dados['firstname']} para a empresa Guia Já. 
                                Fale nesse Guia em tom atrativo para cativar o cliente
                                Regras: No emoticons, máximo de 200 caracteres
                                """
                
                
            }
        ]
)
    message = completion.choices[0].message.content.strip("\"")
    # Removendo caracteres especiais
    normalized_message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
    
    # Removendo Quebras de linhas
    treated_message = normalized_message.replace('\n', ' ')

    return treated_message

