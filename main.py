from add import add_contact
from view import view_contacts
from search import search_contact
from delete import delete_contact

def main():
    contacts=[]

    while True:
        print("1 Add")
        print("2 View")
        print("3 Search")
        print("4 Delete")
        print("5 Exit")

        choice=input("Choice: ")

        if choice=="1":
            add_contact(contacts)

        elif choice=="2":
            view_contacts(contacts)

        elif choice=="3":
            search_contact(contacts)

        elif choice=="4":
            delete_contact(contacts)

        elif choice=="5":
            break

        else:
            print("Invalid\n")

main()