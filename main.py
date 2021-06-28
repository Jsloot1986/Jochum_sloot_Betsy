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
        record = UserProduct.select().join(Product).where(Product.product_name == product_name and UserProduct.user_id == user_id).dicts()[1]
        user_product = UserProduct.get(UserProduct.user_id == record['user_id'], UserProduct.product_id == record['product_id'])
        user_product.number = new_quantity
        user_product.save()
        update_product.append([user_product.id, user_product.number])
    except:
        print("No record found")
    return update_product

#print(update_stock(1, 'sweater', 10))



def add_product_to_catalog(user_id, product_name, new_quantity) -> None:
    try:
        record = UserProduct.select().join(Product).where(Product.product_name == product_name and UserProduct.user_id == user_id).dicts()[0]
        existing_record = "Y"
        return record
    except:
        existing_record = "N"
    if existing_record == "N":
        try:
            product_id_arr = Product.select(Product.id).where(Product.product_name == product_name).dicts()[0]
            UserProduct.create(user_id=user_id, product_id=product_id_arr['id'], number=new_quantity)
            print(product_id_arr)
        except:
            print("Either the product or the user_id doesn't exist yet")

#print(add_product_to_catalog(2, 'orange', 10))

    
def purchase_product(product_id, buyer_id, quantity, price) -> None:
    try:
        user_product = UserProduct.get(UserProduct.user_id == buyer_id and UserProduct.product_id == product_id)
        if user_product.number >= quantity:
            Transaction.create(user_id=buyer_id, product_id=product_id, number=quantity, sell_date=datetime.now(), sell_price=price)
            user_product.number = user_product.number-quantity
            user_product.save()
            print(user_product)
        else:
            raise ValueError("not enough goods in stock")
    except ValueError as ve:
        print(ve)
    except:
        print(f"No record in user product with values user_id {str(buyer_id)} and product id {str(product_id)}")

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
    print("product "+product.product_name)

query = list_user_products(1)
#print(f"the query is: {query}")
for product in query.dicts():
    print=("list_user_products "+ product.__repr__())


query = list_products_per_tag(1)
print("the next one is a list of products with tag id 1")

for tag in query.dicts():
    print(tag)

print("update product in user catlog")

update_stock(1, "sweater", 30)
purchase_product(67, 1, 1, 90.1234)

remove_product("Apples")
