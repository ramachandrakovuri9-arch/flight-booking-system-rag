import sqlite3

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()


def view_bookings():

    user_id = int(input("Enter User ID : "))

    cursor.execute("""

    SELECT
        bookings.id,
        flights.source,
        flights.destination,
        flights.date,
        flights.time,
        bookings.seat_no,
        flights.price

    FROM bookings

    JOIN flights

    ON bookings.flight_id = flights.id

    WHERE bookings.user_id = ?

    """, (user_id,))

    bookings = cursor.fetchall()

    if len(bookings) == 0:
        print("No Bookings Found")
        return

    print("\n========== MY BOOKINGS ==========\n")

    for booking in bookings:

        print("Booking ID :", booking[0])
        print("Source     :", booking[1])
        print("Destination:", booking[2])
        print("Date       :", booking[3])
        print("Time       :", booking[4])
        print("Seat No    :", booking[5])
        print("Price      :", booking[6])

        print("-"*40)


if __name__ == "__main__":
    view_bookings()