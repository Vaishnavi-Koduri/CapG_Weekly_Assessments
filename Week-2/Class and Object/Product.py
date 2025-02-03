class Product:
    def __init__(self,prod_name,prod_price,stock,quantity):
        self.prod_name= prod_name
        self.prod_price= prod_price
        self.stock= stock
        self.quantity= quantity
        print(f"Item required: {self.prod_name}, item price: {self.prod_price}, Stock left: {self.stock}, Quantity asked: {self.quantity}")

    def check_availability(self):
        if self.stock>self.quantity:
            print("The requested quantity is Available and In Stock ")
        else:
            print("Out of Stock")

product= Product("Pen",20,18,21)
product.check_availability()