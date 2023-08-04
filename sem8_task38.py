# -*- coding: utf-8 -*-
# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
import os, random, shutil

filename = "tell_task.txt"
fn_rnd = ["Остап", "Сулейман", "Иван", "Джон", "Жан", "Мбамбо"]
patr_rnd = ["Иоганнович","Себастьянович", "Берта-Мария", "Иванович", "ибн-Саид"]
ln_rnd = ["Бендер-бей", "Бах", "Смит", "Пеле", "Ли", "фон-Бабай"]

# ---- Случайное заселение
def rnd():
    n = int(input("Количество строк :"))
    for i in range(n):
        first_name = random.choice(fn_rnd)
        patronimic = random.choice(patr_rnd)
        last_name = random.choice(ln_rnd)
        tel = random.randint(200000, 999999)
        with open(filename, "a", encoding="UTF-8") as f:
            f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
        s.append([last_name, first_name, patronimic, tel])
    return

# ----- Открытие и загрузка файла(с семинара. не менял)
def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s

# ----- Ввод с клавиатуры(с семинара. не менял)
def input_tel(s):
    first_name = input("Введите имя: ")
    patronimic = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    tel = input("Введите телефон: ")
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
    s.append([last_name, first_name, patronimic, tel])
    return s

# ---- Поиск (изменено. с семинара, тормозился на первом найденном элементе)
def search_tel(s, object):
    flag = False
    sch = ob = 0
    for line in s:   
        sch += 1
        if object in line or object.capitalize() in line:
            ob += 1
            flag = True
            print(sch, " ".join(line)) 
    if flag == False:
        print("Записи не найдено")     
    return 

# ----- Вывод файла(с семинара.изменено на вывод кол-ва строк)    
def show_tell(s):
    sts = 0
    for line in s:
        sts += 1
        print(sts, " ".join(line))
    return #sts # возвращает количество строк

# ----- Удаление строки
def remove(s):
    show_tell(s)
    rmv = (int(input("Какую строку хотите удалить? :")))-1 
    s.pop(rmv)
    with open(filename, "w", encoding="UTF-8") as f:
        for i in range(len(s)):
            f.write(f"{s[i][0]} {s[i][1]} {s[i][2]} {s[i][3]} \n")
    return

# ----- Замена элемента в строке
def rewrite(s):
    #show_tell(s)
    rwr = (int(input("Какую строку хотите изменить? :")))-1
    rwr_1 = (int(input("Что хотите изменить? \n0 - Фамилия \n1 - Имя\n2 - Отчество \n3 - Телефон \n")))
    #print("s",s[rwr])
    if  rwr_1 == 0:
        g = input("Введите фамилию :")
        s[rwr][0] = g
    if  rwr_1 == 0:
        g = input("Введите имя :")
        s[rwr][1] = g
    if  rwr_1 == 0:
        g = input("Введите отчество :")
        s[rwr][2] = g 
    if  rwr_1 == 0:
        g = input("Введите телефон :")
        s[rwr][3] = g           
    print("s",s[rwr]) 
    with open(filename, "w", encoding="UTF-8") as f:
        for i in range(len(s)):
            f.write(f"{s[i][0]} {s[i][1]} {s[i][2]} {s[i][3]} \n")
    show_tell(s)
    return

if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input("0 - Добавить случайные данные \n1 - Добавить данные с клавиатуры\n2 - Искать данные \n3 - Посмотреть \n4 - Удалить\n5 - Изменить\n9 - Выход:\n")
        if action == "1":
            s = input_tel(s)
        elif action == "0": 
            s = rnd()
        elif action == "2":
            search_name = input("Ищите! ")
            search_tel(s, search_name)
        elif action == "3":
            show_tell(s)
        elif action == "4": 
            remove(s)  
        elif action == "5": 
            rewrite(s)       
        elif action == "9":
            print("Good bye!")
            break
        else:
            print("Подумай!!!")