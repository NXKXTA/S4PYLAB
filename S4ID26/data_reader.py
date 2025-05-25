file_path = "./data_height_weight.txt"
people = []
with open(file_path, "r") as file:
    chunk = []  # Временный буфер для тройки данных
    index = 0
    for line in file:
        line = line.strip()
        if line:
            chunk.append(line)
            if len(chunk) == 3:
                try:
                    gender = chunk[0]  # Пол
                    weight = str(round(float(chunk[1]), ndigits=3))  # Масса тела
                    height = str(round(float(chunk[2]), ndigits=3))  # Рост
                    index+=1
                    people.append([str(index), gender, weight, height])
                    chunk = []
                except (IndexError, ValueError) as e:
                    print(f"Ошибка в данных: {e}. Пропускаю строки {index * 3 - 2} - {index * 3}")
# print(people)