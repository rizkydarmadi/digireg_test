## requirement

- python 3.11
- docker-compose

## how to install

- run docker compose for postgres

```bash
sudo docker-compose up -d
```

- create table contact

```bash
psql -h localhost -p 5462 -U postgres postgres -f sql/seed.sql
```

- or write in sql

```sql
CREATE TABLE contact (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  phone VARCHAR(20)
);
```

- create virtual environtment

```bash
python -m venv env
```

- install all dependencies

```bash
pip install -r requirements.txt
```

## Test it

```bash
pytest test.py
```
