def add_name(data):
    with open("db.txt", "a") as file:
        file.write(data)
    print("Абонент добавлен\n")

def search_name(name):  # Предполагается, что по ФИО можно найти только 1 человека. Функция также возвращает либо -1, если никого не найдено, либо номер строки в файле(index), где абонент записан. 
    with open("db.txt", "r") as file:
        data = file.readlines()
        flag = False
        index = 0
        for i in data:
            if i.split()[0] == name[0] and i.split()[1] == name[1] and i.split()[2] == name[2]:
                print(f"Найден абонент: {i}")
                index = data.index(i)
                flag = True
        if flag == False:
            print("Абонентов не найдено\n")
            return -1
        else:
            return index

def search_all(str):
    with open("db.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if str in i:
                print(i)
                flag = True
        if flag == False:
            print("Абонентов не найдено\n")

def modify(index, number):
    with open("db.txt", "r") as file:
        data = file.readlines()
        data[index] = data[index].replace(data[index].split()[4], number)
    with open("db.txt", "w") as file:
        file.writelines(data)

def delete_name(index):
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.pop(index)          
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_db_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key = lambda x: x.split()[1])
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_db_data():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key = lambda x: x.split()[4])
    with open("db.txt", "w") as file:
        file.writelines(data)

def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(f"{i.split()[0]} {i.split()[1]} {i.split()[2]}")  

def print_db():
    with open("db.txt", "r") as file:
        print(file.read())