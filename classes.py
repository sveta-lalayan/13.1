class Category:
    total_amount_of_categories = 0
    amount_of_unique_goods = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods


        Category.total_amount_of_categories += 1
        Category.amount_of_unique_goods += len(self.goods)


class Products:

    def __init__(self,product_name: str, product_description: str, price: float, quantity: int):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity


#i1 = Category('orange', 'beautiful', ["blankets, cushions"])
#print(i1.goods)

#p2 = Products("cushions", "soft", 2000, 3)
#print(p2.price)