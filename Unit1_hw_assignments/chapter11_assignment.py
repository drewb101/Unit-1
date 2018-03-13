def sort_contacts(contacts):
    newcontacts=[]
    keys = contacts.keys()
    for key in sorted(keys):
        data = (key, contacts[key][0], contacts[key][1])
        newcontacts.append(data)
    
    return newcontacts
    
contacts = input("Please input the contacts.")
print(sort_contacts(contacts))
