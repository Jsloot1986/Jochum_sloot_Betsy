__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from datetime import datetime

from make_records import *
from models import *


def search(term) -> list[Product]:
    search_list = []
    query = Product.select().where(Product.product_name == term)
    for item in query:
        search_list.append(item.product_name)
    return search_list

#print(search('Sweater'))

def list_user_products(user_id) -> list[UserProduct]:
    user_products = []
    product_list = Product.select().join(UserProduct).join(User).where(User.id == user_id)

    for product in product_list:
        user_products.append(product.product_name)
    return user_products

#print(list_user_products(1))


def list_products_per_tag(tag_id) -> list[Tag.name]:
    tag_list = []
    query = ProductTag.select().join(Product).switch(ProductTag).join(Tag).where(Tag.id == tag_id)

    for tag in query:
        tag_list.append(tag)
    return tag_list

#print(list_products_per_tag(1))


def update_stock(user_id, product_name, new_quantity) -> None:
    update_product =[]
    try:
        record = UserProduct.select().join(Product).where(Product.product_name == product_name and UserProduct.user_id == user_id)
        user_product = UserProduct.get(UserProduct.user_id == record['user_id'], UserProduct.product_id == record['product_id'])
        product_number = Product.get(Product.product_name == product_name)
        product_number.number = new_quantity
        product_number.sace()
        user_product.save()
        update_product.append([user_product.id, product_number.number])
    except:
        print("No record found")
    return update_product

#print(update_stock(1, 'sweater', 10))



def add_product_to_catalog(user_id, product_name, new_quantity) -> None:
    try:
        record = UserProduct.select().join(Product).where(Product.product_name == product_name and UserProduct.user_id == user_id)
        existing_record = "Y"
        return record
    except:
        existing_record = "N"
    if existing_record == "N":
        try:
            product_id_arr = Product.select(Product.id).where(Product.product_name == product_name)
            UserProduct.create(user_id=user_id, product_id=product_id_arr['id'])
            product_id_arr.number = new_quantity
            product_id_arr.save()
            print(product_id_arr)
        except:
            print("Either the product or the user_id doesn't exist yet")

#print(add_product_to_catalog(2, 'orange', 10))

    
def purchase_product(product_id, buyer_id, quantity, price) -> None:
    try:
        user_product = UserProduct.get(UserProduct.user_id == buyer_id and UserProduct.product_id == product_id)
        product_number = Product.get(Product.product_name == product_id)
        if product_number.number >= quantity:
            Transaction.create(user_id=buyer_id, product_id=product_id, number=quantity, sell_date=datetime.now(), sell_price=price)
            product_number.number = product_number.number-quantity
            user_product.save()
            product_number.save()
            print(user_product, product_number)
        else:
            raise ValueError("not enough goods in stock")
    except ValueError as ve:
        print(ve)
    except:
        print(f"No record in user product with values user_id {str(buyer_id)} and product_id {str(product_id)}")

#print(purchase_product(1, 1, 1, 90.1234))


def remove_product(product_name) -> None:
    product = Product.get(Product.product_name == product_name)
    print(product)
    product.delete_instance()

#print(remove_product('T-shirt'))

create_tables()

make_records()

chosen_product = search("Sweater")
for product in chosen_product:
    print(f"products: {product} ")

query = list_user_products(1)
for product in query:
    print=(f"list_user_products {product.__repr__()}")


query = list_products_per_tag(1)
for tag in query:
    print(f"list with tag id 1: {tag}")

print("update product in user catlog")

update_stock(1, "sweater", 30)
purchase_product(1, 1, 1, 90.1234)

remove_product("Apples")
