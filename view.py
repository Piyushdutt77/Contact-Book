def view_contacts(contacts):
    if len(contacts)==0:
        print("No contacts")
        return

    print("Contacts:")
    for c in contacts:
        print(c["name"],c["phone"])
    print()
