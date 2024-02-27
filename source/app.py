from frontend import ExcelValidatorUI
from backend import validate_excel

def main():
    ui = ExcelValidatorUI()

    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        validation_result, errors = validate_excel(uploaded_file)
        ui.display_results(validation_result, errors) 



if __name__ == "__main__":
    main() 