import mysql.connector
import configparser


def connect_database():
    return mysql.connector.connect("address-book.db")

def create_table():
    db = connect_database()
    cursor = db.cursor()

    query = """
            CREATE TABLE contacts 
            (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            number VARCHAR(50),
            email VARCHAR(100),
            address VARCHAR(255)
            )
            """
    
    cursor.execute(query)
    db.commit()
    db.close()


def add_contacts(name, number, email, address):
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            INSERT INTO contacts (name, number, email, adress)
            VALUES (%s, %s, %s, %s, %s)
            """
    values = (name, number, email, address) 
    cursor.execute(query)
    db.commit()
    db.close()


def update_contacts(name, number, email, address):
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            update contacts set name = '{name}', number = {number}, email = '{email}', address = '{address}' where id = {id}
            """
    cursor.execute(query)
    db.commit()
    db.close()


def delete_contacts(id):
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            delete from contacts where id = {id}
            """
    cursor.execute(query)
    db.commit()
    db.close()