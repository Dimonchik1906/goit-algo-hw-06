from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Імʼя не має бути пустим")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону має бути 10 чисел")
        super().__init__(value)           

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    # видалення контакту
    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if p.value != phone_number]
    # пошук номера
    def find_phone(self, number):
        for p in self.phones:
            if p.value == number:
                return p
        return None
    # зміна номеру
    def edit_phone(self, old_number, new_nuber):   
        number = self.find_phone(old_number)
        if number:
            self.remove_phone(old_number)
            self.add_phone(new_nuber)
            return
        raise ValueError("Номер телефону не знайдено")
    # ввивід тексту
    def __str__(self):
        return f"Імʼя контакту: {self.name.value}, телефон: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # додати запис
    def add_record(self, record):
        self.data[record.name.value] = record
    # знайти запис
    def find(self, name):
        return self.data.get(name, None)
    # видалити запис
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Тестування роботи класів
if __name__ == "__main__":
    book = AddressBook()
    
    john_record = Record("John")
    john_record.add_phone("1234567890")   
    john_record.add_phone("5555555555")
    john_record.add_phone("0987654321")
    book.add_record(john_record)
    jane_record = Record("Jane")
    jane_record.add_phone("9876511111")
    book.add_record(jane_record)
    print(book)
    john = book.find("John")
    john.edit_phone("1234567890", "1112223334")
    print(john)
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    book.delete("Jane")
    john_record.remove_phone("0987654321")
    print(book)

