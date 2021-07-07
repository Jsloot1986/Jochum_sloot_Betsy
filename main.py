__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from datetime import datetime

from make_records import *
from models import *


def search(term):
    search_list = []
    query = Product.select().where(Product.product_name == term)
    for item in query:
        search_list.append(item.product_name)
    return search_list 

#print(search('Sweater'))

def list_user_products(user_id):
    user_products = []
    product_list = Product.select().join(User).where(User.id == user_id)

    for product in product_list:
        user_products.append(product.product_name)
    return user_products 

#print(list_user_products(1))


def list_products_per_tag(tag_id):
    tag_list= []
    tag_name = []
    producttags = (Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id))
    tags = (Tag.select().where(Tag.id == tag_id))

    for tag in producttags:
        tag_list.append(tag.product_name)
    for tag in tags:
        tag_name.append(tag.name)
    return tag_name, tag_list

#print(list_products_per_tag(1))


def add_product_to_catalog(user_id, product_name, price, new_quantity):
    new_product = Product.create(
        product_name=product_name,
        description= product_name,
        price_per_unit= price,
        owner= user_id,
        stock = new_quantity 
    )
    return new_product.product_name 

def update_stock(product_id, new_quantity):
    product = Product.get_by_id(product_id)
    product.stock = new_quantity
    product.save()
    return product.product_name, new_quantity 
    

#print(update_stock(1, 'sweater', 10))

    
def purchase_product(product_id, buyer_id, quantity, price):
    product = Product.get_by_id(product_id)
    new_quantity = product.stock - quantity
    if product.stock < quantity:
        raise ValueError("Amount not available in stock")
    Transaction.create(buyer=buyer_id, product_bought=product_id, amount_bought=quantity, sell_date=datetime.now(), sell_price=price)
    update_stock(product_id, new_quantity)
    return product.product_name, new_quantity 

#print(purchase_product(1, 1, 1, 90.1234))


def remove_product(product_name):
    product = Product.get(Product.product_name == product_name)
    product.delete_instance()
    print(f'the product {product_name} with product_id {product} is removed')

#print(remove_product('T-shirt'))

if __name__ == '__main__':
    create_tables()
    make_records()

    print(f'You searched for "Sweater" and this is the list {search("Sweater")}')
    print(f'The products from user_id 1 are: {list_user_products(1)} ')

    print(f'The product_list from tag_id 1 is: {list_products_per_tag(1)}')

    print(f'The new product us added {add_product_to_catalog(1, "T-shirt NY", 15.99, 20)}')
    print(f'the follow product updated {update_stock(1, 30)}')
    print(f'The follow product is sold and update in stock with {purchase_product(1, 4, 3, 155)}')

    print(remove_product("Apples"))
