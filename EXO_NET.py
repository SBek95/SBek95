import socket
import sqlite3

#Попытка подключения и создание базы данных для сохранения входящих сообщений.
try:
    conn = sqlite3.connect('EXO.sqlite')
    cursor = conn.cursor()
    print("Успешно открыта база данных")
except sqlite3.Error as err:
    print('Ошибка : ' + err.args[0])
finally:
    conn.close()
    print("Закрыта база данных")

# ФУНКЦИЯ ТАБЛИЫ БАЗЫ ДАННЫХ - "КОМАНДЫ"
def f1():
     conn = sqlite3.connect('EXO.sqlite')
     cursor = conn.cursor()

     cursor.execute('''  CREATE TABLE EXO_DATA(
                    COMAND           TEXT    NOT NULL);''')
     cursor.close()

# СОХРАНЕНИЕ БАЗЫ ДАННЫХ
def f2():
     conn = sqlite3.connect('EXO.sqlite')
     cursor = conn.cursor()

     comand = "'" + soc + "'"
     q = "INSERT INTO EXO_DATA (COMAND) VALUES (" + comand +")"
     print(q)
     cursor.execute(q)
     conn.commit()
     conn.close()

# ПОДКЛЮЧЕНИЕ К СЕРВЕРУ
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
conn, addr = sock.accept()
print('connected:', addr)
messege = input("Введите команду- ")
conn.send(messege.encode())
# РЕШЕНИЕ СОЗДАНИЯ БАЗЫ ДАННЫХ!!
Base = input("Создать базу данных для сохранения входящих сообщений?- Y или N")
if Base == 'Y':
    f1()
    print("База данных создана")
else:
    print("Вы отклонили создание базы, т.к. она у вас уже есть!!")
# функция приема и сохранения сообщений
while True:
   sock = conn.recv(102300)
   soc = sock.decode()
   print(soc)

   if soc == 'Костюм отключается от сервера':
      f2()
      print("Данные сохранены в базу!")
      break
conn.close()