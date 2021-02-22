import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteka"
)

mycursor = mydb.cursor()
rows = [
    ('Jane', 'Janich', 'jane_janich@mail.com',
     '062111111', 1, 'janejanich', 'jane123'),
    ('Joe', 'Joeich', 'joe_joich@mail.com', '062222222', 1, 'joejoich', 'joe132'),
    ('Samantha', 'Pajser', 'samanta.p@mail.com',
     '062333333', 1, 'samantap', 'malacrnagarava'),
    ('Mujo', 'Palic', 'mujo.p@mail.com', '062444444', 1, 'mujop', 'mujomujomujo'),
    ('Alija', 'Derzelez', 'aljo.dj@mail.com',
     '062555555', 1, 'aljodj', 'didzejaljo'),


]
sql = "INSERT INTO radnici (radnik_name, radnik_surname, radnik_email, radnik_phonenumber, radnik_permission, radnik_username, radnik_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
mycursor.executemany(sql, rows)
mydb.commit()
