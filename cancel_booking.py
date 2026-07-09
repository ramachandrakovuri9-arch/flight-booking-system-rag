import sqlite3

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()


def cancel_booking():

    booking_id = int(input("Enter Booking ID : "))

    # Find the flight id
    cursor.execute(
        "SELECT flight_id FROM bookings WHERE id=?",
        (booking_id,)
    )

    booking = cursor.fetchone()

    if booking is None:
        print("Booking Not Found")
        return

    flight_id = booking[0]

    # Delete booking
    cursor.execute(
        "DELETE FROM bookings WHERE id=?",
        (booking_id,)
    )

    # Increase seats
    cursor.execute(
        """
        UPDATE flights
        SET seats = seats + 1
        WHERE id=?
        """,
        (flight_id,)
    )

    conn.commit()

    print("Booking Cancelled Successfully")


if __name__ == "__main__":
    cancel_booking()