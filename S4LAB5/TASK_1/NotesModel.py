# Модель
from PyQt6.QtCore import Qt, QModelIndex, QAbstractListModel


# Создаем класс модели, который наследуется от QAbstractListModel
class NotesModel(QAbstractListModel):
    def __init__(self):
        # Вызываем конструктор родительского класса (QAbstractListModel)
        super().__init__()
        # Инициализируем список для хранения заметок
        self.notes = []

    # Метод data возвращает данные для отображения в представлении (QListView)
    def data(self, index, role):
        # Проверяем, запрашивается ли роль DisplayRole (отображение текста)
        if role == Qt.ItemDataRole.DisplayRole:
            # Возвращаем текст заметки по указанному индексу
            return self.notes[index.row()]

    # Метод rowCount возвращает количество строк (заметок) в модели
    def rowCount(self, parent=QModelIndex()):
        # Возвращаем длину списка заметок
        return len(self.notes)

    # Метод add_note добавляет новую заметку в модель
    def add_note(self, text):
        # Начинаем процесс вставки строки в модель
        # QModelIndex() указывает, что изменения происходят на верхнем уровне
        # self.rowCount() указывает индекс новой строки (в конец списка)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        # Добавляем текст заметки в список
        self.notes.append(text)
        # Завершаем процесс вставки строки
        self.endInsertRows()

    # Метод delete_note удаляет заметку из модели по индексу
    def delete_note(self, index):
        # Получаем номер строки, которую нужно удалить
        row = index.row()
        # Начинаем процесс удаления строки из модели
        # QModelIndex() указывает, что изменения происходят на верхнем уровне
        # row указывает индекс удаляемой строки
        self.beginRemoveRows(QModelIndex(), row, row)
        # Удаляем заметку из списка по индексу
        del self.notes[row]
        # Завершаем процесс удаления строки
        self.endRemoveRows()
