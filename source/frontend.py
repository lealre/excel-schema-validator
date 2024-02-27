import streamlit as st

class ExcelValidatorUI:
    
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title= "Excel Schema Validator"
        )
    
    def display_header(self):
        st.title("Excel Schema Validator")
    
    def upload_file(self):
        return st.file_uploader("Upload file in the field", type = ["xlsx"])
    
    def display_results(self, validation_result, errors):
        if errors:
            for error in errors:
                st.error(f'Validation error: {error}')
        else:
            st.success('Excel Schema is correct!')