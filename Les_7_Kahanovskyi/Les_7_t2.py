import sqlite3


def watch():
    sql_w = 'SELECT * FROM students s INNER JOIN marks m ON s.Surname = m.Surname '
    cursor.execute(sql_w)

    for line_w in cursor.fetchall():
        print(line_w)


def add():
    sql_2 = f''' INSERT INTO marks
             VALUES (?, ?, ?, ?, ?, ?, ?)
            '''

    sql_3 = f''' INSERT INTO students
             VALUES (?, ?, ?, ?, ?, ?, ?)
            '''

    marks_list = [
        input(' surname : '), int(input(' math_mark : ')),
        int(input(' geography_mark : ')), int(input('chemistry_mark')),
        int(input(' history_mark : ')), int(input(' physics_mark '))
    ]

    sum_l = [i for i in marks_list if str(i).isdigit()]
    average = sum(sum_l) / len(sum_l)

    value_list = [
        input(' num : '), input(' surname : '),
        input(' name : '), input(' faculty '),
        input('grope'), input('num of stud card'), average]

    cursor.execute(sql_2, marks_list + [average])
    conn.commit()

    cursor.execute(sql_3, value_list)
    conn.commit()


def change(column_to_change, new_info):
    sql_ch_1 = f' UPDATE students SET {column_to_change} = "{new_info}"  WHERE Surname = "{input("Surname ")}"'
    cursor.execute(sql_ch_1)
    conn.commit()


def find(num_sd):

    sql_f = f" SELECT * FROM students WHERE Num_of_student_card = {num_sd} "
    cursor.execute(sql_f)

    print(cursor.fetchall())


def the_best():

    sql_tb = ' SELECT * FROM students WHERE Average = 5 '
    cursor.execute(sql_tb)

    for line in cursor.fetchall():
        print(line)


conn = sqlite3.connect('HW_7_2.db')
cursor = conn.cursor()

while True:

    choice_1 = input('Do you user or admen ? (a/u) ')

    while choice_1.lower() == 'a':

        choice_admen = input(' What do you want to do ? (watch/add/change) ')

        while choice_admen.lower() == 'watch':
            watch()
            break

        while choice_admen.lower() == 'add':
            add()
            break

        while choice_admen.lower() == 'change':
            change(input(" Which column do you want to change ? "), input("Write new info in this column : "))
            watch()
            break
        break

    while choice_1.lower() == 'u':

        choice_user = input(' What do you want to do ? (watch/find/the best) ')

        while choice_user.lower() == 'watch':
            watch()
            break

        while choice_user.lower() == 'find':

            find(int(input(' Enter num of sd please : ')))
            break

        while choice_user.lower() == 'the best':

            the_best()
            break
        break

conn.close()
