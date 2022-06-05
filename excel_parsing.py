import openpyxl

path_file = input('Введите путь к файлу: ')
separator = input('Введите символ-разделитель: ')
wb = openpyxl.open(path_file, read_only=True)
list_sheet = wb.sheetnames
for sheet in list_sheet:
    with open(sheet, mode='w', encoding='utf8') as file:
        for row in wb[sheet]:
            for col in row:
                file.write(f'{col.value}{separator}')
            file.write('\n')
        file.close()