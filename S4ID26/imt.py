from data_reader import people


for person in people:
    try:
        imt = str(round(float(person[2]) / ((float(person[3]) / 100) ** 2), ndigits=3))
    except ValueError:
        imt = "-"
    person.append(imt)
    # ИМТ рассчитывается по формуле вес в кг/рост в метрах. Состояния имт определяются так:
    # ниже 16 - дефицит массы тела
    # 16-18,49 - недостаточная масса тела
    # 18,5-24,99 - норма
    # 25-29,99 - избыточная масса тела
    # 30-34,99 - ожирение 1 степени
    # 35-40 - ожирение 2 степени
    # 40+ - ожирение 3 степени
    f_imt = float(person[4])
    if f_imt <= 16:
        condition = "дефицит массы тела"
        color = "#a2d2ff"  # Цвет: тёмно-голубой
    elif 16 <= f_imt <= 18.49:
        condition = "недостаточная масса тела"
        color = "#8093f1"  # Цвет: синий
    elif 18.50 <= f_imt <= 24.99:
        condition = "норма"
        color = "#d0f4de"  # Цвет: зелёный
    elif 25 <= f_imt <= 29.99:
        condition = "избыточная масса тела"
        color = "#fcf6bd"  # Цвет: канареечный, ярко-жёлтый
    elif 30 <= f_imt <= 34.99:
        condition = "ожирение 1 степени"
        color = "#ffd670"  # Цвет: оранжевый
    elif 35 <= f_imt <= 40:
        condition = "ожирение 2 степени"
        color = "#ff9770"  # Цвет: оранжевый или красный, чё-то такое
    else:
        condition = "ожирение 3 степени"
        color = "#ff70a6"  # Цвет: розовый
    person.append(condition)
    person.append(color)

print(people)

