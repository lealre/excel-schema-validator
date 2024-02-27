import pandas as pd
from contract import Sales


def validate_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []

        # 1 - Checks if there are more columns than it was supposed in the file
        extra_columns = set(df) - set(Sales.model_fields.keys())

        if extra_columns is None:
            return False, f"Extra columns detected in Excel file: {(',').join(extra_columns)}"
        
        # 2 - Runs every line in the Excel file to independently validate it and identify missing or incorrectly typed data
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                errors.append([f'Error in row {index + 2}: {e}'])
        
        # Return the dataframe, validation results, and a list of error messages
        return True, errors        
    
    except Exception as e:
        return pd.DataFrame, f'Unexpected error: {str(e)}'