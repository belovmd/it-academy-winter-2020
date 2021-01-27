import os

error_messages = {
    'read': 'Unable to read/open file',
    'write': 'Unable to write file'
}


# проверяем, сущ ли файл и открываем его, записываем его строки в file_lines
# если файла нет или ошибка при открытии - выводим ошибку
def try_to_read(file):
    file_lines = []
    if os.path.exists(file):
        with open(file, "r") as list_file:
            try:
                file_lines = list_file.readlines()
            except:
                print(error_messages['read'])
    else:
        print(error_messages['read'])
    return file_lines


def try_to_write(file, content):
    with open(file, "w") as file:
        try:
            file.write(content)
        except:
            print(error_messages['write'])
