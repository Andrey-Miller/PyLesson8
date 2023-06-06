import view
import db

def main():
    while True:
        ask = view.user_input()
        print("\n")
        if ask == 1:
            data = view.input_man()
            db.add_name(data)
        elif ask == 2:
            name = view.search_fio()
            search_res = db.search_name(name)
            if search_res == -1:
                print("Не найдено абонетов для изменения\n")
            else:
                number = view.edit_number()
                confirm = view.confirm()
                if confirm == "Y":
                    db.modify(search_res, number)
                    print("Номер обновлен\n")
        elif ask == 3:
            name = view.search_fio()
            search_res = db.search_name(name)
            if search_res == -1:
                print("Не найдено абонетов для удаления\n")
            else:
                confirm = view.confirm()
                if confirm == "Y":
                    db.delete_name(search_res)
                    print("Абонент удален\n")
        elif ask == 4:
            name = view.search_fio()
            db.search_name(name)
        elif ask == 5:
            str = view.search()
            result = db.search_all(str)
        elif ask == 6:
            db.sort_db_name()
        elif ask == 7:
            db.sort_db_data()
        elif ask == 8:
            db.print_name()
        elif ask == 9:
            db.print_db()
        elif ask == 0:
            break
        else:
            print("Неправильная команда\n")

main()
