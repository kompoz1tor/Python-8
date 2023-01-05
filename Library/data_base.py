#Функции
import phone_book as pb


#Путь к "базе данных"
path = 'phone_book.txt'

# 'r' - Метод чтения
#Прочитать построчно наш файл, все строки и запихать в phone_book
#Вывели на печать
def load_data_base():
    with open(path, 'r', encoding = 'UTF-8') as file:
        phone_book = file.readlines() 
    pb.set_phone_book(str_to_list(phone_book)) 
#Возращаем phone_book, после отбаботки функции str_to_list                    

#strip убирает ненужные символы
def str_to_list(phone_book: list):
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(contact.strip().split(';'))
    return new_phone_book

def save_data_base():
    with open(path, 'w', encoding = 'UTF-8') as file:
        file.write(list_to_str())

def list_to_str():
    phone_book = pb.get_phone_book()
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(';'.join(contact) + '\n')
    new_phone_book[-1] = new_phone_book[-1][:-1]
    return ''.join(new_phone_book)
