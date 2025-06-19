"""Homework"""
from peewee import *
import datetime

# Из-за особенности загрузки домашнего задания, просьба поменять пути для корректной работы
db = SqliteDatabase("non_git\\homework\\barbershop.db")

# Модель таблицы мастеров:
class Masters(Model):
    first_name = CharField(max_length=50, null=False)
    middle_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=False)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        database = db

# Модель таблицы сервисов:
class Services(Model):
    title = CharField(max_length=100, unique=True)
    description = TextField()
    price = DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        database = db

# Модель таблицы записей:
class Appointments(Model):
    name = CharField(max_length=100, null=False)
    phone = CharField(max_length=20, null=False)
    дата = DateTimeField(default=datetime.datetime.now)
    comment = TextField()
    status = CharField(max_length=20, default="записана")
    master_id = ForeignKeyField(Masters, backref="appointments", on_delete="CASCADE")

    class Meta:
        database = db

# Модель таблицы объединения таблиц мастеров и сервисов:
class masters_services(Model):
    master_id = ForeignKeyField(Masters, backref="masters_services", on_delete="CASCADE")
    service_id = ForeignKeyField(Services, backref="masters_services", on_delete="CASCADE")

    class Meta:
        database = db
        indexes = (
            (("master_id",), False),
            (("service_id",), False),
        )

# Модель таблицы объединения таблиц записей и сервисов:
class appointments_services(Model):
    appointment_id = ForeignKeyField(Appointments, backref="appointments_services", on_delete="CASCADE")
    service_id = ForeignKeyField(Services, backref="appointments_services", on_delete="CASCADE")

    class Meta:
        database = db
        indexes = (
            (("appointment_id",), False),
            (("service_id",), False),
        )
