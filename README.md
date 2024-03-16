# Excel Schema Validator

### Run using Docker

1. Build the image

```bash
docker build -t excel-schema .
````

2. Create the container

```bash
docker run -d -p 8051:8051 --name excel-shema-container excel-schema
```