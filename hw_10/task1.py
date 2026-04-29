def init():
    return {}


def add_to_dict(d, lst):
    d[lst[0]] = lst[1]


def remove_from_dict(phonebook, key):
    del phonebook[key]


def value_by_key(phonebook, key):
    return phonebook.get(key)


def list_of_keys(phonebook):
    return list(phonebook.keys())


def key_exist(phonebook, key):
    return key in phonebook


def main():
    command_list = ["add", "remove", "list", "show", "exit"]
    phone_book = init()
    while True:
        user_input = input("Enter the command: ")
        parts = user_input.split()
        command = parts[0].lower()
        if command == "add" and len(parts) == 3:
            if key_exist(phone_book, parts[1]):
                print(f"{parts[1].title()} already exists")
            else:
                contact = parts[1:3]
                add_to_dict(phone_book, contact)
        elif command == "remove" and len(parts) == 2:
            remove_from_dict(phone_book, parts[1])
        elif command == "list":
            print(list_of_keys(phone_book))
        elif command == "show" and len(parts) == 2:
            result = value_by_key(phone_book, parts[1])
            if result:
                print(f"Phone: {result}")
            else:
                print("Name not found")
        elif command == "exit":
            break
        else:
            print("Available features:", ", ".join(command_list))


if __name__ == "__main__":
    main()

