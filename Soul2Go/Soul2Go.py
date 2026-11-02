# Prices for Soul on the GO
TAX_RATE = 0.085
BURGER_PRICE = 6.99
FRIES_PRICE = 2.99
DRINK_PRICE = 1.99

def add_ingredient(ingredient):
    """Adds an ingredient to the Soul Burger."""
    print("Adding " + ingredient + " to your Soul Burger!")


def build_soul_burger():
    """Asks the customer which ingredients they want."""

    ingredients = [
        "pepper jack cheese",
        "candied bacon",
        "caramelized onions",
        "lettuce",
        "tomato",
        "Soul Sauce"
    ]

    chosen_ingredients = []

    print("\nNow let's build your Soul Burger!")

    for ingredient in ingredients:
        answer = input(
            "Would you like " + ingredient + "? (yes/no): "
        )

        if answer.lower() == "yes":
            chosen_ingredients.append(ingredient)

    print("\n----- BUILDING YOUR SOUL BURGER -----")

    for ingredient in chosen_ingredients:
        add_ingredient(ingredient)

    print("Your Soul Burger is ready!")

def calculate_combo_price(has_burger, has_fries, has_drink):
    """Calculates the total price of the Soul on the GO meal."""

    subtotal = 0

    if has_burger:
        subtotal += BURGER_PRICE

    if has_fries:
        subtotal += FRIES_PRICE

    if has_drink:
        subtotal += DRINK_PRICE

    tax = TAX_RATE * subtotal
    total_cost = subtotal + tax

    print("\n----- ORDER TOTAL -----")
    print("Subtotal: $" + str(round(subtotal, 2)))
    print("Tax: $" + str(round(tax, 2)))
    print("Total: $" + str(round(total_cost, 2)))

    return total_cost


def order_decision():
    """Asks the customer if they want to supersize their combo."""

    supersize = input(
        "\nWould you like to make that a BIG SOUL combo? (yes/no): "
    )

    if supersize.lower() == "yes":
        print("YESSS! That's BIG SOUL energy! Large fries and drink it is!")
        return True

    else:
        print("Aww Come On Man Don't Be No Jive Turkey!")
        return False


def order_food(menu, order):
    """Uses recursion to ask the customer about each menu item."""


    if not menu:
        return


    food_item = menu.pop(0)

    answer = input(
        "\nWould you like to order " + food_item + "? (yes/no): "
    )

    if answer.lower() == "yes":
        order.append(food_item)
        print(food_item + " added to your order.")

        if food_item == "a Soul Burger":
            build_soul_burger()

    else:
        print("No " + food_item + "? No problem!")

    order_food(menu, order)

print("======================================")
print("      WELCOME TO SOUL ON THE GO!")
print("   Good Food. Good Mood. Feed Your Soul.")
print("======================================")


menu_items = [
    "a Soul Burger",
    "Soul Fries",
    "a Strawberry Lemonade"
]

customer_order = []

print("\nLet's get your order started!")

order_food(menu_items, customer_order)

order_decision()

has_burger = "a Soul Burger" in customer_order
has_fries = "Soul Fries" in customer_order
has_drink = "a Strawberry Lemonade" in customer_order

print("\n----- PREPARING THE REST OF YOUR ORDER -----")

if has_fries:
    print("Preparing your Soul Fries!")

if has_drink:
    print("Pouring your Strawberry Lemonade!")

calculate_combo_price(has_burger, has_fries, has_drink)

print("\nYour order is complete!")
print("Thanks for stopping at Soul on the GO!")
print("Now go feed your soul!")