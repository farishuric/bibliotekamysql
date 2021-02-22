import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteka"
)

administrator = 1
radnik = 2

mycursor = mydb.cursor()

username = input("Enter your username: ")
password = input("Enter password: ")

myError = "Invalid username or password!"
sql = "SELECT * FROM radnici WHERE radnik_username = %s AND radnik_password = %s"
val = (username, password)

mycursor.execute(sql, val)
account = mycursor.fetchone()

hellousername = account[1]
hellousersurname = account[2]
permission = account[5]
print(
    f"Welcome back {hellousername} {hellousersurname}. What do you want to do?")
print("")
print("1) Knjige\n2) Autori\n3) Kartice\n4) Klijenti")
print("")

user_module = int(input("Enter module number: "))

sql = "SELECT * FROM radnici WHERE radnik_username = %s AND radnik_password = %s"
val = (username, password)

if user_module == 1 and permission == administrator:
    print("1)Dodaj novu knjigu u sistem\n2)Izmijeni postojeću knjigu iz sistema\n3)Obriši knjigu iz sistema")
    user_book_module = int(input("Enter module number: "))
    if user_book_module == 1:
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        book_quantity = int(input("Enter books quantity: "))
        sql = "INSERT INTO knjige (knjiga_name, knjiga_author, knjiga_stanje) VALUES (%s, %s, %d)"
        values = (book_name, book_author, book_quantity)
        mycursor.execute(sql, values)
    elif user_book_module == 2:

elif user_module == 1 and permission == radnik:
    print("1)Dodaj novu knjigu u sistem\n2)Izmijeni postojeću knjigu iz sistema")
    user_book_module = int(input("Enter module number: "))
    if user_book_module == 1:
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        book_quantity = int(input("Enter books quantity: "))
        sql = "INSERT INTO knjige (knjiga_name, knjiga_stanje, knjiga_author) VALUES (%s, %s, %s)"
        values = (book_name, book_quantity, book_author)
        mycursor.execute(sql, values)
        mydb.commit()
else:
    print(myError)
