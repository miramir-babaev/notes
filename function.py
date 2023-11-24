import operations
import notes
import ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = operations.read_file()
    for notes in array:
        if notes.Note.get_id(note) == notes.Note.get_id(notes):
            notes.Note.set_id(note)
    array.append(note)
    operations.write_file(array, 'a')
    print('Заметка успешно добавлена.')


def show(text):
    logic = True
    array = operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notes.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notes.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notes.Note.get_date(notes):
                print(notes.Note.map_note(notes))
    if logic == True:
        print('У вас нет заметок')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = operations.read_file()
    logic = True
    for notes in array:
        if id == notes.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                notes.Note.set_title(notes, note.get_title())
                notes.Note.set_body(notes, note.get_body())
                notes.Note.set_date(notes)
                print('Заметка успешно изменена.')
            if text == 'del':
                array.remove(notes)
                print('Заметка успешно удалена.')
            if text == 'show':
                print(notes.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет,проверьте вводимые данные')
    operations.write_file(array, 'a')