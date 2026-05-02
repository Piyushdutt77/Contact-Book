def delete_contact(contacts):
    name=input("Enter name to delete: ")

    for c in contacts:
        if c["name"].lower()==name.lower():
            contacts.remove(c)
            print("Deleted\n")
            return

    print("Not found\n")