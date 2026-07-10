from contact_book import ContactBook


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
                number = int(input("Numbers: "))
                contact = ContactBook()
                contact.add(name, number)

                # want to save?
                save = input("save contact?(y/n): ")
                if save == "y":
                    contact.save()
                    print("\ncontact is saved!\n")
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
