from collections import defaultdict


class ContactBook():
    def __init__(self):
        self.contacts = defaultdict(dict)
        
    def add_contact(self, name: str, phone: str, email: str = None):
        if name in self.contacts:
            raise KeyError("این اسم در لیست مخاطبان وجود دارند، نمیتوانید اضافه کنید")
        
        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email

    def view_contact(self):
        for name, info in self.contacts.items():
            print(f"name: {name}")
            print(f"Phone number: {info ['phone'] }")
            print(f"email: {info ['email']}")
            print('-'*50)
        
    def update_contact(self, name: str, phone: str = None, email: str = None):
        if name in self.contacts:
            if phone or phone =='': #سیو کردن به صورت خالی
                self.contacts[name]["phone"] = phone
            if email or email =='':
                self.contacts[name]["email"] = email
            
            print("update contact successfully")
            return
        
        print("not contact found!")
            
    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
            print("delete it")
            return
        
        else:
            print("contact not found!")


if __name__ == "__main__":
    contact_book = ContactBook()
    
    print("\n\nWelcome to contact book application!\n")

    while True:
        print("\n1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Quit")
        
        user_choice = input("Please choice an option: ")
        
        if user_choice == '5':
            break
        
        elif user_choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            contact_book.add_contact(name, phone, email)
            
        elif user_choice == '2':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            contact_book.update_contact(name, phone, email)
            
        elif user_choice == '3':
            print("\nlist of contact name: ")
            contact_book.view_contact()
            
        elif user_choice == '4':
            name = input("Enter contact name: ")
            contact_book.delete_contact(name)