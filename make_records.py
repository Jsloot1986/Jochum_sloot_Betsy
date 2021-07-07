from peewee import *

from models import *

db = SqliteDatabase('betsy_workshop.db')


def make_records():
    if not User.select().where(User.first_name == 'Jochum', User.last_name == 'Sloot'):
        User.create(
            first_name='Jochum',
            last_name='Sloot',
            street='Elandsgracht 120',
            city='Amsterdam',
            country='Nederland'
        )
    if not User.select().where(User.first_name == 'Mirjam', User.last_name == 'Sloot'):
        User.create(
            first_name='Mirjam',
            last_name='Sloot',
            street='Nieuwstraat 1',
            city='Oldemarkt',
            country='Nederland'
        )
    if not User.select().where(User.first_name == 'Sabrina', User.last_name == 'Sloot'):
        User.create(
            first_name='Sabrina',
            last_name='Sloot',
            street='Antwerpenstraat 33',
            city='Antwerpen',
            country='België'
        )
    if  not User.select().where(User.first_name == 'David', User.last_name == 'Hello'):
        User.create(
            first_name='David',
            last_name='Hello',
            street='Insulindeweg 222',
            city='Amsterdam',
            country='Nederland'
        )

    if not Tag.select().where(Tag.name == 'Clothes'):
        Tag.create(name='Clothes')
    if not Tag.select().where(Tag.name == 'Winter'):
        Tag.create(name='Winter')
    if not Tag.select().where(Tag.name == 'Domestic'):
        Tag.create(name='Domestic')
    if not Tag.select().where(Tag.name == 'Games'):
        Tag.create(name='Games')
    if not Tag.select().where(Tag.name == 'Family'):
        Tag.create(name='Family')
    if not Tag.select().where(Tag.name == 'Fruit'):
        Tag.create(name='Fruit')
    if not Tag.select().where(Tag.name == 'Healthy'):
        Tag.create(name='Healthy')
    if not Tag.select().where(Tag.name == 'Books'):
        Tag.create(name='Books')
    if not Tag.select().where(Tag.name == 'Thriller'):
        Tag.create(name='Thriller')

    user_id_1 = User.get(User.first_name == 'Jochum')
    user_id_2 = User.get(User.first_name == 'Mirjam')
    user_id_3 = User.get(User.first_name == 'Sabrina')
    user_id_4 = User.get(User.first_name == 'David')

    if not Product.select().where(Product.product_name == 'Sweater'):
        Product.create(
            product_name = 'Sweater',
            description = 'Sweater, warm and made from polyeaster',
            price_per_unit=49.99,
            owner = user_id_1,
            stock = 10
        )
    if not Product.select().where(Product.product_name == 'T-shirt'):
        Product.create(
            product_name = 'T-shirt',
            description = 'T-shirt, with Garfield',
            price_per_unit=9.99,
            owner = user_id_1,
            stock = 20
        )
    if not Product.select().where(Product.product_name == 'Trouser'):
        Product.create(
            product_name = 'Trouser',
            description = 'Trouser, Levi Jeans',
            price_per_unit=39.99,
            owner = user_id_1,
            stock = 10
        )
    if not Product.select().where(Product.product_name == 'Monopoly'):
        Product.create(
            product_name = 'Monopoly',
            description = 'Monopoly the New York edition',
            price_per_unit=29.99,
            owner=user_id_2,
            stock = 15
        )
    if not Product.select().where(Product.product_name == 'Cluedo'):
        Product.create(
            product_name = 'Cluedo',
            description = 'Cluedo the extended version',
            price_per_unit=25.99,
            owner = user_id_2,
            stock = 15
        )
    if not Product.select().where(Product.product_name == 'Apples'):
        Product.create(
            product_name = 'Apples',
            description = 'Apples, nice and sweet from Spain',
            price_per_unit=2.99,
            owner = user_id_3,
            stock = 100
        )
    if not Product.select().where(Product.product_name == 'Grapes'):
        Product.create(
            product_name = 'Grapes',
            description = 'Grapes, tasty from France',
            price_per_unit=1.99,
            owner= user_id_3,
            stock = 100
        )

    

    product_id_1 = Product.select().where(Product.product_name == 'Sweater')
    
    product_id_2 = Product.get(Product.product_name == 'T-shirt')
    
    product_id_4 = Product.get(Product.product_name == 'Monopoly')
    
    product_id_5 = Product.get(Product.product_name == 'Cluedo')
    

    
    clothes = Tag.select().where(Tag.name == 'Clothes')
    domestic = Tag.select().where(Tag.name == 'Domestic')
    winter = Tag.select().where(Tag.name == 'Winter')
    games = Tag.select().where(Tag.name == 'Games')
    family = Tag.select().where(Tag.name == 'Family')
    
    if not ProductTag.select().where(ProductTag.product == 'Sweater'):
        ProductTag.create(
            product = product_id_1,
            tags = clothes
        )
    if not ProductTag.select().where(ProductTag.product == 'T-shirt'):
        ProductTag.create(
            product = product_id_2,
            tags = clothes
        )
    if not ProductTag.select().where(ProductTag.product == 'Monopoly'):
        ProductTag.create(
            product = product_id_4,
            tags = games
        )
    if not ProductTag.select().where(ProductTag.product == 'Cluedo'):
        ProductTag.create(
            product = product_id_5,
            tags = games
        )

    if not Product.select().where(Product.product_name == 'Hotel Belagrus'):
        Product.create(
            product_name='Hotel Belagrus',
            description='Thriller/Roman about Hotel Belagrus',
            price_per_unit= 11.50,
            owner = user_id_4,
            stock= 100,
        )

    hotel_belagrus_id = Product.get(Product.product_name == "Hotel Belagrus")
    books = Tag.get(Tag.name == 'Books')
    thriller = Tag.get(Tag.name == 'Thriller')

    if not ProductTag.select().where(ProductTag.product == hotel_belagrus_id):
        ProductTag.create(product = hotel_belagrus_id, tags = books)

    

    