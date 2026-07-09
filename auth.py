import sqlite3

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()


def register():

    print("\n----- Register -----")

    name = input("Enter Name : ")
    email = input("Enter Email : ")
    password = input("Enter Password : ")

    try:
        cursor.execute(
            "INSERT INTO users(name,email,password) VALUES(?,?,?)",
            (name, email, password)
        )

        conn.commit()

        print("\nRegistration Successful!")

    except:
        print("\nEmail already exists.")


def login():

    print("\n----- Login -----")

    email = input("Enter Email : ")
    password = input("Enter Password : ")

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        print("\nLogin Successful!")
        print("Welcome", user[1])
    else:
        print("\nInvalid Email or Password")

