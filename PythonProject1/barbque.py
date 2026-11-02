# Author: [Guinevere Baptiste]
# Date: [09/13/2026]

customer_name = input("Please enter your name:")
sandwich_price = 8
platter_price = 12
# .lower() allows the program to recognize the answer regardless of capitalization.
meal_choice = input("Do you want a sandwich meal or a platter meal? (sandwich/platter): ")
if meal_choice.lower() == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
 # If the input is invalid, the program defaults to a sandwich meal.
else:
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price
num_meals = int(input("How many meals do you want?"))
total_cost = meal_price * num_meals
# Add $0.50 per meal if the customer requests extra sauce.
extra_sauce = input("Do you want extra sauce? (yes/no):")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"

print("\nOrder Summary:")
print("Customer Name: " + customer_name)
print("Meal Type: " + meal_choice + " meal")
print("Number of Meals: " + str(num_meals))
# This uses a conditional expression, so the if/else stays on one line
# instead of using the indentation required by a normal if/else statement
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))
# .format() displays the prices with exactly two decimal places.
print("Original Total: $" + "{: .2f}" .format(original_total))
print("Final Total: $" + "{: .2f}".format(total_cost))
