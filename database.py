import sqlite3

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    destination TEXT,
    date TEXT,
    time TEXT,
    price INTEGER,
    seats INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    flight_id INTEGER,
    seat_no TEXT,
    booking_date TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM flights")

count = cursor.fetchone()[0]

if count == 0:

    flights = [

        ("Hyderabad","Bengaluru","2026-07-05","09:30",4500,25),
        ("Hyderabad","Delhi","2026-07-06","11:00",6500,30),
        ("Hyderabad","Mumbai","2026-07-07","18:45",5200,18),
        ("Chennai","Hyderabad","2026-07-08","07:30",4000,22),
        ("Bengaluru","Kolkata","2026-07-10","16:20",7200,19)

    ]

    cursor.executemany("""
    INSERT INTO flights
    (source,destination,date,time,price,seats)
    VALUES(?,?,?,?,?,?)
    """, flights)

conn.commit()

print("Database Ready")