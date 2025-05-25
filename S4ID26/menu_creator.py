from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

def create_menu(parent):
    menubar = QMenuBar(parent)

    # Вкладка Файл
    file_menu = menubar.addMenu("Файл")

    # Добавляем во вкладку "Файл" действие "Выход"
    exit_action = QAction("Выйти", parent)
    exit_action.triggered.connect(parent.close)  # Слот соединён с действием Выйти
    file_menu.addAction(exit_action)

    # Добавляем во вкладку "Файл" действие "Добавить человека"
    add_action = QAction("Добавить человека", parent)
    add_action.triggered.connect(parent.open_add_dialog) # При нажатии кнопки будет вызываться метод open_add_dialog из MainWindow
    file_menu.addAction(add_action)

    # Добавляем во вкладку "Файл" действие "Удалить человека"
    del_action = QAction("Удалить человека", parent)
    del_action.triggered.connect(parent.delete_person)  # Привязка к методу
    file_menu.addAction(del_action)

    # Добавляем во вкладку "Файл" действие "Изменить человека"
    edit_action = QAction("Изменить человека", parent)
    edit_action.triggered.connect(parent.open_edit_dialog)
    file_menu.addAction(edit_action)

    # Добавляем во вкладку "Файл" действие "Сохранить изменения"
    save_action = QAction("Сохранить изменения", parent)
    save_action.triggered.connect(parent.save_to_file)
    file_menu.addAction(save_action)

    # Добавляем во вкладку "Файл" действие "Диаграмма"
    chart_action = QAction("Диаграмма", parent)
    chart_action.triggered.connect(parent.show_bmi_chart)
    file_menu.addAction(chart_action)

    # # Добавляем во вкладку "Файл" действие "Фильтр по ИМТ"
    filter_action = QAction("Фильтр по ИМТ", parent)
    filter_action.triggered.connect(parent.open_filter_dialog)
    file_menu.addAction(filter_action)

    return menubar
