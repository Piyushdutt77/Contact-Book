def add_contact(contacts):
    name=input("Enter name: ")
    phone=input("Enter phone: ")

    contact={"name":name,"phone":phone}
    contacts.append(contact)

    print("Contact added!")
