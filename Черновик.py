import os
import re

# Указываем директорию, в которой находятся файлы
directory = r"C:\Users\compm\PycharmProjects\Selenium_2-0"

# Регулярное выражение для поиска файлов по заданному формату
pattern = r"Глава (\d+\.\d+) Урок (\d+)"

for filename in os.listdir(directory):
    # Проверяем, что это файл с расширением .py
    if filename.endswith(".py"):
        # Применяем регулярное выражение для извлечения номеров главы и урока
        match = re.match(pattern, filename.replace(".py", ""))
        if match:
            chapter_number = match.group(1).replace(".", "-")
            lesson_number = match.group(2)

            # Формируем новое имя файла по заданному формату
            new_filename = f"test_Chapter_{chapter_number}_Lesson_{lesson_number}.py"

            # Получаем полный путь к файлу
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            # Переименовываем файл
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")