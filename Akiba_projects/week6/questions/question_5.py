print("====================================================")
print(" Question 5: OOP Methods and Object Relationships")
print("====================================================")


class Product:
    store_name = "BanG"
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def display_product(self):
        print("Product Info: ")
        print("\n Store name: ", Product.store_name)
        print("product name: ", self.name)
        print("Price: ", self.price)

    @classmethod        
    def change_store_name(cls, new_name):
        cls.store_name = new_name
        new_name = "BG"
        print("New store name: ", new_name)
        
    @staticmethod
    def is_valid_price(price):
        return price > 0
    
    
product1 = Product("Computer", 70000)
product2 = Product("phone", 45000)

product1.display_product()
product1.is_valid_price()
product1.change_store_name()
product2.display_product()
product2.is_valid_price()


class Shopping_cart:
    def __init__(self):
        self.product_list = []
    
    def add_product(self, product):
        self.product_list.append(product)
        
    def calculate_total(self):
        total_price = 0
        for product in self.product_list:
            total_price += product.price
        return total_price
    
    def display_cart(self):
        for product in self.product_list:
            print("product name: ", product.name, "price= ", product.price)
            print("total price= ", self.calculate_total())
     
        
cart1 = Shopping_cart()

cart1.add_product("Computer")
cart1.calculate_total()
cart1.display_cart()
