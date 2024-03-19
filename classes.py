class Category:
    total_amount_of_categories = 0
    amount_of_unique_goods = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods


        Category.total_amount_of_categories += 1
        Category.amount_of_unique_goods += len(self.goods)


    @property
    def goods(self):
        return self.__goods

    def add_goods(self, product):
        self.__goods.append(product)



    @property
    def get_product(self):
        the_current_list = []
        for product in self.__goods:
            the_current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity}')
            return the_current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.goods})'





class Products:

    def __init__(self,product_name: str, product_description: str, price: float, quantity: int):
        self.product_name = product_name
        self.product_description = product_description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Введенная цена некорректная')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена не изменилась')
        else:
            self.__price = new_price

    def get_product_price(self):
        return self.price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        if list_of_products:
            for product in list_of_products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price

                    return product

        new_product = cls(name, description, price, quantity)
        return new_product
