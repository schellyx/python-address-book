import mysql.connector
import configparser


config = configparser.ConfigParser()
config.read('db_config.ini')

#database connection
def connect_database():
    return mysql.connector("databaseA.db")

def create_connection():
    connection = mysql.connector.connect(
        host = config['mysql']['host'],
        user = config['mysql']['user'],
        password = config['mysql']['password'],
        database = config['mysql']['database'])
    
    if connection.is_connected():
        return connection
    else:
        print("connection failed")


    connection = create_connection()
    if connection:
        print("connection succesfull")
        connection.close()
    else:
        print("connection failed")

#add funktions 
def create_table():
    db = connect_database()
    cursor = db.cursor()

    query = """
            CREATE TABLE IF NOT EXISTS Contacts 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            values
            ('{name}', {number}, '{email}', '{address}')
            """

    cursor.execute(query)
    db.commit()
    db.close()


def show_contacts():
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            select * from contacts
            """
    cursor.execute(query)
    contacts = cursor.fetchall()

    db.commit()
    db.close()
    return contacts

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


def main():
    create_table()
    while True:
                print("\n --- address book ---")
                print("\n 1. add contacts")
                print("\n 2. show address book")
                print("\n 3. update contacts")
                print("\n 4. delete contacts")
                print("\n 5. stop programm")
                choice = input("please choose an option: \n")
                print(type(choice)) 
                if choice == "1":
                        print("you've chosen option 1!")
                        add_contacts()
                elif choice == "2":
                        print("you've chosen option 2!")
                        show_contacts()
                elif choice == "3":
                        print("you've chosen option 3!")
                        update_contacts()
                elif choice == "4":
                        print("you've chosen option 4!")
                        delete_contacts()
                elif choice == "5":
                        print("you've chosen option 5! Good Bye!")
                        break
                else:
                        print("Please select one of the mentioned options.")
main()