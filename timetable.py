# Login details (you can change these)
saved_username = "admin"
saved_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == saved_username and password == saved_password:

    print("\n✅ Login successful!")

    day = input("\nEnter the day: ").lower()
    time = input("Enter time (morning / afternoon / evening / night): ").lower()

    print("\n📅 Your Schedule:")

    if day == "sunday":
        if time == "morning":
            print("Sunday Morning:")
            print("• Wake up comfortably")
            print("• Light stretching")
            print("• Enjoy breakfast with family")

        elif time == "afternoon":
            print("Sunday Afternoon:")
            print("• Have lunch")
            print("• Watch TV or web series")
            print("• Short rest")

        elif time == "evening":
            print("Sunday Evening:")
            print("• Meet friends")
            print("• Evening snacks")

        elif time == "night":
            print("Sunday Night:")
            print("• Dinner time")
            print("• Relax music")
            print("• Sleep early")

        else:
            print("Invalid time entered.")

    elif day == "monday":
        if time == "morning":
            print("Monday Morning:")
            print("• Wake up early")
            print("• Morning workout")
            print("• Get ready for college")

        elif time == "afternoon":
            print("Monday Afternoon:")
            print("• Attend lectures")
            print("• Lunch break")

        elif time == "evening":
            print("Monday Evening:")
            print("• Study session")
            print("• Tea break")

        elif time == "night":
            print("Monday Night:")
            print("• Revise topics")
            print("• Dinner")
            print("• Go to sleep")

        else:
            print("Invalid time entered.")

    # (rest of your code stays exactly the same...)

else:
    print("\n❌ Invalid username or password!")
    
#hi
