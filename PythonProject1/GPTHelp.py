# Ask the customer for their name and set the prices for each meal option.
customer_name = input("Please enter your name: ")
sandwich_price = 8
platter_price = 12

# Ask the customer which type of meal they would like.
meal_choice = input("Do you want a sandwich meal or a platter meal? (sandwich/platter): ")

# Determine the meal price based on the customer's choice.
# .lower() allows the program to recognize the answer regardless of capitalization.
if meal_choice.lower() == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else:
    # If the input is invalid, the program defaults to a sandwich meal.
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price

# Calculate the initial cost based on the number of meals ordered.
num_meals = int(input("How many meals do you want? "))
total_cost = meal_price * num_meals

# Add $0.50 per meal if the customer requests extra sauce.
extra_sauce = input("Do you want extra sauce? (yes/no): ")

if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals

# Store the original price separately so the receipt can show
# the cost before the extra sauce charge.
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"

# Display the completed order summary.
print("\nOrder Summary:")
print("Customer Name: " + customer_name)
print("Meal Type: " + meal_choice + " meal")
print("Number of Meals: " + str(num_meals))

# This uses a conditional expression, so the if/else stays on one line
# instead of using the indentation required by a normal if/else statement.
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))

# .format() displays the prices with exactly two decimal places.
print("Original Total: $" + "{:.2f}".format(original_total))
print("Final Total: $" + "{:.2f}".format(total_cost))