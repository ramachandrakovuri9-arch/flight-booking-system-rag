import sqlite3

conn = sqlite3.connect("database/flights.db")
cursor = conn.cursor()


def show_flights():

    cursor.execute("SELECT * FROM flights")

    flights = cursor.fetchall()

    print("\n================ AVAILABLE FLIGHTS ================\n")

    if len(flights) == 0:
        print("No Flights Available")
        return

    for flight in flights:

        print(f"Flight ID        : {flight[0]}")
        print(f"Source           : {flight[1]}")
        print(f"Destination      : {flight[2]}")
        print(f"Date             : {flight[3]}")
        print(f"Time             : {flight[4]}")
        print(f"Price            : ₹{flight[5]}")
        print(f"Available Seats  : {flight[6]}")
        print("-" * 45)


if __name__ =="__main__":
    show_flights()