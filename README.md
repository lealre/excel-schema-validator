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

The context of this project reflects a common scenario within organizations, where various departments routinely exchange data using Excel files that adhere to a predefined table schema. However, errors or inconsistencies, such as missing data or unexpected data formats, can disrupt workflows and cause delays in projects. By defining a clear data contract that outlines the expected structure, the application can identify any deviations from this contract. It alerts users to discrepancies, highlighting the specific rows and columns where the data does not conform to the agreed-upon schema.

## How to run this project

### Using Docker

1. Build the image

```bash
docker build -t excel-schema .
````

2. Create the container

```bash
docker run -d -p 8051:8051 --name excel-schema-container excel-schema
```

## Developments tools

pandas==2.2.0
pydantic==2.6.2
pytest==8.0.2
selenium==4.18.1
streamlit==1.31.0
taskipy==1.12.2