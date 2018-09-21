import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def files_list():
    migrations_dir = os.path.join(current_dir, migrations)
    all_files_list = os.listdir(path=migrations_dir)
    return all_files_list

def sql_files_list(files_list):
    sql_list = list()
    for file in files_list:
        if '.sql' in file:
            sql_list.append(file)
    return sql_list

def read_file(file_name):
    file_path = os.path.join(current_dir, migrations, file_name)
    with open(file_path, 'r') as file:
        file_data = file.read()
        file_data = file_data.lower()
    return file_data

def search_in_file(sql_files_list):
    files_list = sql_files_list
    while True:
        search = input('Введите фразу для поиска в файле (регистр не важен): ')
        search = search.lower()
        searched_files = list()
        for file_name in files_list:
            if search in read_file(file_name):
                searched_files.append(file_name)
                print(file_name)
        print('Всего найдено файлов: {}'.format(len(searched_files)))
        files_list = searched_files

def core():
    search_in_file(sql_files_list(files_list()))

if __name__ == '__main__':
    core()
    pass
