from peewee import *

from models import *

db = SqliteDatabase('betsy_workshop.db')

def add_tag(product, tag_name):
    tag = Tag.get(Tag.name == tag_name)
    if tag in product.tags:
        None
    else:
        product.tags.add([tag])

def make_records():
    if User.select().where(User.first_name == 'Jochum' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Jochum',
            last_name='Sloot',
            street='Elandsgracht 120',
            city='Amsterdam',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Mirjam' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Mirjam',
            last_name='Sloot',
            street='Nieuwstraat 1',
            city='Oldemarkt',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Sabrina' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Sabrina',
            last_name='Sloot',
            street='Antwerpenstraat 33',
            city='Antwerpen',
            country='België'
        )
    if User.select().where(User.first_name == 'David' and User.last_name == 'Hello'):
        None
    else:
        User.create(
            first_name='David',
            last_name='Hello',
            street='Insulindeweg 222',
            city='Amsterdam',
            country='Nederland'
        )

    if Tag.select().where(Tag.name == 'Clothes'):
        None
    else:
        Tag.create(name='Clothes')
    if Tag.select().where(Tag.name == 'Winter'):
        None
    else:
        Tag.create(name='Winter')
    if Tag.select().where(Tag.name == 'Domestic'):
        None
    else:
        Tag.create(name='Domestic')
    if Tag.select().where(Tag.name == 'Games'):
        None
    else:
        Tag.create(name='Games')
    if Tag.select().where(Tag.name == 'Family'):
        None
    else:
        Tag.create(name='Family')
    if Tag.select().where(Tag.name == 'Fruit'):
        None
    else:
        Tag.create(name='Fruit')
    if Tag.select().where(Tag.name == 'Healthy'):
        None
    else:
        Tag.create(name='Healthy')
    if Tag.select().where(Tag.name == 'Book'):
        None
    else:
        Tag.create(name='Book')
    if Tag.select().where(Tag.name == 'Thriller'):
        None
    else:
        Tag.create(name='Thriller')
    if Product.select().where(Product.product_name == 'Sweater'):
        None
    else:
        Product.create(
            product_name = 'Sweater',
            description = 'Sweater, warm and made from polyeaster',
            price_per_unit=49.999,
            tags = [],
            catalog_id= 1
        )
    if Product.select().where(Product.product_name == 'T-shirt'):
        None
    else:
        Product.create(
            product_name = 'T-shirt',
            description = 'T-shirt, with Garfield',
            price_per_unit=9.999,
            tags = [],
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Trouser'):
        None
    else:
        Product.create(
            product_name = 'Trouser',
            description = 'Trouser, Levi Jeans',
            price_per_unit=39.999,
            tags = [],
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Monopoly'):
        None
    else:
        Product.create(
            product_name = 'Monopoly',
            description = 'Monopoly the New York edition',
            price_per_unit=29.999,
            tags = [],
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Cluedo'):
        None
    else:
        Product.create(
            product_name = 'Cluedo',
            description = 'Cluedo the extended version',
            price_per_unit=25.999,
            tags = [],
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Apples'):
        None
    else:
        Product.create(
            product_name = 'Apples',
            description = 'Apples, nice and sweet from Spain',
            price_per_unit=2.995,
            tags = [],
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Grapes'):
        None
    else:
        Product.create(
            product_name = 'Grapes',
            description = 'Grapes, tasty from France',
            price_per_unit=1.999,
            tags= [],
            catalog_id = 1
        )

    if UserProduct.select().where(UserProduct.user_id == 1):
        None
    else:
        UserProduct.create(user_id= 1, product_id= 1, number=2)
        UserProduct.create(user_id= 1, product_id= 2, number=5)
    if UserProduct.select().where(UserProduct.user_id == 2):
        None
    else:
        UserProduct.create(user_id= 2, product_id= 3, number=2)
        UserProduct.create(user_id= 2, product_id= 4, number=4)

    if Product.select().where(Product.product_name == 'Hotel Belagrus'):
        None
    else:
        Product.create(
            product_name='Hotel Belagrus',
            description='Thriller/Roman about Hotel Belagrus',
            price_per_unit= 11.50,
            number= 100,
            tags=[],
            catalog_id=1
        )

    hotel_belagrus_id = Product.get(Product.product_name == "Hotel Belagrus")

    if UserProduct.select().where(UserProduct.user_id == 4 and UserProduct.product_id == hotel_belagrus_id):
        None
    else:
        UserProduct.create(user_id= 4, product_id=hotel_belagrus_id, number=100)

    

    