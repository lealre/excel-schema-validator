import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM vendas', con=DATABASE_URL)

    # Verificar se o DataFrame não está vazio
    assert not df.empty, "DataFrame is empty."

    # Verificar o schema (colunas e tipos de dados)
    expected_dtype = {
        'email': 'object',  
        'data': 'datetime64[ns]',
        'valor': 'float64',
        'quantidade': 'int64',
        'produto': 'object',
        'categoria': 'object'
    }
    print(df.dtypes.to_dict())
    assert df.dtypes.to_dict() == expected_dtype, "The DataFrame schema is not correct."