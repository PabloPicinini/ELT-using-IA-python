import pandas as pd
from ia_generation_guide import generate_ai_travel_guide

df = pd.read_csv('csv/travel_guide.csv')
first_three = df.head(3)
list_columns = list(first_three.columns) #listando colunas do CSV Original
list_registers = first_three.to_dict(orient='records')

# CSV origem
travel_guide_csv = 'csv/guide_users.csv'

# CSV destino
try:
    df_travel_guide = pd.read_csv(travel_guide_csv)
except:
    df_travel_guide = pd.DataFrame(columns=list_columns) # Criando Dataframe vazio caso o arquivo não exista



for users in list_registers:
    # Gerando um Guia para cada id de usuário
    guide = generate_ai_travel_guide(users)
    # Adicionando no dicionário
    users['guide'] = guide

for user_travel in list_registers:
    id_user = user_travel['id']
    #Verificando se existe este id no csv destino
    id_exists = df_travel_guide[df_travel_guide['id'] == id_user].index  
    if not id_exists.empty:
        # Pegando as mesmas colunas do dataframe destino e gerando um dataframe temporário
        temp_df = pd.DataFrame([user_travel], columns=df_travel_guide.columns)
        # Atualizando linhas do CSV destino com o valores do temp_df
        df_travel_guide.loc[id_exists] = temp_df.values
        
    else:
        # Adiciona registros novos caso não tenha id.
        df_travel_guide = df_travel_guide.append(user_travel, ignore_index=True)


# Registrando no CSV destino
df_travel_guide.to_csv(travel_guide_csv, index=False)

