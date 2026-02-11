
while True:
    print("\n🎬 Welcome to Movie Ticket Booking")
    print("1. Avengers  (₹200)")
    print("2. Pushpa    (₹150)")
    print("3. Jawan     (₹180)")
    print("4. Exit")

    choice = int(input("Select movie (1-4): "))

    if choice == 4:
        print("Thank you! Visit Again 😊")
        break

    # Movie Selection
    if choice == 1:
        price = 200
        movie = "Avengers"
    elif choice == 2:
        price = 150
        movie = "Pushpa"
    elif choice == 3:
        price = 180
        movie = "Jawan"
    else:
        print("Invalid choice! Try again.")
        continue

    tickets = int(input("Enter number of tickets: "))
    total = price * tickets

    print("\n🎟 Select Your Seats")

    count = 1
    while count <= tickets:
        seat = input(f"Enter seat number for ticket {count} (Example A1, B2): ")
        print("Seat", seat, "booked ✅")
        count += 1

    print("\n🎉 Booking Confirmed!")
    print("Movie:", movie)
    print("Tickets:", tickets)
    print("Total Amount: ₹", total)

    again = input("\nDo you want to book again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for booking! 🍿")
        break

movie_1="border"
movie_2 = "dhurandar"
movie_3 = "Pushpa 2"

choose_movie= input(f"movie available are: \n1.{movie_1} \n 2.{movie_2} \n 3.{movie_3}")
price = 0
if choose_movie == 1:
    price ="200 rs"
    print(f"The price of movie ticket is{price}")
    
elif choose_movie==2:
    price = "230 rs"
    print(f"The price of movie ticket is {price}")

else:
  price = "100 rs"
  print(f"the price of movie ticket is {price}")  

