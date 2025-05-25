from PyQt6.QtCore import QSortFilterProxyModel, Qt

# Кастомная прокси-модель
class BMIFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, min_val=0, max_val=100, parent=None):
        super().__init__(parent)
        self.min_val = min_val
        self.max_val = max_val

    def set_range(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 4, source_parent)  # Колонка с ИМТ
        bmi_str = self.sourceModel().data(index, Qt.ItemDataRole.DisplayRole)
        try:
            bmi = float(bmi_str)
            return self.min_val <= bmi <= self.max_val
        except ValueError:
            return False