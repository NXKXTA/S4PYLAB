from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QCheckBox, QLabel, QDoubleSpinBox, QHBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Столовая ЯрГУ")
        self.setGeometry(100, 100, 300, 300)
        # Список продуктов с названием и ценой
        self.products = [
            {"name": "Суп рассольник", "price": 42},
            {"name": "Бризоль из курицы", "price": 60},
            {"name": "Макароны", "price": 12},
            {"name": "Рис", "price": 20},
            {"name": "Чай", "price": 4},
        ]

        # Основной layout
        self.layout = QVBoxLayout()

        # Создаем виджеты для каждого продукта
        self.product_widgets = []
        for product in self.products:
            self.create_product_widget(product)

        # Метка для отображения общей стоимости
        self.total_label = QLabel("Общая стоимость: 0 руб.")
        self.layout.addWidget(self.total_label)

        # Устанавливаем layout для окна
        self.setLayout(self.layout)

    def create_product_widget(self, product):
        """
            Создает виджеты для одного продукта.

            Аргументы:
                product (dict): Словарь с названием и ценой продукта.
        """
        # Контейнер для продукта
        product_layout = QHBoxLayout()

        # Чекбокс для выбора продукта
        checkbox = QCheckBox(product["name"])  # Создается чекбокс (флажок) с текстом, равным названию продукта
        checkbox.stateChanged.connect(self.update_total)  # stateChanged — это сигнал, который испускается каждый раз, когда состояние чекбокса изменяется
        product_layout.addWidget(checkbox)

        # Виджет для ввода количества (QDoubleSpinBox)
        quantity_input = QDoubleSpinBox()
        quantity_input.setMinimum(1)
        quantity_input.setMaximum(100)
        quantity_input.setValue(1)
        # connect(self.update_total) — этот сигнал подключается к методу update_total, который будет вызываться при изменении состояния чекбокса
        # valueChanged — это сигнал, который испускается каждый раз, когда значение в виджете QDoubleSpinBox (который используется для ввода количества) изменяется.
        # Сигнал valueChanged подключается к методу update_total(а он уже пересчитывает общую стоимость)
        quantity_input.valueChanged.connect(self.update_total)
        product_layout.addWidget(quantity_input)

        # Метка для отображения стоимости продукта
        price_label = QLabel(f"0 руб.")
        product_layout.addWidget(price_label)

        # Добавляем контейнер в основной layout
        self.layout.addLayout(product_layout)

        # Сохраняем виджеты для продукта
        self.product_widgets.append({
            "checkbox": checkbox,
            "quantity_input": quantity_input,
            "price_label": price_label,
            "price": product["price"],
        })

    def update_total(self):
        total_cost = 0

        for widget in self.product_widgets:
            checkbox = widget["checkbox"]
            quantity_input = widget["quantity_input"]
            price_label = widget["price_label"]
            price = widget["price"]

            if checkbox.isChecked():
                # Рассчитываем стоимость продукта
                quantity = quantity_input.value()
                cost = quantity * price
                total_cost += cost

                # Обновляем метку стоимости продукта
                price_label.setText(f"{cost:.2f} руб.")

                # Маркируем выбранный продукт полужирным шрифтом
                checkbox.setStyleSheet("font-weight: bold;")
            else:
                # Сбрасываем стиль и стоимость, если продукт не выбран
                price_label.setText("0 руб.")
                checkbox.setStyleSheet("font-weight: normal;")

        # Обновляем общую стоимость
        self.total_label.setText(f"Общая стоимость: {total_cost:.2f} руб.")