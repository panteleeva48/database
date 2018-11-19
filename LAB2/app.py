from flask import Flask, render_template, request 
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="irene",
  password="Vasya123",
  database="schedule"
)
mycursor = mydb.cursor()

def insert(mycursor, mydb, teacher_name, batch_name, class_name, building_address, classroom_num, student_name, date_time, email):
    
    '''
    Вставляем в таблицы, где нет повторов и ссылок.
    '''
    insert_without_dupl = "INSERT INTO %s (%s) SELECT * FROM (SELECT '%s') AS tmp \
                            WHERE NOT EXISTS (SELECT %s FROM %s WHERE %s = '%s')"
    sql = insert_without_dupl % ('BATCHES', 'Name', batch_name, 'Name',
                                 'BATCHES', 'Name', batch_name)
    mycursor.execute(sql)
    sql = insert_without_dupl % ('CLASSES', 'Name', class_name, 'Name',
                                 'CLASSES', 'Name', class_name)
    mycursor.execute(sql)
    sql = insert_without_dupl % ('BUILDINGS', 'Address', building_address,
                                 'Address', 'BUILDINGS', 'Address', building_address)
    mycursor.execute(sql)
    
    '''
    Вставляем в таблицу, где есть повторы и ссылки (имена и номера аудиторий (в двух корпусах есть аудитория 504) могут повторяться).
    '''    
    sql = "INSERT CLASSROOMS (Number, Address) \
            SELECT %s, (SELECT id from BUILDINGS WHERE Address = '%s') \
            WHERE NOT EXISTS \
                (SELECT Number FROM CLASSROOMS WHERE CLASSROOMS.Number = %s \
                    AND CLASSROOMS.Address = (SELECT id from BUILDINGS WHERE Address = '%s'))" % (classroom_num, building_address,
                                                                                                  classroom_num, building_address)
    mycursor.execute(sql)
    
    sql = "INSERT INTO STUDENTS (Name, Batch, Email) \
            SELECT * FROM (SELECT '%s', (SELECT id from BATCHES WHERE Name = '%s'), '%s') AS tmp \
            WHERE NOT EXISTS (SELECT (Email) FROM STUDENTS WHERE Email = '%s')" % (student_name, batch_name,
                                                                                   email, email)
    mycursor.execute(sql)

    sql = "INSERT INTO SCHEDULE (Date_Time, Teacher, Batch, Classroom, Building, Class, Student) \
            VALUES ('%s', '%s', (SELECT id from BATCHES WHERE Name = '%s'), %s, \
                    (SELECT id from BUILDINGS WHERE Address = '%s'), \
                    (SELECT id from CLASSES WHERE Name = '%s'), \
                    (SELECT id from STUDENTS WHERE Email = '%s' \
                    AND Batch = (SELECT id from BATCHES WHERE Name = '%s')))" % (date_time, teacher_name,
                                                                                 batch_name, classroom_num,

                                                                                 building_address, class_name,
                                                                                 email, batch_name)
    mycursor.execute(sql)
    mydb.commit()
    print("Inserted.")


def update_student_class(Nemail, Nclass_name, Ntime, Nteacher, Nclassroom, Nbuilding,
                         email, class_name, time, teacher, classroom, building):
    '''
    Удаляет определённый предмет в расписании
    '''
    sql = "UPDATE SCHEDULE \
            SET \
                Student = (SELECT id FROM STUDENTS WHERE STUDENTS.Email = '%s'), \
                Class = (SELECT id FROM CLASSES WHERE CLASSES.Name = '%s'), \
                Date_time = '%s', \
                Teacher = '%s', \
                Classroom = %s, \
                Building = (SELECT id FROM BUILDINGS WHERE BUILDINGS.Address = '%s') \
            WHERE \
                Student = (SELECT id FROM STUDENTS WHERE STUDENTS.Email = '%s') AND \
                Class = (SELECT id FROM CLASSES WHERE CLASSES.Name = '%s') AND \
                Date_time = '%s' AND \
                Teacher = '%s' AND \
                Classroom = %s AND \
                Building = (SELECT id FROM BUILDINGS WHERE BUILDINGS.Address = '%s')" % (Nemail, Nclass_name,
                                                                                         Ntime, Nteacher, Nclassroom,
                                                                                         Nbuilding, email, class_name,
                                                                                         time, teacher, classroom, building)
    mycursor.execute(sql)
    mydb.commit()

def delete_student_class(email, class_name, time, teacher, classroom, building):
    '''
    Удаляет определённый предмет в расписании
    '''
    sql = "DELETE FROM SCHEDULE WHERE Student = \
            (SELECT id FROM STUDENTS WHERE STUDENTS.Email = '%s') \
            AND Class = (SELECT id FROM CLASSES WHERE CLASSES.Name = '%s') \
            AND Date_time = '%s' AND Teacher = '%s' \
            AND Classroom = %s \
            AND Building = (SELECT id FROM BUILDINGS \
            WHERE BUILDINGS.Address = '%s')" % (email, class_name, time,
                                                teacher, classroom, building)
    mycursor.execute(sql)
    mydb.commit()
    
def schedule_of_student(email, mycursor):
    '''
    На вход: 'impanteleyeva@gmail.com'
    Возвращает: время, преподавателя, номер кабинета, предмет, группу 
    '''
    sql = "SELECT SCHEDULE.Date_Time, SCHEDULE.Teacher, \
                SCHEDULE.Classroom, BUILDINGS.Address, \
                CLASSES.Name, BATCHES.Name FROM SCHEDULE \
            JOIN BUILDINGS ON SCHEDULE.Building = BUILDINGS.id \
            JOIN CLASSES ON SCHEDULE.Class = CLASSES.id \
            JOIN BATCHES ON SCHEDULE.Batch = BATCHES.id \
            JOIN STUDENTS ON SCHEDULE.Student = STUDENTS.id \
            WHERE STUDENTS.Email = '%s'" % (email)
    mycursor.execute(sql)
    student = mycursor.fetchall()
    return student
    
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/see_data')
def seeing1():   
    return render_template('see.html')

@app.route('/see_data_res', methods=['POST'])
def seeing2():
    email=request.form['email']
    try:
        student = schedule_of_student(email, mycursor)
        return render_template('result_see.html', student=student)
    except:
        return render_template('fail.html')
    
@app.route('/delete_data')
def deleting1():   
    return render_template('delete.html')

@app.route('/delete_data_res', methods=['POST'])
def deleting2():
    email=request.form['email']
    class_name=request.form['class_name']
    time=request.form['time']
    teacher=request.form['teacher']
    classroom=int(request.form['classroom'])
    building=request.form['building']
    try:
        delete_student_class(email, class_name, time, teacher, classroom, building)
        return render_template('result.html')
    except:
        return render_template('fail.html')
    
@app.route('/update_data')
def updating1():   
    return render_template('update.html')

@app.route('/update_data_res', methods=['POST'])
def updating2():
    Nemail=request.form['Nemail']
    Nclass_name=request.form['Nclass_name']
    Ntime=request.form['Ntime']
    Nteacher=request.form['Nteacher']
    Nclassroom=int(request.form['Nclassroom'])
    Nbuilding=request.form['Nbuilding']
    email=request.form['email']
    class_name=request.form['class_name']
    time=request.form['time']
    teacher=request.form['teacher']
    classroom=int(request.form['classroom'])
    building=request.form['building']
    try:
        update_student_class(Nemail, Nclass_name, Ntime, Nteacher, Nclassroom, Nbuilding,
                             email, class_name, time, teacher, classroom, building)
        return render_template('result.html')
    except:
        return render_template('fail.html')

@app.route('/add_data')
def adding1():
    return render_template('add.html')

@app.route('/add_data_res', methods=['POST'])
def adding2():
    teacher_name=request.form['teacher_name']
    batch_name=request.form['batch_name']
    class_name=request.form['class_name']
    building_address=request.form['building_address']
    classroom_num=int(request.form['classroom_num'])
    student_name=request.form['student_name']
    date_time=request.form['date_time']
    email=request.form['email']
    try:
        insert(mycursor, mydb, teacher_name, batch_name,
               class_name, building_address, classroom_num,
               student_name, date_time, email)
        return render_template('result.html')
    except:
        return render_template('fail.html')
        

if __name__ == '__main__':
    app.run(debug=True)
