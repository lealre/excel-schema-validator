from frontend import ExcelValidatorUI
from backend import validate_excel, excel_to_sql

def main():
    ui = ExcelValidatorUI()

    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        df, errors = validate_excel(uploaded_file)
        ui.display_results(errors) 

        if errors:
            ui.display_wrong_message()
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()


if __name__ == "__main__":
    main() 