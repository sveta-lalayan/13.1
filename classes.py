from abc import ABC, abstractmethod


class MixinRepr:

    def __init__(self, *args, **kwargs):
        print(self.__repr__())

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.__dict__}'


class AbstractCategoryOrder(ABC):
    """Это абстрактный класс для категорий и заказов"""

    product = str
    quantity = int

    @abstractmethod
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def get_total_cost(self):
        pass


class Order(AbstractCategoryOrder):
    """Это класс для заказа"""

    def __init__(self, product, quantity):
        super().__init__(product, quantity)

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_total_cost(self):
        return self.product * self.quantity


class Category(AbstractCategoryOrder):
    """Это класс для категории"""

    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods, product):
        self.name = name
        self.description = description
        self.__goods = goods
        super().__init__(name, product)

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    @property
    def goods(self):
        return self.__goods

    def add_goods(self, product):
        if isinstance(product, self.__class__) and isinstance(self, product.__class__):
            if product.quantity < 1:
                raise ValueError("Товар с нулевым количеством не может быть добавлен")
            self.__goods.append(product)
        else:
            raise TypeError

    @property
    def get_product(self):
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        product_counter = 0
        for product in self.__goods:
            product_counter += product.quantity
        return product_counter

    def __str__(self):
        return f'Название категории {self.name}, количество продуктов: {len(self)} шт.'

    def get_total_cost(self):
        return self.product * self.quantity

    def middle_price(self, sum_of_price=None):
        for product in self.__goods:
            sum_of_price += product.price
        try:
            return sum_of_price / len(self.__goods)
        except ZeroDivisionError:
            return 0


class ProductExceptions:

    def __init__(self, name, goods, product):
        super().__init__(name, goods, product)


class AbstractProduct(ABC):

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def get_product_price(self):
        pass

    @classmethod
    @abstractmethod
    def add_new_product(cls, product_data, list_of_products=None):
        pass


class Product(MixinRepr, AbstractProduct):
    """Классы продуктов"""
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
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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
        return self.price

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

        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if isinstance(other, self.__class__) and isinstance(self, other.__class__):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError


class Smartphone(Product):
    performance: float
    model: str
    ram: float

    def __init__(self, name, description, price, quantity, performance, model, ram, color):
        self.performance = performance
        self.model = model
        self.ram = ram
        super().__init__(name, description, price, quantity, color)


class LawnGrass(Product):
    """Класс газонной травы"""
    country_origin: str
    germination_period: str

    def __init__(self, name, description, price, quantity, country_origin, germination_period, color):
        self.country_origin = country_origin
        self.germination_period = germination_period
        super().__init__(name, description, price, quantity, color)