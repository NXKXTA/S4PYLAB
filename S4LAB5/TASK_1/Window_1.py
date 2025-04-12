# Вид
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QListView, QMessageBox
)
# Импортируем нашу модель NotesModel
from NotesModel import NotesModel


# Создаем класс главного окна, который наследуется от QWidget
class MainWindow(QWidget):
    def __init__(self):
        # Вызываем конструктор родительского класса (QWidget)
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle("Заметки")

        # Устанавливаем размер и положение окна (x, y, width, height)
        self.setGeometry(100, 100, 400, 300)

        # Создаем экземпляр модели NotesModel
        self.model = NotesModel()

        # Создаем поле для ввода текста заметки
        self.note_input = QLineEdit()

        # Создаем кнопку для добавления заметки
        self.add_button = QPushButton("Добавить заметку")

        # Создаем список (QListView) для отображения заметок
        self.notes_list = QListView()

        # Устанавливаем модель для списка заметок
        self.notes_list.setModel(self.model)

        # Создаем вертикальный layout для размещения элементов интерфейса
        layout = QVBoxLayout()

        # Добавляем поле ввода в layout
        layout.addWidget(self.note_input)

        # Добавляем кнопку в layout
        layout.addWidget(self.add_button)

        # Добавляем список заметок в layout
        layout.addWidget(self.notes_list)

        # Устанавливаем layout для главного окна
        self.setLayout(layout)

        # Подключаем сигнал нажатия на кнопку к методу add_note
        self.add_button.clicked.connect(self.add_note)

        # Подключаем сигнал клика по элементу списка к методу delete_note
        self.notes_list.clicked.connect(self.delete_note)

    # Метод для добавления заметки
    def add_note(self):
        # Получаем текст из поля ввода и удаляем лишние пробелы
        text = self.note_input.text().strip()

        # Проверяем, что текст не пустой
        if text:
            # Добавляем заметку в модель
            self.model.add_note(text)

            # Очищаем поле ввода
            self.note_input.clear()
        else:
            # Если текст пустой, показываем предупреждение
            QMessageBox.warning(self, "Ошибка", "Заметка не может быть пустой!")

    # Метод для удаления заметки
    def delete_note(self, index):
        # Удаляем заметку из модели по индексу
        self.model.delete_note(index)