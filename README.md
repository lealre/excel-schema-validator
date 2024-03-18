# Excel Schema Validator

This project consists of a web application that validates a specific Excel schema and stores the data in a database. The contract schema represents the required structure that we want to enforce and consolidate. Excel files that do not adhere to this specific schema will not be stored. For any schema that differs from the contract, the application will display a message to the user, indicating where the data schema differs from the contract schema.

![](pics/app-diagram.PNG)

This project uses the following contract to validate the inputted data:

| Column   | Data Type                                 |
|----------|-------------------------------------------|
| email    | Email structure (text@text.com)           |
| date     | Date (yyyy-mm-dd)                         |
| value    | Numeric Positive                          |
| product  | Text                                      |
| amount   | Numeric Positive Integer                  |
| category | Only 3 options (*category1*, *category2* or *category3*) |

## Context

The context of this project reflects a common scenario within organizations, where various departments routinely exchange data using Excel files that adhere to a predefined table schema. However, errors or inconsistencies, such as missing data or unexpected data formats, can disrupt workflows and cause delays in projects. By defining a clear data contract that outlines the expected structure, the application can identify any deviations from this contract. It alerts users to discrepancies, highlighting the specific rows and columns where the data does not conform to the agreed-upon schema.

## How to run this project

To properly run this project, you should connect the app with your own PostgresSQL DataBase. You can do this by running the following comand in terminal:

```bash
echo "POSTGRES_USER=<your-database-keys>" >> .env
echo "POSTGRES_PASSWORD=<your-database-keys>" >> .env
echo "POSTGRES_HOST=<your-database-keys>" >> .env
echo "POSTGRES_PORT=<your-database-keys>" >> .env
echo "POSTGRES_DB=<your-database-keys>" >> .env
```

### Local Setup

pyenv
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

virtualenv
```bash
python -m venv .venv
source .venv/bin/activate
```

install dependenies
```bash
pip install -r requirements.txt
```

run the app
```bash
task run
```

run the tests
```bash
task run
```

### Using Docker

1. Build the image


```bash
docker build -t excel-schema .
````

2. Create the container

```bash
docker run -d -p 8051:8051 --name excel-schema-container excel-schema
```

3. Access link in your browser


## Developments tools

- pandas
- pydantic
- pytest
- selenium 
- streamlit
- taskipy