#Связывает phone_book со view

import view
import phone_book as pb
import data_base as db


print(view.main_menu())

def main_menu(choice: int):
    match choice:
        case 1: 
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book) # показываем телефонную книгу
        case 2: 
            db.load_data_base() # добавляем телефонную книгу
            view.load_success() 
        case 3: 
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact() #вызываем функцию для ввода данных нового контакта 
            pb.add_contact(contact)
        case 5: 
            print('5')
        case 6: 
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_seccess()
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 7: 
            print('7')
        case 0: 
            return True


#Делаем while True - будет крутить меню по кругу, пока не введём 0
#Только в случае case 0 возвращает True и срабатывает break
while True:
    choice = view.main_menu()
    if main_menu(choice): 
        view.log_off()
        break
