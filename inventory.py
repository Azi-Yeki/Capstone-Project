# We create a class called Shoe


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return ("\nCountry: " + self.country + " \n Shoe Code: " + str(self.code) + " \n Shoe Name: " + self.product + "\n Shoe Cost: " + str(self.cost) + "\nQuantity: " + str(self.quantity) + "\n")

shoe_list = []

def read_shoes_data():
    try:

        with open('inventory.txt', 'r') as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()

        for line in range(1, len(shoe_list_inside_file)):
            country, code, product, cost, quantity = shoe_list_inside_file[line].strip('\n').split(',')
            shoes = Shoe(country, code, product, float(cost), int(quantity))
            shoe_list.append(shoes)

    except FileNotFoundError:

         print('inventory file not found. Please check file name correctly')

read_shoes_data()

def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    shoes_captured = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    shoe_list.append(shoes_captured)


def update():
    # Create a variable called obj_data.
    # This will take my intake my shoe objects.

    obj_data = f'Country,Code,Product,Cost,Quantity'

    # Create a for loop for the to iterate over the shoe list.

    for shoe in shoe_list:
        obj_data += '\n' + shoe.file_updated()

    # We then open our file and write to it.

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)

def view_all():
    print(*shoe_list)

def re_stock():
    qty = shoe_list[0].quantity
    shoe_index = 0
    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
            qty = s.quantity
            shoe_index = i

    return shoe_index

def search_shoe(code):
    for shoe_code in shoe_list:
        if shoe_code.code == code:
            return shoe_code

    return ("The shoe code " + str(code) + " is not found \n" )

def value_per_item():
    for s in shoe_list:
        value = s.cost * s.quantity
        print(str(s) + " Value: " + str(value) + "\n")

def highest_qty():
    shoe_index = 0
    max_quantity = shoe_list[shoe_index].get_quantity()
    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_index = s
    print("This shoe is on sale " + str(shoe_list[shoe_index]) + "\n")

user_choice = ''' '''

while user_choice != "end stock taking":
    user_choice = input("Please view below and select \n c = Capture shoe data \n vw = view all shoes \n r = shoes to restock \n f - find shoe \n va = total value per shoe \n s = on sale \n Enter choice: ").lower()

    if user_choice.lower() == 'c':
        shoe_country = input("Please enter the country of the shoes: ")
        shoe_code = input("Please enter the shoe code: ")
        shoe_name = input("Please enter product name: ")
        shoe_cost = float(input("Please enter the cost of the shoe: "))
        shoe_quantity = int(input("Please enter the quantity of the shoes: "))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)

    elif user_choice.lower() == 'vw':
        view_all()

    elif user_choice.lower() == 'r':
        shoe_index = re_stock()
        print("The shoe with the lowest quantity: " + str(shoe_list[shoe_index]))
        restock_choice = input("Restock? \n Y = yes \n N = no: \n")

        if restock_choice.lower() == 'y':
            shoe_list[shoe_index].quantity = int(input("Quantity: \n"))

        if restock_choice.lower() == 'n':
            print("No restock \n")

        update()
        re_stock()

    elif user_choice.lower() == 'f':
        s_code = input('Please enter the shoe code you looking for: ')
        print(f'{search_shoe(s_code)}')

    elif user_choice.lower() == 'va':
        value_per_item()

    elif user_choice.lower() == 's':
        highest_qty()

    elif user_choice.lower() == 'e':
        print('Thank you')

    else:
        print("Invalid choice. Please try again.")