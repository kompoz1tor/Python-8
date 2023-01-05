
# Все PRINT и INPUT находятся во view 


def main_menu():
    print('\nВыберите пункт меню: ')
    print('1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu() #В функции main_menu возвращается значение функции choice_main_menu


#Выбор главного меню, делаем переменную choice которая равняется выбранному пункту. С обработкой ошибок на вхождение
# While True - цикл будет работать пока наше число не будет в диапозоне от 0 до 7
def choice_main_menu():
    while True: 
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0,8):
                return choice
            else:
                print('Такого пункта нет, повторите попытку: ')
        except:
            print('Ошибка ввода! Некоректные данные!')

#В phone_book содержатся списки в списке. Мы проходимся по основному списку, каждый контакт это маленький список. Enumerate
#*contact - развернет список и выдаст значения без символов списка, а именно [], '', и ','
def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста, или не загружена!')

def log_off():
    print('До свидания! До новых встреч!')