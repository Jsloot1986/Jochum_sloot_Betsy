from peewee import ManyToManyField, Model, SqliteDatabase, IntegerField, AutoField, DateField, CharField, DecimalField, ForeignKeyField, Check

db = SqliteDatabase('betsy_workshop.db', pragmas={"foreign_keys": 1})

class BaseModel(Model):
    class Meta:
        database = db
#if no primary key is defined an implicit primary key is added

class User(BaseModel):
    first_name = CharField()
    last_name = CharField()
    street = CharField()
    city = CharField()
    country = CharField()

class Tag(BaseModel):
    name = CharField()

class Product(BaseModel):
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(8, 2, True)
    tags = ManyToManyField(Tag)

class UserProduct(BaseModel):
    user_id = ForeignKeyField(User, backref="userproducts")
    product_id = ForeignKeyField(Product, backref="userproducts")
    number = IntegerField(constraints=[Check('number>=0')])

class Transaction(BaseModel):
    user_id = ForeignKeyField(User, backref='transactions')
    product_id = ForeignKeyField(Product, backref='transactions')
    number = IntegerField(constraints=[Check('number>0')])
    sell_date = DateField()
    sell_price = DecimalField(8, 2, True)

ProductTag = Product.tags.get_through_model()

def create_tables():
    with db:
        db.create_tables(
            [User, UserProduct, Product, Tag, ProductTag, Transaction]
        )

       