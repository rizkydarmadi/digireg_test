import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="zefanya",
    port="5462",
)

# Create a cursor object to interact with the database
cursor = conn.cursor()


class Contact:
    def __init__(self, name: str, number: str) -> None:
        self.name: str = name
        self.number: str = number


class AddresBook:
    def add_contact(name: str, phone_number: str):
        insert_query = "INSERT INTO contact (name,phone) VALUES (%s,%s)"
        cursor.execute(insert_query, (name, phone_number))
        conn.commit()

    def remove_contact(name: str) -> None:
        remove_query = "DELETE FROM contact WHERE name = %s"
        cursor.execute(remove_query, (name,))
        conn.commit()

    def search_contact(name: str) -> str:
        select_query = f"SELECT c.name FROM contact c WHERE c.name ILIKE '%{name}%'"
        cursor.execute(select_query)
        data = cursor.fetchone()
        return data[0]
