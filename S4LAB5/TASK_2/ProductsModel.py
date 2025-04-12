from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


# Класс Product представляет собой объект продукта
class Product:
    def __init__(self, name, quantity, unit_weight):
        # Инициализируем атрибуты продукта
        self.name = name  # Название продукта
        self.quantity = quantity  # Количество продукта
        self.unit_weight = unit_weight  # Вес одной единицы продукта в килограммах
        self.total_weight = quantity * unit_weight  # Общий вес продукта (количество * вес единицы)


# Класс ProductsModel наследуется от QAbstractTableModel и представляет модель данных для таблицы
class ProductsModel(QAbstractTableModel):
    def __init__(self):
        # Вызываем конструктор родительского класса (QAbstractTableModel)
        super().__init__()
        # Инициализируем список для хранения продуктов
        self.products = []
        # Инициализируем переменную для хранения общего веса всех продуктов
        self._total_weight = 0.0

    # Свойство total_weight возвращает общий вес всех продуктов
    @property
    def total_weight(self):
        return self._total_weight

    # Метод update_total пересчитывает общий вес всех продуктов
    def update_total(self):
        # Суммируем общий вес всех продуктов в списке
        self._total_weight = sum(p.total_weight for p in self.products)
        # Уведомляем представление об изменении данных
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    # Метод rowCount возвращает количество строк (продуктов) в модели
    def rowCount(self, parent=QModelIndex()):
        return len(self.products)

    # Метод columnCount возвращает количество столбцов в модели
    def columnCount(self, parent=QModelIndex()):
        return 4  # Название, Количество, Вес единицы, Общий вес

    # Метод data возвращает данные для отображения в таблице
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # Проверяем, запрашивается ли роль DisplayRole (отображение данных)
        if role == Qt.ItemDataRole.DisplayRole:
            # Получаем продукт по индексу строки
            product = self.products[index.row()]
            # Возвращаем данные для соответствующего столбца
            return [
                product.name,  # Название продукта
                product.quantity,  # Количество продукта
                f"{product.unit_weight:.2f}",  # Вес единицы продукта (форматированный)
                f"{product.total_weight:.2f}"  # Общий вес продукта (форматированный)
            ][index.column()]

    # Метод headerData возвращает заголовки столбцов или строк
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        # Проверяем, запрашивается ли роль DisplayRole и ориентация горизонтальная
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            # Возвращаем заголовок для соответствующего столбца
            return ["Название", "Количество", "Вес единицы (кг)", "Общий вес (кг)"][section]

    # Метод add_product добавляет новый продукт в модель
    def add_product(self, name, quantity, unit_weight):
        # Начинаем процесс вставки строки в модель
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        # Добавляем новый продукт в список
        self.products.append(Product(name, quantity, unit_weight))
        # Завершаем процесс вставки строки
        self.endInsertRows()
        # Обновляем общий вес всех продуктов
        self.update_total()