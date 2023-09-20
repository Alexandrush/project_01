# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:

import sqlite3
con = sqlite3.connect("teatchers.db")
cursor = con.cursor()

with con:
    con.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        Student_Id INTEGER,
        Student_Name Text,
        School_Id INTEGER Primary Key
);
    """)

sqlquery = "REPLACE INTO Students (Student_Id, Student_Name, School_Id) values(?, ?, ?)"
values = [
    (201, "Иван", 1),
    (202, "Петр", 2),
    (203, "Анастасия", 3),
    (204, "Игорь", 4)]

with con:
    con.executemany(sqlquery, values)

with con:
    values = con.execute("SELECT * FROM Students")
    for row in values:
        print(row)

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school(Student_Id):
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM Students WHERE Student_Id = ?'
    cursor.execute(sqlquery, (Student_Id,))
    school_info = cursor.fetchall()
    # print("Данные по школе")
    for row in school_info:
      print("ID школы:", row[2])

def get_student(student_id):
    con = get_connection()
    cursor = con.cursor()
    sqlquery1 = 'SELECT * FROM Students WHERE Student_Id = ?'
    cursor.execute(sqlquery1, (student_id,))
    student_info = cursor.fetchall()
    # print ("Данные по школе")
    for row in student_info:
      print("ID студента:", row[0])
      print ("Имя студента:", row[1])
    close_connection(con)

y = int(input('Введи ID студента:'))
get_school(y)
get_student(y)
