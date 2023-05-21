## requirement

- python 3.11
- docker-compose

## how to install

- run docker compose for postgres

```bash
sudo docker-compose up -d
```

- create virtual environtment

```bash
python -m venv env
```

- install all dependencies

```bash
pip install -r requirements.txt
```

## Run it

```bash
uvicorn main:app --reload --port 8003
```

- open swagger http://localhost:8003/docs
