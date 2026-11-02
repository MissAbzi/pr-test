# Guinevere Baptiste
# 10/18/2026

# Customer Greeting
print("Bienvenidos to Catrina's Mexicana Grill Where You Build Your Taacccooooo!")

tortilla_types = ["Masa", "Flour", "Whole Wheat"]
filling_types = ["Carne", "Pollo", "Pescado", "Frijoles"]
toppings = ["Queso", "Lechuga", "Tomates", "Onions", "Salsa", "Sour Crema"]

def display_options(options):
    for index, item in enumerate(options,start=1):
        print(f"{index}. {item}")

#Get and Validate Customer Choices
def get_choice(options):
    while True:
        choice = input("Enter the number of your Choice!").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]
        print("Invalid Option, Please Choose a Valid Menu Number")


display_options(tortilla_types)
selected_tortilla = get_choice(tortilla_types)

print("You selected:", selected_tortilla)

display_options(filling_types)
selected_filling = get_choice(filling_types)
print("You selected:", selected_filling)

selected_toppings = []
while True:
        print("\n Choose Your Toppings")
        display_options(toppings)
        selected_topping = get_choice(toppings)
        selected_toppings.append(selected_topping)
        print("You Added:", selected_topping)
        another = input("Would you like another topping? (yes/no): ").strip().lower()
        if another == "no":
            break

# Display the completed order
print("\n===== YOUR TAACCCOOOOO ORDER =====")
print("Tortilla:", selected_tortilla)
print("Filling:", selected_filling)
print("Toppings:")

# Print each selected topping
for topping in selected_toppings:
    print("-", topping)


# Special message for customers who select salsa
if "Salsa" in selected_toppings:
    print("One sazon salsa taco coming up!")


# Thank the customer
print("\nMuchas Gracias for ordering from Catrina's Mexicana Grill!")