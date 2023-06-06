def user_input():
    ask = int(input("Выбери действие\n1 - добавить абонента\n"
                "2 - изменить номер абонента\n"
                "3 - удалить абонента\n"
                "4 - поиск по ФИО \n"
                "5 - поиск по всем данным\n"
                "6 - отсортировать справочник по именам абонентов\n"
                "7 - отсортировать справочник по датам рождения\n"
                "8 - вывод ФИО абонентов\n"
                "9 - вывод справочника\n"
                "0 - выход\n\n"
                ))
    return ask

def input_man():
    name = input("Введи ФИО ").split()
    date = input("Введи дату рождения ")
    phone = input("Введи номер телефона ")
    data = name[0]+" "+name[1] +" "+name[2]+" "+date+" "+phone+" "+"\n"
    return data

def search_fio():
    str = input("Введи ФИО(через пробел) для поиска: ").split()
    return str

def search():
    str = input("Введи любое значение(имя, номер, дату рождения): ")
    return str

def confirm():
    answer = input("Подтвердить изменение/удаление данных? Y/N: ")
    return answer

def edit_number():
    number = input("Введи новый номер телефона: ")
    return number