# ELT-using-IA-python
Carga de dados, transformação de dados e exportação dos dados, utilizando CSV como banco de dados e Inteligência Artificial.

## Travel Guide Generator

Este é um código Python para gerar guias de viagem personalizados usando o ChatGpt da OpenAI. Ele lê dados de um arquivo CSV de entrada, executa uma consulta ao GPT para gerar guias de viagem personalizados com base nos dados de entrada e, em seguida, salva os guias de viagem gerados em um arquivo CSV de saída.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python: pandas, openai, unicodedata

## Uso
Configure suas credenciais da API da OpenAI, disponível no [site](https://platform.openai.com/account/api-keys):

1. Você precisará configurar sua chave de API da OpenAI no arquivo config.ini no mesmo diretório do código. O arquivo config.ini deve conter o seguinte:
```
[Config]
api_key = 'sua_chave_de_api_aqui'
```

2. Execute o código:
    - Execute o script Python generate_travel_guide.py para gerar os guias de viagem. Certifique-se de estar no diretório correto onde o código está localizado: python `generate_travel_guide.py`

3. Resultado:
    - Os guias de viagem gerados serão salvos em um arquivo CSV de saída chamado guide_users.csv.
    - Este código demonstra como usar o ChatGpt (OpenAI) para automatizar a geração de guias de viagem com base em dados de entrada. 