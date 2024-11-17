try:
    with open("lab10.txt", "w") as file:
        file.write("Федоренко\n")
        file.write("Питання:Що виконує функція open()?\n")
        file.write("Куцомеля\n") # Додано прізвище
        file.write("Відповідь: Функція open() відкриває файл і повертає об'єкт файлу, " # Відьповідь на питання
                    "який дозволяє працювати з файлом (читати з нього, записувати в нього тощо). "
                    "Вона приймає два основні параметри: шлях до файлу і режим відкриття (наприклад, "
                    "'r' для читання,'w' для запису). При необхідності можна вказати кодування.\n")
        file.write("Питання: Як працює функція close()?\n") #Наступне питання для третього студента
        
    print("Дані успішно записані у файл 'lab10.txt'.")

    # Читання та вивід вмісту текстового файлу
    with open("lab10.txt", "r") as file:
        print("\nВміст файлу:")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Файл не знайдено. Перевірте шлях до файлу.")
except IOError:
    print("Сталася помилка введення/виведення.")
except Exception as e:
    print(f"Невідома помилка: {e}")
