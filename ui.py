import Note

def menu():
     print("В данном консольном приложении Заметки есть такие функции как \n Вывод всех заметок \n добавление зметок \n удаление заметок \n изменение заметок \n зметка по дате  \n заметка по id \n выход \выберите действие " )


def create_note(number):
    title = text_input(
        input('Название заметки: '), number)
    body = text_input(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)

def text_input(text):
    
       
    text = input('Введите тескт: ')
    
    return text