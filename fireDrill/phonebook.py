contacts = []


def add_contacts(name, email, phone):
    contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    contacts.append(contact)


def remove_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            break
    return contacts


def main():
    for count in range(2):
        name = input("Enter your name: ")
        email = input("Enter your email address")
        phone = input("Enter your phone number")
        add_contacts(name, email, phone)

        print(contacts)

    name_to_remove = input("Enter name to remove")
    remove_contact(name_to_remove)


main()
print(contacts)
