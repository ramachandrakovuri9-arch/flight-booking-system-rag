from chatbot import run_chatbot
from flights import show_flights
from bookings import book_ticket
from view_bookings import view_bookings
from cancel_booking import cancel_booking

while True:
    print("\n========== FLIGHT BOOKING SYSTEM ==========")
    print("1. Register")
    print("2. Login")
    print("3. View Flights")
    print("4. Book Ticket")
    print("5. View My Bookings")
    print("6. Cancel Booking")
    print("7. AI Flight&policy assistant")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        show_flights()

    elif choice == "4":
        book_ticket()

    elif choice == "5":
        view_bookings()

    elif choice == "6":
        cancel_booking()

    elif choice == "7":
        run_chatbot()
    elif choice == "8":
        break
    else:
        print("Invalid Choice!")