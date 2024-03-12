import pandas as pd
from contract import Sales
from dotenv import load_dotenv
import os

load_dotenv(".env")

# Lê as variáveis de ambiente
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def validate_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []

        # 1 - Checks if there are more columns than it was supposed in the file
        extra_columns = set(df.columns) - set(Sales.model_fields.keys())
    
        if extra_columns:
            return False, False, f"Extra columns detected in Excel file: {(',').join(extra_columns)}"
        
        # 2 - Runs every line in the Excel file to independently validate it and identify missing or incorrectly typed data
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                errors.append([f'Error in row {index + 2}: {e}'])
        
        # Return the dataframe, validation results, and a list of error messages
        return df, True, errors        
    
    except Exception as e:
        return pd.DataFrame, f'Unexpected error: {str(e)}'

def excel_to_sql(df):
    df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index=False)