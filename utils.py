class Category:
    total_amount_of_categories = 0
    amount_of_unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = str(name)
        self.description = str(description)
        self.goods = list(goods)
        self.total_amount_of_categories = 1

        Category.total_amount_of_categories += 1


class Products:

    def __init__(self,product_name, product_description, price, quantity):
        self.product_name = product_name
        self.product_description = product_description
        self.price = float(price)
        self.quantity = quantity


#i1 = Category('orange', 'beautiful', ["blankets, cushions"])
#print(i1.goods)

#p2 = Products("cushions", "soft", 2000, 3)
#print(p2.price)