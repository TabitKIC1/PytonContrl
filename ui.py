import Note

def menu():
     print("В данном консольном приложении Заметки есть такие функции как \n 1 - Вывод всех заметок \n 2 - добавление зметок \n 3 - удаление заметок \n 4 - изменение заметок \n 5 - зметка по дате  \n 6 -  заметка по id \n 7 - выход \n выберите действие " )


def create_note(number):
    title = text_input(
        input('Название заметки: '), number)
    body = text_input(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)

def text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text

