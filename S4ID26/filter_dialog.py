from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QDialogButtonBox, QMessageBox
from PyQt6.QtGui import QDoubleValidator

class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Фильтр по ИМТ")

        layout = QVBoxLayout()

        # Поля ввода
        self.min_edit = QLineEdit()
        self.min_edit.setPlaceholderText("Минимальный ИМТ")
        self.max_edit = QLineEdit()
        self.max_edit.setPlaceholderText("Максимальный ИМТ")

        # Валидаторы для чисел
        self.min_edit.setValidator(QDoubleValidator(0, 100, 2))
        self.max_edit.setValidator(QDoubleValidator(0, 100, 2))

        # Кнопки
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.validate)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(QLabel("Диапазон ИМТ:"))
        layout.addWidget(self.min_edit)
        layout.addWidget(self.max_edit)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def validate(self):
        try:
            min_val = float(self.min_edit.text()) if self.min_edit.text() else 0
            max_val = float(self.max_edit.text()) if self.max_edit.text() else 100

            if min_val < 0 or max_val < 0:
                raise ValueError("ИМТ не может быть отрицательным")

            if min_val > max_val:
                raise ValueError("Минимальное значение не может превышать максимальное")

            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def get_values(self):
        return (
            float(self.min_edit.text()) if self.min_edit.text() else 0,
            float(self.max_edit.text()) if self.max_edit.text() else 100
        )