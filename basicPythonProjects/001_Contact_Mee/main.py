from contact_book import ContactBook

# contacts object
contacts = ContactBook()


def main():
    while True:
        print("=========== Contact Mee ===========")
        menu = """
    1) new contact      2) search contact
    3) edit contact     4) delete contact
    0) exit
        """
        print(menu)
        option = int(input("> "))

        match option:
            case 1:
                name = input("Name: ")
                number = input("Numbers: ")
                contacts.add(name, number)

                # want to save?
                save = input("save contact?(y/n): ")
                if save == "y":
                    contacts.save()
                    print("\ncontact is saved!\n")
            case 2:
                keyword = input("keyword (name/numbers): ")
                myContact = contacts.search(keyword)

                if myContact is None:
                    print("contact not found!")
                    continue

                print(f"\nName: {myContact.name}, Numbers: {myContact.number}\n")
            case 3:
                keyword = input("search contact (name/number): ")
                new_name = input("new name (empty?): ")
                new_number = input("new number (empty?): ")

                success = contacts.edit(
                    keyword,
                    new_name=new_name if new_name else None,
                    new_number=new_number if new_number else None,
                )

                if success:
                    print("\ncontact updated!\n")
                else:
                    print("\nContact not found!\n")
            case 4:
                pass
            case _:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
