import json
class admin :
    def __init__(self):
        self.food={}
        self.food_id=len(self.food)+1
    
    def add_food_items(self):
        self.name = input("Enter the name of the food item : ")
        self.quantity = input("Enter the quantity : ")
        self.price = int(input("Enter the price of the item : "))
        self.stock = int(input("Enter the stock : "))
        self.discount = int(input("Enter the amount of discount : "))
        self.item = {"name" : self.name,"quantity" : self.quantity,"price" : self.price,"stock" : self.stock,"discount" : self.discount}
        self.food_id = len(self.food)+1
        self.food[self.food_id] = self.item
        with open("food_item.json","w") as f : 
            json.dump(self.food,f)
        print("Item added successfully")

    def remove_food_items(self) : 
        for k,v in self.food.items():
            print("Food id",k,"and food items",v)
        del self.food[int(input("Enter the food id which is to be deleted"))]
        with open("food_item.json","w") as f : 
            json.dump(self.food)
        print("Item removed successfully")

    def view_food_items(self):
        for k,v in self.food.items():
            print("Food id",k,"Food items",v)

    def edit_food_items(self):
        f_id = int(input("Enter the food id to be editted"))
        for i in self.food[f_id]:
            self.foods[f_id][i] = input(f"Enter the {i} you want to update : ")
        with open("food_item.json","w") as f :
            json.dump(self.food,f)
        print("Food itens updated")

x = admin()
x.add_food_items()
x.remove_food_items()
x.view_food_items()
x.add_food_item()
x.edit_food_items()
