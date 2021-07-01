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
    if User.select().where(User.first_name == 'Jochum', User.last_name == 'Sloot').exists():
        None
    else:
        User.create(
            first_name='Jochum',
            last_name='Sloot',
            street='Elandsgracht 120',
            city='Amsterdam',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Mirjam', User.last_name == 'Sloot').exists():
        None
    else:
        User.create(
            first_name='Mirjam',
            last_name='Sloot',
            street='Nieuwstraat 1',
            city='Oldemarkt',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Sabrina', User.last_name == 'Sloot').exists():
        None
    else:
        User.create(
            first_name='Sabrina',
            last_name='Sloot',
            street='Antwerpenstraat 33',
            city='Antwerpen',
            country='België'
        )
    if User.select().where(User.first_name == 'David', User.last_name == 'Hello').exists():
        None
    else:
        User.create(
            first_name='David',
            last_name='Hello',
            street='Insulindeweg 222',
            city='Amsterdam',
            country='Nederland'
        )

    if Tag.select().where(Tag.name == 'Clothes').exists():
        None
    else:
        Tag.create(name='Clothes')
    if Tag.select().where(Tag.name == 'Winter').exists():
        None
    else:
        Tag.create(name='Winter')
    if Tag.select().where(Tag.name == 'Domestic').exists():
        None
    else:
        Tag.create(name='Domestic')
    if Tag.select().where(Tag.name == 'Games').exists():
        None
    else:
        Tag.create(name='Games')
    if Tag.select().where(Tag.name == 'Family').exists():
        None
    else:
        Tag.create(name='Family')
    if Tag.select().where(Tag.name == 'Fruit').exists():
        None
    else:
        Tag.create(name='Fruit')
    if Tag.select().where(Tag.name == 'Healthy').exists():
        None
    else:
        Tag.create(name='Healthy')
    if Tag.select().where(Tag.name == 'Book').exists():
        None
    else:
        Tag.create(name='Book')
    if Tag.select().where(Tag.name == 'Thriller').exists():
        None
    else:
        Tag.create(name='Thriller')
    if Product.select().where(Product.product_name == 'Sweater').exists():
        None
    else:
        Product.create(
            product_name = 'Sweater',
            description = 'Sweater, warm and made from polyeaster',
            price_per_unit=49.999,
            tags = [],
            number = 10,
            catalog_id= 1
        )
    if Product.select().where(Product.product_name == 'T-shirt').exists():
        None
    else:
        Product.create(
            product_name = 'T-shirt',
            description = 'T-shirt, with Garfield',
            price_per_unit=9.999,
            tags = [],
            number = 20,
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Trouser').exists():
        None
    else:
        Product.create(
            product_name = 'Trouser',
            description = 'Trouser, Levi Jeans',
            price_per_unit=39.999,
            tags = [],
            number = 10,
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Monopoly').exists():
        None
    else:
        Product.create(
            product_name = 'Monopoly',
            description = 'Monopoly the New York edition',
            price_per_unit=29.999,
            tags = [],
            number = 15,
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Cluedo').exists():
        None
    else:
        Product.create(
            product_name = 'Cluedo',
            description = 'Cluedo the extended version',
            price_per_unit=25.999,
            tags = [],
            number = 15,
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Apples').exists():
        None
    else:
        Product.create(
            product_name = 'Apples',
            description = 'Apples, nice and sweet from Spain',
            price_per_unit=2.995,
            tags = [],
            number = 100,
            catalog_id = 1
        )
    if Product.select().where(Product.product_name == 'Grapes').exists():
        None
    else:
        Product.create(
            product_name = 'Grapes',
            description = 'Grapes, tasty from France',
            price_per_unit=1.999,
            tags= [],
            number = 100,
            catalog_id = 1
        )

    user_id_1 = User.get(User.first_name == 'Jochum')
    user_id_2 = User.get(User.first_name == 'Mirjam')
    user_id_3 = User.get(User.first_name == 'Sabrina')
    user_id_4 = User.get(User.first_name == 'David')

    product_id_1 = Product.get(Product.product_name == 'Sweater')
    product_id_2 = Product.get(Product.product_name == 'T-shirt')
    product_id_3 = Product.get(Product.product_name == 'Monopoly')
    product_id_4 = Product.get(Product.product_name == 'Cluedo')
    
    if UserProduct.select().where(UserProduct.user_id == user_id_1).exists():#tevens geprobeerd met user_id_1 alleen krijg ik een foutmelding
        None
    else:
        UserProduct.create(user_id= user_id_1, product_id= product_id_1)
        UserProduct.create(user_id= user_id_1, product_id= product_id_2)
    if UserProduct.select().where(UserProduct.user_id == user_id_2).exists(): #zelfde als bij user.id 1 fout melding is Params: ['Mirjam', 1, 0]
        None
    else:
        UserProduct.create(user_id= user_id_2, product_id= product_id_3)
        UserProduct.create(user_id= user_id_2, product_id= product_id_4)

    if Product.select().where(Product.product_name == 'Hotel Belagrus').exists():
        None
    else:
        Product.create(
            product_name='Hotel Belagrus',
            description='Thriller/Roman about Hotel Belagrus',
            price_per_unit= 11.50,
            tags=[],
            number= 100,
            catalog_id=1
        )

    hotel_belagrus_id = Product.get(Product.product_name == "Hotel Belagrus")

    if UserProduct.select().where(UserProduct.user_id == user_id_4, UserProduct.product_id == hotel_belagrus_id).exists():
        None
    else:
        UserProduct.create(user_id= user_id_4, product_id=hotel_belagrus_id)

    

    