# Author: Guinevere Baptiste
# Date: October 4, 2026


# ============================================================
# TAE'S ANIMAL RESCUE
# Every Animal Deserves a Forever Home
# ============================================================


# Create an empty list to store animal names
animals = []

# Maximum number of animals the rescue can hold
CAPACITY = 5


# ------------------------------------------------------------
# GET ANIMAL COUNT
# ------------------------------------------------------------

def get_animal_count():
    """Returns the total number of animals currently in the rescue."""

    return len(animals)


# ------------------------------------------------------------
# ADD ANIMAL
# ------------------------------------------------------------

def add_animal(name, species):
    """Adds a new animal if there is room in the rescue."""

    # Check the animal count before adding another animal
    if get_animal_count() < CAPACITY:
        animals.append(name)
        print(name + " the " + species + " has been added to the rescue.")
        return True

    else:
        print("Sorry! Tae's Animal Rescue is a full house!")
        return False


# ------------------------------------------------------------
# ADOPT ANIMAL
# ------------------------------------------------------------

def adopt_animal(name):
    """Removes an animal from the rescue when adopted."""

    if name in animals:
        animals.remove(name)
        print(name + " found their forever home!")
        return True

    else:
        print(name + " is not currently at Tae's Animal Rescue.")
        return False


# ------------------------------------------------------------
# WELCOME
# ------------------------------------------------------------

print("======================================")
print("       TAE'S ANIMAL RESCUE")
print(" Every Animal Deserves a Forever Home")
print("======================================")

print("\nLet's check in our animals.")


# ------------------------------------------------------------
# ADD ANIMALS UNTIL THE RESCUE REACHES CAPACITY
# ------------------------------------------------------------

while get_animal_count() < CAPACITY:

    name = input("\nWhat is the animal's name? ")
    species = input("What kind of animal is " + name + "? ")

    add_animal(name, species)

    # Display how much room remains
    spaces_left = CAPACITY - get_animal_count()

    if spaces_left > 0:
        print("We have room for "
              + str(spaces_left)
              + " more animal(s).")


# ------------------------------------------------------------
# DISPLAY THE FULL SHELTER
# ------------------------------------------------------------

print("\nThere are currently "
      + str(get_animal_count())
      + " animals at Tae's Animal Rescue.")

print("\nAnimals currently in the rescue:")

for animal in animals:
    print("- " + animal)


# ------------------------------------------------------------
# CHECK FOR AN ADOPTION
# ------------------------------------------------------------

adoption = input(
    "\nHas one of our animals found a forever home? (yes/no): "
)

# .strip() removes accidental spaces before or after the answer
if adoption.strip().lower() == "yes":

    adopted_name = input(
        "Which animal was adopted? "
    )

    if adopt_animal(adopted_name):

        print("\nWe now have capacity for another animal!")

        # Ask about a new animal now that a space is available
        new_animal = input(
            "Would you like to add another animal? (yes/no): "
        )

        if new_animal.strip().lower() == "yes":

            name = input("\nWhat is the animal's name? ")
            species = input("What kind of animal is " + name + "? ")

            add_animal(name, species)

else:
    print("\nWE'RE A FULL HOUSE!")


# ------------------------------------------------------------
# DISPLAY FINAL ANIMAL COUNT
# ------------------------------------------------------------

print("\nThere are currently "
      + str(get_animal_count())
      + " animals at Tae's Animal Rescue.")

print("\nAnimals currently in the rescue:")

for animal in animals:
    print("- " + animal)


# ------------------------------------------------------------
# GOODBYE
# ------------------------------------------------------------

print("\nThank you for helping the animals at Tae's Animal Rescue!")