def view_contacts(contacts):
    if len(contacts)==0:
        print("No contacts\n")
        return

    print("\nContacts:")
    for c in contacts:
        print(c["name"],c["phone"])
    print()