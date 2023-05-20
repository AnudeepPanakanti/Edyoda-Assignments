class user : 
 def register():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    # Perform any additional validation or processing if needed

    print("Registration successful!")
    print("Full Name:", full_name)
    print("Phone Number:", phone_number)
    print("Email:", email)
    print("Address:", address)
    print("Password:", password)

 def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Perform login verification
    if email == email and password == password:
        print("Login successful!")
    else:
        print("Login failed. Please check your email and password.")


 def show_menu():
    print("Welcome! Please select an option:")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")

    option = input("Enter the option number: ")

    if option == "1":
        place_new_order()
    elif option == "2":
        show_order_history()
    elif option == "3":
        update_profile()
    else:
        print("Invalid option. Please try again.")




# Order class to store the details of each order
class Order:
    def __init__(self, food_items):
        self.food_items = food_items


# User class to store user details and order history
class user:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_order(self, food_items):
        order = Order(food_items)
        self.order_history.append(order)

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

# Function to display the menu and take user input for food selection
def place_new_order():
    menu = {
        1: "Tandoori Chicken (4 pieces) [INR 240]",
        2: "Vegan Burger (1 Piece) [INR 320]",
        3: "Truffle Cake (500gm) [INR 900]"
    }

    print("Menu:")
    for item in menu.items():
        print(f"{item[0]}. {item[1]}")

    food_items = []
    while True:
        selection = input("Enter the numbers corresponding to the food items you want to order (separated by commas): ")
        try:
            food_items = [int(num.strip()) for num in selection.split(",")]
            break
        except ValueError:
            print("Invalid input. Please enter the numbers corresponding to the food items.")

    selected_items = [menu[item] for item in food_items]
    print("Selected Food Items:")
    for item in selected_items:
        print(item)

    confirm_order = input("Do you want to place the order? (yes/no): ")
    if confirm_order.lower() == "yes":
        user.place_order(selected_items)
        print("Order placed successfully!")
    else:
        print("Order canceled.")

# Function to display the order history of the user
def show_order_history():
    print("Order History:")
    if not user.order_history:
        print("No previous orders found.")
    else:
        for i, order in enumerate(user.order_history):
            print(f"Order {i + 1}:")
            for item in order.food_items:
                print(item)
            print()

# Function to update the user's profile
def update_profile():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    user.update_profile(full_name, phone_number, email, address, password)
    print("Profile updated successfully!")

# Main program
user = user("John Doe", "1234567890", "johndoe@example.com", "123, Main Street", "password")

while True:
    print("\n Welcome to the App")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        place_new_order()
    elif choice == "2":
        show_order_history()
    elif choice == "3":
        update_profile()
    elif choice == "4":
        break

