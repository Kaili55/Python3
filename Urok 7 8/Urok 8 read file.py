def open_file():
    while True:
        try:
            file_name = input("ведите название файла: ")
            file = open(file_name, 'r')

        except FileNotFoundError:
            print("Файла с таким названием не существует")
            print("Проверьте написание названия и попробуйте ещё раз")

        else:
            return file


file = open_file()

print("\n Содержимое файла:")
for line in file.readlines():
    print(line.strip('\n'))

file.close()