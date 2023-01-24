class Product:
    def __init__(self, categories, name, price, description=''):
        # self.__allowed_categories = {'Accessorise': Accessorise, 'Devices': Devices, 'Clothes': Clothes,
        #                              'Furniture': Furniture}
        self.__categories = categories
        self.__name = name
        self.__price = price
        self.__description = description

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_categories(self):
        return self.__categories

    def get_all_features(self):
        return self.__name, self.__categories, self.__price, self.__description

    # def make_prod_obj(self, categories, name, price):
    #     if self.categories is not None:
    #         return categories(categories, name, price)
    #     return None
    #
    # def allowed_categories(self, categories):
    #     if categories in self.__allowed_categories:
    #         return self.__allowed_categories[categories]
    #     return None
    #
    # def set_product_features(self, *args):
    #     for i in args:
    #         self.features.append(i)


# class Accessorise(Product):
#     def __init__(self, categories, name, price):
#         self.description = {'name': None, 'price': None}
#         self.set_description(name, price)
#
#     def set_description(self, name, price):
#         self.description['name'] = name
#         self.description['price'] = price
#
#
# class Devices(Product):
#     def __init__(self, categories, name, price):
#         self.description = {'name': None, 'price': None}
#         self.set_description(name, price)
#
#     def set_description(self, name, price):
#         self.description['name'] = name
#         self.description['price'] = price
#
#
# class Clothes(Product):
#     def __init__(self, categories, name, price):
#         self.description = {'name': None, 'price': None}
#         self.set_description(name, price)
#
#     def set_description(self, name, price):
#         self.description['name'] = name
#         self.description['price'] = price
#
#
# class Furniture(Product):
#     def __init__(self, categories, name, price):
#         self.description = {'name': None, 'price': None}
#         self.set_description(name, price)
#
#     def set_description(self, name, price):
#         self.description['name'] = name
#         self.description['price'] = price
