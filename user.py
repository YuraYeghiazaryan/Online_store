import cart


class User:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__email = ''
        self.__id = None
        self.__my_cart = cart.ShoppingCart(self.__id)
        self.__many = 1000

    def add_in_cart(self, prod):
        self.__my_cart.add_product(prod)

    def view_cart(self):
        return self.__my_cart.show_cart()

    def buy_products_in_my_cart(self):
        if self.__my_cart.by_all(self.__many):
            self.__many -= self.__my_cart.get_total_price()
            return "Բոլոր ապրանքները գնվեցին"
        return "Հաշվի գումարը բավարար չէ,գործարք կատարելու համար:)"

    def get_many(self):
        return self.__many

    def get_cart(self):
        return self.__my_cart
