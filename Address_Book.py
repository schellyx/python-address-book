import mysql.connector
import address_database 
address_book = []

def add():
    add_contacts("Michelle", 45645, "Example@email.com", "Dresden")  
    return
    contacts = input("please enter the contact information of the person you would like to add:")
    if contacts:
        address_book.append(contacts)
        print("your contact {contacts} has been successfull added")
    else:
        print("empty input, please enter a articel")


def show_contacts():
    address_book = select_contacts()
    if address_book:
        print("here is your address book:")
    for contacts in address_book:
        print(contacts)
    else:
        print("your address book is empty")


def update_contacts():
        select = input("please enter id")

        try:
            id = int(select)
            name = input("Please enter the contacts name")
            number_input = input("please enter a phone number")
            number = int(number_input)
            email_input = input("please enter a email address")
            email = int(email_input)
            address = input("please enter a address")
        
            update_contacts(id, name, number, email, address)
        except:
            print("Please enter a number")


def delete_contacts():
    select_contacts = input("Please enter id")

    try:
        id = int(select)
        delete_contacts(id)
    except:
        print("Please enter a number")


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