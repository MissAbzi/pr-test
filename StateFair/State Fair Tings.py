# Guinevere Baptiste
# October 11th, 2026
# Minnesota State Fair Python Adventure

print("=" * 48)
print("WELCOME TO THE MINNESOTA STATE FAIR!")
print("Your Two-Day Python Adventure Begins!")
print("=" * 48)

name = input("\nWhat's your name, fair adventurer? ").strip()

if not name:
    name = "Fair Adventurer"

print("\nWelcome, " + name + "!")
print("Let's explore the Great Minnesota Get-Together!")

# FOOD STANDS
food_stands = {
    "Pronto Pups": "Footlong Corn Dogs",
    "Big Fat Bacon": "Bacon-on-a-Stick",
    "Fresh French Fries": "French Fries",
    "Sweet Martha's": "Fresh Chocolate Chip Cookies",
    "Fried Oreo Stand": "Deep-Fried Oreos",
    "Alligator Stand": "Fried Alligator-on-a-Stick",
    "The Cheese Curd Tacos": "Cheese Curd Tacos",
    "Cheese Curds Stand": "Deep-Fried Cheese Curds"
}

# LIST OF ATTRACTIONS

attractions = [
    ("Giant Slide", "Near the Grandstand"),
    ("Skyride", "Above the Fairgrounds"),
    ("Haunted House", "Near the Midway"),
    ("Bungee Cord Ride", "Adventure Area"),
    ("Ferris Wheel", "Midway"),
    ("Butter Sculpture", "Dairy Building"),
    ("Potato Sack Slides", "Giant Slide Area"),
    ("Space Tower", "Fairgrounds")
]

# UNIQUE ACTIVITIES

activities = {
    "Riding the Giant Slide",
    "Watching the Parade",
    "Eating Sweet Martha's Cookies",
    "Trying Fried Oreos",
    "Riding the Ferris Wheel",
    "Visiting the Butter Sculpture",
    "Trying Fried Alligator",
    "Exploring the Midway",
    "Watching Live Music",
    "Taking Photos",
    "Shopping at Fair Vendors",
    "Riding the Skyride"
}


# INTERACTIVE MENU

while True:

    print("\n" + "=" * 48)
    print("MINNESOTA STATE FAIR MAIN MENU")
    print("=" * 48)

    print("1. Explore Food Stands")
    print("2. Explore Attractions")
    print("3. Plan Your Activities")
    print("4. View Two-Day Fair Planner")
    print("5. Add Your Own Fair Experience")
    print("6. Exit the Fair")

    choice = input("\nChoose an option (1-6): ").strip()

 # OPTION 1: FOOD STANDS

    if choice == "1":

        print("\nWELCOME TO THE FOOD STANDS!")

        input("\nPress Enter to see what's cooking...")

        for stand, food in food_stands.items():
            print("- " + stand + ": " + food)

        answer = input(
            "\nWould you like to try a food? (yes/no): "
        ).lower().strip()

        if answer == "yes":

            stand_names = list(food_stands.keys())

            for i, stand in enumerate(stand_names, 1):
                print(str(i) + ". " + stand)

            selection = input("\nEnter the food stand number: ")

            if selection.isdigit():
                number = int(selection)

                if 1 <= number <= len(stand_names):
                    stand = stand_names[number - 1]
                    food = food_stands[stand]

                    print("\nDelicious choice!")
                    print("You're enjoying " + food + "!")

                    activities.add("Eating " + food)

                else:
                    print("That stand doesn't exist!")

            else:
                print("Please enter a valid number.")

# OPTION 2: ATTRACTIONS

    elif choice == "2":

        print("\nWELCOME TO THE FAIR ATTRACTIONS!")

        input("\nPress Enter to see the attractions...")

        for i, attraction in enumerate(attractions, 1):
            print(
                str(i) + ". " + attraction[0] +
                " - " + attraction[1]
            )

        answer = input(
            "\nWould you like to visit an attraction? (yes/no): "
        ).lower().strip()

        if answer == "yes":

            selection = input("\nEnter attraction number: ")

            if selection.isdigit():
                number = int(selection)

                if 1 <= number <= len(attractions):
                    attraction = attractions[number - 1]

                    print("\nGreat choice, " + name + "!")
                    print("You're visiting " + attraction[0] + "!")
                    print("Location: " + attraction[1])

                    activities.add("Visiting " + attraction[0])

                else:
                    print("That attraction doesn't exist!")

            else:
                print("Please enter a valid number.")

# OPTION 3: ACTIVITIES

    elif choice == "3":

        print("\nYOUR FAIR ACTIVITIES!")

        input("\nPress Enter to view your activities...")

        for activity in sorted(activities):
            print("- " + activity)

        print("\nYou currently have " +
              str(len(activities)) + " unique activities!")

        answer = input(
            "\nWould you like to add an activity? (yes/no): "
        ).lower().strip()

        if answer == "yes":

            new_activity = input(
                "\nEnter your new activity: "
            ).strip()

            if new_activity:
                if new_activity in activities:
                    print("\nThat activity already exists!")
                    print("Sets do not allow duplicates.")

                else:
                    activities.add(new_activity)
                    print("\nActivity successfully added!")

            else:
                print("No activity was entered.")

        answer = input(
            "\nWould you like to remove an activity? (yes/no): "
        ).lower().strip()

        if answer == "yes":

            activity_list = sorted(activities)

            for i, activity in enumerate(activity_list, 1):
                print(str(i) + ". " + activity)

            selection = input("\nEnter activity number to remove: ")

            if selection.isdigit():
                number = int(selection)

                if 1 <= number <= len(activity_list):
                    removed = activity_list[number - 1]
                    activities.remove(removed)

                    print("\nRemoved: " + removed)

                else:
                    print("Invalid activity number.")

            else:
                print("Please enter a valid number.")

# OPTION 4: TWO-DAY FAIR PLANNER

    elif choice == "4":

        print("\nLET'S PLAN YOUR TWO DAYS AT THE FAIR!")

        activity_choices = sorted(activities)

        if activity_choices:
            selected_activity = activity_choices[0]
        else:
            selected_activity = "Explore the Fairgrounds"

        daily_planner = {

            "Day 1": {

                "Morning": [
                    ("Breakfast", food_stands["Sweet Martha's"]),
                    ("Ride", attractions[0][0]),
                    ("Activity", "Visit the Animal Barns")
                ],

                "Afternoon": [
                    ("Lunch", food_stands["Pronto Pups"]),
                    ("Ride", attractions[4][0]),
                    ("Activity", selected_activity)
                ],

                "Evening": [
                    ("Dinner", food_stands["The Cheese Curd Tacos"]),
                    ("Ride", attractions[1][0]),
                    ("Entertainment", "Watch Live Music")
                ]
            },

            "Day 2": {

                "Morning": [
                    ("Breakfast", food_stands["Fried Oreo Stand"]),
                    ("Attraction", attractions[5][0]),
                    ("Activity", "Take Fair Photos")
                ],

                "Afternoon": [
                    ("Lunch", food_stands["Alligator Stand"]),
                    ("Ride", attractions[3][0]),
                    ("Activity", "Explore the Midway")
                ],

                "Evening": [
                    ("Dinner", food_stands["Cheese Curds Stand"]),
                    ("Ride", attractions[2][0]),
                    ("Final Ride", attractions[6][0])
                ]
            }
        }

        day = input(
            "\nWhich day would you like to view? (1, 2, or both): "
        ).lower().strip()

        if day == "1":
            selected_days = ["Day 1"]

        elif day == "2":
            selected_days = ["Day 2"]

        elif day == "both":
            selected_days = ["Day 1", "Day 2"]

        else:
            selected_days = []
            print("\nInvalid choice. Please choose 1, 2, or both.")

        for selected_day in selected_days:

            print("\n" + "=" * 40)
            print(selected_day.upper() + " FAIR ADVENTURE")
            print("=" * 40)

            for time, plans in daily_planner[selected_day].items():

                input(
                    "\nPress Enter to explore your " +
                    time.lower() + " plans..."
                )

                print("\n" + time.upper() + ":")

                for plan in plans:
                    print("- " + plan[0] + ": " + plan[1])

        if selected_days:
            print("\nYour fair itinerary is ready!")

# OPTION 5: CUSTOM EXPERIENCE

    elif choice == "5":

        print("\nCREATE YOUR OWN FAIR EXPERIENCE!")

        print("1. Add a Food Stand")
        print("2. Add an Attraction")
        print("3. Add an Activity")

        custom = input("\nChoose an option (1-3): ").strip()

        if custom == "1":

            stand = input("Enter food stand name: ").strip()
            food = input("Enter the food served: ").strip()

            if stand and food:
                food_stands[stand] = food
                print("\nFood stand added successfully!")
            else:
                print("Both fields are required.")

        elif custom == "2":

            attraction_name = input(
                "Enter attraction name: "
            ).strip()

            location = input(
                "Enter attraction location: "
            ).strip()

            if attraction_name and location:

                new_attraction = (attraction_name, location)

                if new_attraction not in attractions:
                    attractions.append(new_attraction)
                    print("\nAttraction added successfully!")
                else:
                    print("\nThat attraction already exists!")

            else:
                print("Both fields are required.")

        elif custom == "3":

            new_activity = input(
                "Enter your activity: "
            ).strip()

            if new_activity:
                if new_activity in activities:
                    print("\nActivity already exists!")
                else:
                    activities.add(new_activity)
                    print("\nActivity added successfully!")
            else:
                print("No activity was entered.")

        else:
            print("\nInvalid selection.")

# OPTION 6: EXIT

    elif choice == "6":

        print("\n" + "=" * 48)
        print("THANK YOU FOR VISITING THE STATE FAIR!")
        print("=" * 48)

        print("\nHere's your adventure summary, " + name + "!")

        print("Food stands available: " + str(len(food_stands)))
        print("Attractions available: " + str(len(attractions)))
        print("Unique activities: " + str(len(activities)))

        print("\nThanks for visiting the Great Minnesota Get-Together!")
        print("See you next year!")

        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")