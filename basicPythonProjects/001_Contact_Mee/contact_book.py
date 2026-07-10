import json
from contact import Contact


class ContactBook:
    def __init__(self):
        self.contacts = list()

        # read contact
        with open("contact.json") as c:
            data = json.load(c)

        # save dictionary as object
        for contact in data:
            contactObject = Contact.from_dict(contact)
            self.contacts.append(contactObject)

    def add(self, name, number):
        # create new object of contact
        newContact = Contact(name, number)
        # append the custom object to contact book
        self.contacts.append(newContact)

    def save(self):
        # create a new list contains dictionary (converted from self.contacts)
        data = [contact.to_dict() for contact in self.contacts]

        # dump to JSON
        with open("contact.json", "w") as c:
            json.dump(data, c)  # no need .write()

    def edit(self, keyword, new_name=None, new_number=None):
        # search for contact
        myContact = self.search(keyword)
        if myContact is None:
            return False

        if new_name:
            myContact.name = new_name
        if new_number:
            myContact.number = new_number

        self.save()
        return True

    def search(self, keyword):
        for contact in self.contacts:
            if contact.name == keyword or contact.number == keyword:
                return contact
        else:
            return None

    def delete(self, keyword):
        myContact = self.search(keyword)
        if myContact is None:
            return False

        self.contacts.remove(myContact)
        self.save()

        return True
