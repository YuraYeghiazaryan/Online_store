from product import Product


class ShoppingCart:
    def __init__(self, user_id):
        self.__id = user_id
        self.__products = []
        self.__total_price = 0

    def add_product(self, *args):
        for prod in args:
            if type(prod) is Product:
                self.__products.append(prod)
                self.__total_price += prod.get_price()
            else:
                return "The type of argument must be Product type"

    def del_product(self, prod):
        if prod in self.__products:
            self.__products.remove(prod)
            self.__total_price -= prod.get_price()
        else:
            return "The product is not in the cart"

    def show_cart(self):
        for prod in self.__products:
            print(prod.get_all_features())

    def by_all(self, many):
        if many >= self.__total_price:
            self.__products = []
            return self.__total_price
        return False

    def get_total_price(self):
        return self.__total_price
