import sqlite3
from datetime import datetime

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()


def book_ticket():

    user_id = int(input("Enter User ID: "))
    flight_id = int(input("Enter Flight ID: "))
    seat_no = input("Enter Seat Number: ")

    cursor.execute("SELECT seats FROM flights WHERE id=?", (flight_id,))
    flight = cursor.fetchone()

    if flight is None:
        print("❌ Flight not found.")
        return

    seats = flight[0]

    if seats <= 0:
        print("❌ No seats available.")
        return

    booking_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO bookings(user_id, flight_id, seat_no, booking_date)
        VALUES (?, ?, ?, ?)
    """, (user_id, flight_id, seat_no, booking_date))
    
    cursor.execute("""
        UPDATE flights
        SET seats = seats - 1
        WHERE id = ?
    """, (flight_id,))

    conn.commit()

    print("\n✅ Ticket Booked Successfully!")


book_ticket()