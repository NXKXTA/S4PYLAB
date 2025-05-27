from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor, QDoubleValidator, QPainter
from PyQt6.QtWidgets import QMainWindow, QTableView, QApplication, QDialog, QComboBox, QLineEdit, QVBoxLayout, QLabel, \
    QDialogButtonBox, QMessageBox, QWidget
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6 import QtGui
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from filter_proxy_model import BMIFilterProxyModel
from filter_dialog import FilterDialog
from person_dialog import PersonDialog
from menu_creator import create_menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расчёт ИМТ")
        self.setGeometry(100, 100, 800, 700)
        self.setWindowIcon(QtGui.QIcon("./primary-kpf.svg"))

        # Модель данных
        # -----------------------------------------------------------------------------------------
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Пол", "Масса (кг)", "Рост(см)", "ИМТ", "Состояние"])

        from imt import people
        for person in people:
            row = [
                QStandardItem(person[0]),  # ID
                QStandardItem(person[1]),  # Пол
                QStandardItem(person[2]),  # Масса
                QStandardItem(person[3]),  # Рост
                QStandardItem(person[4]),  # ИМТ
                QStandardItem(person[5])  # Состояние по ИМТ
            ]
            row[5].setBackground(QColor(person[6]))  # Задать цвет на фоне ячейки состояния

            # Выравнивание по центру для всех столбцов
            for item in row:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.model.appendRow(row)
        # -----------------------------------------------------------------------------------------

        # Добавляем прокси-модель для фильтрации
        self.proxy_model = BMIFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Добавляем строки с данными о людях в таблицу
        # -----------------------------------------------------------------------------------------
        self.table_view = QTableView()
        font = self.table_view.font()
        font.setPointSize(10)  # Задаём размер шрифта
        self.table_view.setFont(font)
        self.table_view.setModel(self.proxy_model)  # Устанавливаем ПРОКСИ-модель
        self.table_view.resizeColumnsToContents()  # Автоматически подгоняет ширину под содержимое
        # ------------------------------------------------------------------------------------------

        # Настройки заголовка
        # ------------------------------------------------------------------------------------------------------------
        header = self.table_view.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравнивание заголовков по центру
        header.setStyleSheet("QHeaderView::section { background-color: #e0e0e0; }")  # Цвет фона

        # Можно вместо автоматической подгонки ширины под содержимое задать ширину каждого столбца вручную:
        # self.table_view.setColumnWidth(0, 40)
        # self.table_view.setColumnWidth(1, 50)
        # self.table_view.setColumnWidth(2, 100)
        # self.table_view.setColumnWidth(3, 100)
        # self.table_view.setColumnWidth(4, 50)
        # self.table_view.setColumnWidth(5, 200)
        # -------------------------------------------------------------------------------------------------------------

        # Отдельный виджет состояния при нажатии
        # -------------------------------------------------------------------------------------------------------------
        # Создаём контейнер для таблицы и виджета состояния
        container = QWidget()
        layout = QVBoxLayout() # Главная выкладка

        # Добавляем таблицу
        layout.addWidget(self.table_view)

        # Создаем виджет состояния
        self.status_widget = QLabel("Выберите запись для отображения состояния")
        self.status_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_widget.setFixedHeight(50)  # Фиксированная высота
        self.status_widget.setStyleSheet("""
                    QLabel {
                        font-size: 14px;
                        font-weight: bold;
                        border: 2px solid #cccccc;
                        border-radius: 5px;
                        padding: 10px;
                    }
                """)
        layout.addWidget(self.status_widget)

        container.setLayout(layout)
        self.setCentralWidget(container)  # Заменяем прямую установку таблицы

        # Подключаем обработчик выбора строки
        self.table_view.selectionModel().selectionChanged.connect(self.update_status_widget)

        # Создание меню
        # ----------------------------------------------------------------------------------
        menubar = create_menu(self)
        self.setMenuBar(menubar)  # Устанавливаем меню в главное окно
        # -----------------------------------------------------------------------------------

    def open_filter_dialog(self):
        dialog = FilterDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            min_val, max_val = dialog.get_values()
            self.apply_filter(min_val, max_val)

    def apply_filter(self, min_val, max_val):
        try:
            self.proxy_model.set_range(min_val, max_val)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка фильтрации: {str(e)}")

    # Отдельный виджет состояния
    # -------------------------------------------------------------------------------------------------------------
    def update_status_widget(self):
        selected_proxy_indexes = self.table_view.selectionModel().selectedRows()

        if len(selected_proxy_indexes) != 1:
            self.status_widget.setText("Выберите одну запись для отображения состояния")
            self.status_widget.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: bold;
                    border: 2px solid #cccccc;
                    border-radius: 5px;
                    padding: 10px;
                }
            """)
            return

        try:
            # Преобразование индекса из прокси-модели
            proxy_index = selected_proxy_indexes[0]
            source_index = self.proxy_model.mapToSource(proxy_index)

            # Проверка валидности индекса
            if not source_index.isValid():
                raise ValueError("Некорректный индекс строки")

            row = source_index.row()

            # Проверка существования элемента в модели
            if row >= self.model.rowCount():
                raise IndexError("Строка за пределами диапазона модели")

            status_item = self.model.item(row, 5)
            if not status_item:
                raise ValueError("Элемент состояния не найден")

            # Получение данных
            status = status_item.text()
            color = status_item.background().color().name()

            # Обновление виджета
            self.status_widget.setText(f"Состояние: {status}")
            self.status_widget.setStyleSheet(f"""
                QLabel {{
                    background: {color};
                    color: {'white' if QColor(color).lightness() < 128 else 'black'};
                    font-size: 14px;
                    font-weight: bold;
                    border: 2px solid #cccccc;
                    border-radius: 5px;
                    padding: 10px;
                }}
            """)

        except Exception as e:
            print(f"Ошибка обновления статуса: {str(e)}")
            self.status_widget.setText("Ошибка отображения состояния")
            self.status_widget.setStyleSheet("""
                QLabel {
                    background: #ffcccc;
                    color: black;
                    border: 2px solid #ff0000;
                    border-radius: 5px;
                    padding: 10px;
                }
            """)
    # -------------------------------------------------------------------------------------------------------------

    # Окно изменения человека
    #--------------------------------------------------------------------------------------------------------------
    def open_edit_dialog(self):
        selected = self.table_view.selectionModel().selectedRows()

        if len(selected) != 1:
            QMessageBox.warning(self, "Ошибка", "Выберите одну запись для редактирования!")
            return

        row = selected[0].row()

        # Получаем текущие данные
        current_data = {
            "gender": self.model.item(row, 1).text(),
            "weight": self.model.item(row, 2).text(),
            "height": self.model.item(row, 3).text()
        }

        # Открываем диалог с текущими данными
        dialog = PersonDialog(initial_data=current_data)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_data = dialog.get_data()
            self.update_person(row, new_data)

    def update_person(self, row, data):
        try:
            # Обновляем базовые данные
            self.model.setItem(row, 1, QStandardItem(data["gender"]))
            self.model.setItem(row, 2, QStandardItem(data["weight"]))
            self.model.setItem(row, 3, QStandardItem(data["height"]))

            # Пересчитываем ИМТ
            weight = float(data["weight"])
            height = float(data["height"])
            bmi = weight / ((height / 100) ** 2)

            # Обновляем статус
            if bmi <= 16:
                condition = "дефицит массы тела"
                color = "#a2d2ff"
            elif 16 <= bmi <= 18.49:
                condition = "недостаточная масса тела"
                color = "#8093f1"  # Цвет: синий
            elif 18.50 <= bmi <= 24.99:
                condition = "норма"
                color = "#d0f4de"  # Цвет: зелёный
            elif 25 <= bmi <= 29.99:
                condition = "избыточная масса тела"
                color = "#fcf6bd"  # Цвет: канареечный, ярко-жёлтый
            elif 30 <= bmi <= 34.99:
                condition = "ожирение 1 степени"
                color = "#ffd670"  # Цвет: оранжевый
            elif 35 <= bmi <= 40:
                condition = "ожирение 2 степени"
                color = "#ff9770"  # Цвет: оранжевый или красный, чё-то такое
            else:
                condition = "ожирение 3 степени"
                color = "#ff70a6"  # Цвет: розовый

            # Обновляем ИМТ и статус
            self.model.setItem(row, 4, QStandardItem(f"{bmi:.3f}"))
            status_item = QStandardItem(condition)
            status_item.setBackground(QColor(color))
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.model.setItem(row, 5, status_item)

            # Обновляем исходные данные
            from imt import people
            if row < len(people):
                people[row] = [
                    str(row + 1),
                    data["gender"],
                    data["weight"],
                    data["height"],
                    f"{bmi:.3f}",
                    condition,
                    color,
                ]

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректные данные!")
    # ------------------------------------------------------------------------------------------------------------------

    # Функция обновления файла
    # ------------------------------------------------------------------------------------------------------------------
    def save_to_file(self):
        from imt import people
        try:
            with open("./data_height_weight.txt", "w") as f:
                for person in people:
                    f.write(f"{person[1]}\n")  # Пол
                    f.write(f"{person[2]}\n")  # Вес
                    f.write(f"{person[3]}\n")  # Рост
            QMessageBox.information(self, "Успех", "Данные успешно сохранены!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    def open_add_dialog(self):
        dialog = PersonDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.add_new_person(data)

    # ------------------------------------------------------------------------------------------------------------------

    # Функция удаления человека
    # ------------------------------------------------------------------------------------------------------------------
    def delete_person(self):
        # Получаем выделенные строки
        selected = self.table_view.selectionModel().selectedRows()

        if not selected:
            QMessageBox.warning(self, "Ошибка", "Выберите человека для удаления!")
            return

        # Удаляем в обратном порядке (чтобы индексы не сдвигались)
        for index in reversed(selected):
            row = index.row()

            # Удаление из модели
            self.model.removeRow(row)

            # Удаление из исходных данных
            from imt import people
            if row < len(people):
                del people[row]

    # ------------------------------------------------------------------------------------------------------------------

    # Функция добавления человека
    # ------------------------------------------------------------------------------------------------------------------
    def add_new_person(self, data):
        try:
            # Расчет ИМТ
            weight = float(data["weight"])
            height = float(data["height"])
            bmi = weight / ((height / 100) ** 2)

            # Определение состояния
            if bmi <= 16:
                status = "дефицит массы тела"
                color = "#a2d2ff"  # Цвет: тёмно-голубой
            elif 16 <= bmi <= 18.49:
                status = "недостаточная масса тела"
                color = "#8093f1"  # Цвет: синий
            elif 18.50 <= bmi <= 24.99:
                status = "норма"
                color = "#d0f4de"  # Цвет: зелёный
            elif 25 <= bmi <= 29.99:
                status = "избыточная масса тела"
                color = "#fcf6bd"  # Цвет: канареечный, ярко-жёлтый
            elif 30 <= bmi <= 34.99:
                status = "ожирение 1 степени"
                color = "#ffd670"  # Цвет: оранжевый
            elif 35 <= bmi <= 40:
                status = "ожирение 2 степени"
                color = "#ff9770"  # Цвет: оранжевый или красный, чё-то такое
            else:
                status = "ожирение 3 степени"
                color = "#ff70a6"  # Цвет: розовый

            # Добавление в модель
            new_id = str(self.model.rowCount() + 1)
            row = [
                QStandardItem(new_id),
                QStandardItem(data["gender"]),
                QStandardItem(data["weight"]),
                QStandardItem(data["height"]),
                QStandardItem(f"{bmi:.3f}"),
                QStandardItem(status)
            ]
            row[-1].setBackground(QColor(color))

            for item in row:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.model.appendRow(row)

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректные данные!")
    # ------------------------------------------------------------------------------------------------------------------

    # Функция рисования диаграммы
    # ------------------------------------------------------------------------------------------------------------------
    def show_bmi_chart(self):
        try:
            from imt import people

            # Собираем статистику
            stats = {
                "дефицит массы тела": 0,
                "недостаточная масса тела": 0,
                "норма": 0,
                "избыточная масса тела": 0,
                "ожирение 1 степени": 0,
                "ожирение 2 степени": 0,
                "ожирение 3 степени": 0
            }

            # Подсчет данных
            total = 0
            for person in people:
                status = person[5]
                if status in stats:
                    stats[status] += 1
                    total += 1

            if total == 0:
                QMessageBox.warning(self, "Ошибка", "Нет данных для построения диаграммы")
                return

            # Создаем серию для круговой диаграммы
            series = QPieSeries()
            color_mapping = {
                "дефицит массы тела": "#a2d2ff",
                "недостаточная масса тела": "#8093f1",
                "норма": "#d0f4de",
                "избыточная масса тела": "#fcf6bd",
                "ожирение 1 степени": "#ffd670",
                "ожирение 2 степени": "#ff9770",
                "ожирение 3 степени": "#ff70a6"
            }

            # Добавляем данные в серию
            for status, count in stats.items():
                if count > 0:
                    slice_ = series.append(f"{status} ({count})", count)
                    slice_.setColor(QColor(color_mapping[status]))
                    slice_.setLabelVisible(True)
                    slice_.setLabelArmLengthFactor(0.2)

            # Настраиваем отображение
            series.setLabelsVisible(True)
            series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)

            # Создаем и настраиваем график
            chart = QChart()
            chart.addSeries(series)
            chart.setTitle("Распределение состояний ИМТ")
            chart.legend().setVisible(True)
            chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
            chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

            # Создаем view для графика
            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
            chart_view.setMinimumSize(800, 600)

            # Создаем диалоговое окно
            dlg = QDialog(self)
            dlg.setWindowTitle("Диаграмма состояний ИМТ")
            dlg.setModal(True)
            layout = QVBoxLayout(dlg)
            layout.addWidget(chart_view)
            dlg.resize(1000, 700)
            dlg.exec()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при построении диаграммы:\n{str(e)}")
    # -------------------------------------------------------------------------------------------------------------


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

