import user
import product

# make some products
p1 = product.Product('Accessorise', 'Բռասլետ', 50)
p2 = product.Product('devices', 'Iphone', 200)
p3 = product.Product('Կահույք', 'դիվան', 30, 'Շատ թարմ պահած դիվան ա')

# make user object
user1 = user.User('Yura', 'Yeghiazaryan')

print("Օգտատիրոջ ընդհանուր գումարը կազմում է ", user1.get_many())

# զամբյուղի մեջ ավելացնենք ապրանքները
user1.get_cart().add_product(p1, p2)
user1.get_cart().add_product(p3)
print()

print("Զամբյուղ")
user1.view_cart()
print()

print("Զամբյուղի ապրանքների ընդհանուր գումար՝ ", user1.get_cart().get_total_price())

#  գնենք զամբյուղի բոլոր ապրանքները
print(user1.buy_products_in_my_cart())

print("հաշվի մնացորդ՝ ", user1.get_many())
