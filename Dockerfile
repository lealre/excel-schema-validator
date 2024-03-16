FROM python:3.11.5-slim AS base
COPY . /src
WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8051
ENTRYPOINT [ "task", "run", "--server.port=8051", "serve.address=0.0.0.0" ]