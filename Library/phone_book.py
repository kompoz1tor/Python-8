phone_book = []

#благодаря геттерам мы берём нашу переменную и возвращаем её значение
def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book