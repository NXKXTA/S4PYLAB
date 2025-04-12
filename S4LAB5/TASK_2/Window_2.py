from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QTableView, QLabel,
    QFormLayout, QHeaderView, QMessageBox
)
from PyQt6.QtCore import Qt
from ProductsModel import ProductsModel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учёт продуктов")
        self.setGeometry(100, 100, 600, 400)

        # Создаем модель
        self.model = ProductsModel()

        # Создаем элементы интерфейса
        self.name_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.weight_input = QLineEdit()
        self.add_button = QPushButton("Добавить продукт")
        self.total_label = QLabel("Общий вес: 0 кг")
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Настройка таблицы
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Форма для ввода
        form_layout = QFormLayout()
        form_layout.addRow("Название:", self.name_input)
        form_layout.addRow("Количество:", self.quantity_input)
        form_layout.addRow("Вес единицы (кг):", self.weight_input)

        # Основной layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.total_label)
        main_layout.addWidget(self.table_view)
        self.setLayout(main_layout)

        # Подключаем сигналы
        self.add_button.clicked.connect(self.add_product)
        self.model.dataChanged.connect(self.update_total)

        # Инициализируем общий вес
        self.update_total()

    def add_product(self):
        try:
            name = self.name_input.text().strip()
            quantity = int(self.quantity_input.text())
            weight = float(self.weight_input.text())

            if name and quantity > 0 and weight > 0:
                self.model.add_product(name, quantity, weight)
                self.name_input.clear()
                self.quantity_input.clear()
                self.weight_input.clear()
            else:
                QMessageBox.warning(self, "Ошибка", "Некорректные данные")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите числовые значения")

    def update_total(self):
        self.total_label.setText(f"Общий вес: {self.model.total_weight:.2f} кг")