try:
    with open("lab10.txt", "w") as file:
        file.write("Федоренко\n")
        file.write("Питання:Що виконує функція open()?\n")
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
