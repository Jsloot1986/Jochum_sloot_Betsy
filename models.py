from enum import unique
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
    name = CharField(unique=True)

class Product(BaseModel):
    product_name = CharField(max_length= 50, null=False)
    description = CharField(max_length= 50)
    price_per_unit = DecimalField(
        constraints=[Check("price_per_unit >= 0")],
        decimal_places=2,
        auto_round=True,
        null=False,
        default=0,
        max_digits=10)
    owner = ForeignKeyField(User, backref="products")
    stock = IntegerField(default=1)

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    product_bought = ForeignKeyField(Product, backref='transactions')
    amount_bought = IntegerField()
    sell_date = DateField()
    sell_price = DecimalField(
        constraints=[Check("sell_price >= 0")],
        decimal_places=2,
        auto_round=True,
        null=False,
        default=0,
        max_digits=10
    )

class ProductTag(BaseModel): 
    product = ForeignKeyField(Product, index=True, backref="products")
    tags = ForeignKeyField(Tag, index=True, backref="tags")

def create_tables():
    with db:
        db.create_tables(
            [User, Product, Tag, ProductTag, Transaction]
        )

       