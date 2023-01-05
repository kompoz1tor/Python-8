import view
import phone_book as pb
import data_base as db


#Связывает phone_book со view
def main_menu(choice: int):
    match choice:
        case 1: 
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2: 
            db.load_data_base()
        case 3: 
            print()
        case 4: 
            print()
        case 5: 
            print()
        case 6: 
            print()
        case 7: 
            print()
        case 0: 
            return True

print(view.main_menu())
#Делаем while True - будет крутить меню по кругу, пока не введём 0
#Только в случае case 0 возвращает True и срабатывает break
while True:
    choice = view.main_menu()
    if main_menu(choice): 
        view.log_off()
        break
