class Category:
    name: str
    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    @property
    def goods(self):
        return self.__goods

    def add_goods(self, product):
        """Добавляет данные с приватного атрибута __goods"""
        if isinstance(product, self.__class__) and isinstance(self, product.__class__):
            self.__goods.append(product)
        raise TypeError

    @property
    def get_product(self):
        """Получает имя, цену и остаток"""
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        """ Подсчитывает кол-во продуктов в категории"""
        product_counter = 0
        for product in self.__goods:
            product_counter += product.quantity
        return product_counter

    def __str__(self):
        """ Выводит кол-во продуктов"""
        return f'Название категории {self.name}, количество продуктов: {len(self)} шт.'


class Product:
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @property
    def price(self):
        """Получает приватные данные через getter"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Условия изменения цены"""
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')
        else:
            self.__price = new_price

    def get_product_price(self):
        """Получает приватный атрибут price"""
        return self.price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        color = product_data

        if list_of_products:
            for product in list_of_products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price

                    return product


        new_product = cls(name, description, price, quantity, color)
        return new_product

    def __str__(self):
        """ Строково отображает остаток продукта на складе """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ складывает сумму продуктов """
        if isinstance(other, self.__class__) and isinstance(self, other.__class__):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError


class Smartphone(Product):

    performance: float
    model: str
    ram: float

    def __init__(self, name, description, price, quantity, performance, model, ram, color):
        super().__init__(name, description, price, quantity, color)

        self.performance = performance
        self.model = model
        self.ram = ram


class LawnGrass(Product):
    country_origin: str
    germination_period: str

    def __init__(self, name, description, price, quantity, country_origin, germination_period, color):
        super().__init__(name, description, price, quantity, color)
        self.country_origin = country_origin
        self.germination_period = germination_period