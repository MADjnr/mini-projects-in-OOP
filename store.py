class Store:

    def __init__(self, name, address, num_employees):
        self.name = name
        self.address = address
        self.num_employees = num_employees

    def greet_customers(self):
        print("Welcome to our store! What would you like to buy?")


class DonutStore(Store):

    def __init__(self, name, address, num_employees):
        Store.__init__(self, name, address, num_employees)

    def greet_customers(self):
        print("welcome to our store what donut would you like to eat")



my_donut_store = DonutStore('round donut', 'Onuiyi', 24)

print(my_donut_store.name)
print(my_donut_store.address)

