# Exomiser REST API Mocking Server

Mocking the Exomser REST API server for VarFish development.

The server responds to requests like the original implementation and returns random numbers as scores.

## Setup

Create a Python environment of your choice, e.g. with conda.

```bash
# git clone https://github.com/bihealth/exomiser-rest-api-mock
# cd exomiser-rest-api-mock
# conda create -n exomiser-rest-api-mock python=3.10
# conda activate exomiser-rest-api-mock
# pip install Flask
```

## Use

The server will be listening on `localhost:5001`.
The port can be changed and should not be default in case you run already the CADD REST API server on the default port.

```bash
# flask --app mock run --port 5001
```

In the VarFish `.env`, activate CADD. Make sure to include the protocol when pointing to the server.

```bash
VARFISH_ENABLE_EXOMISER_PRIORITISER=1
VARFISH_EXOMISER_PRIORITISER_API_URL=http://localhost:5001
```
