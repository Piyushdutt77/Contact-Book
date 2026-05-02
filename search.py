def search_contact(contacts):
    name=input("Enter name to search: ")

    found=False

    for c in contacts:
        if c["name"].lower()==name.lower():
            print("Found:",c["name"],c["phone"])
            found=True

    if found==False:
        print("Not found")
        
