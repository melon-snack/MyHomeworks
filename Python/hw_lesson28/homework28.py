"""Homework"""
from peewee import *
import datetime

# Из-за особенности загрузки домашнего задания, просьба поменять пути для корректной работы
db = SqliteDatabase("barbershop.db")

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

# Создание БД:
# Занесение данных в таблицы:
db.connect()
db.create_tables([Masters, Services, Appointments, masters_services, appointments_services])

# Занесение данных в таблицу мастеров:
masters_data = [
    {
        "first_name": "Пётр",
        "last_name": "Сергеев",
        "middle_name": "Николаевич",
        "phone": "+7-999-999-99-99"
    },
    {
        "first_name": "Василий",
        "last_name": "Морозов",
        "middle_name": "Антонович",
        "phone": "+7-888-888-88-88"
    },
]
add_masters = Masters.bulk_create([Masters(**master) for master in masters_data])

# Занесение данных в таблицу мастеров:
services_data = [
    {
        "title": "Мужская стрижка",
        "description": "Модельная стрижка волос для мужчин, укладка со специальными средствами",
        "price": "1000",
    },
    {
        "title": "Окрашивание волос",
        "description": "Мелирование, окрашивание в один или несколько цветов, тонирование",
        "price": "3500",
    },
    {
        "title": "Стрижка бороды",
        "description": "Нанесение тонирующих лосьонов, стижка, бритьё",
        "price": "2000",
    },
    {
        "title": "Стрижка усов и бакенбард",
        "description": "Профессиональная стрижка и укладка усов",
        "price": "1000",
    },
    {
        "title": "Маникюр",
        "description": "Маникюр, обработка кутикулы, формирование ногтей, полировка ногтевой пластины, увлажнение кожи рук",
        "price": "2500",
    },
]
add_services = Services.bulk_create([Services(**service) for service in services_data])

# Занесение данных в таблицу мастеров:
appointments_data = [
    {
        "name": "Сергей",
        "phone": "+7-666-666-66-66",
        "comment": "тест коммент номер 1",
        "master_id": "1",
        "status": "выполняется",
    },
    {
        "name": "Иван",
        "phone": "+7-555-555-55-55",
        "comment": "тест коммент номер 2",
        "master_id": "2",
        "status": "ожидание мастера",
    },
    {
        "name": "Данила",
        "phone": "+7-111-111-11-11",
        "comment": "тест коммент номер 3",
        "master_id": "2",
        "status": "выполняется",
    },
]
add_appointments = Appointments.bulk_create([Appointments(**appointment) for appointment in appointments_data])

# Добавление связующих данных:
masters_services_data = [
    {
        "master_id": "1",
        "service_id": "1",
    },
    {
        "master_id": "2",
        "service_id": "2",
    },
    {
        "master_id": "1",
        "service_id": "3",
    },
    {
        "master_id": "1",
        "service_id": "4",
    },
    {
        "master_id": "2",
        "service_id": "5",
    },
]
add_masters_services = masters_services.bulk_create([masters_services(**ms_connection) for ms_connection in masters_services_data])

appointments_services_data = [
    {
        "appointment_id": "1",
        "service_id": "3",
    },
    {
        "appointment_id": "1",
        "service_id": "1",
    },
    {
        "appointment_id": "2",
        "service_id": "2",
    },
    {
        "appointment_id": "2",
        "service_id": "4",
    },
    {
        "appointment_id": "3",
        "service_id": "2",
    },
    {
        "appointment_id": "3",
        "service_id": "4",
    },
]
add_appointments_services = appointments_services.bulk_create([appointments_services(**ap_connection) for ap_connection in appointments_services_data])

# Проверка данных в БД:
print("Проверка мастеров:")
masters_show = (Masters.select())
for master in masters_show:
    print(f"Имя: {master.first_name}\n Фамилия: {master.last_name}\n Отчество: {master.middle_name}\n Телефон: {master.phone}\n")

print("Проверка сервисов:")
services_show = (Services.select())
for service in services_show:
    print(f"Название: {service.title}\n Описание: {service.description}\n Цена: {service.price}.\n")

print("Проверка записей")
appointments_show = (Appointments.select().join(Masters))
for appointment in appointments_show:
    print(f"Имя заказчика: {appointment.name}\n Телефон заказчика: {appointment.phone}\n Дата заказа: {appointment.дата}\n Комментарий: {appointment.comment}\n Статус заказа: {appointment.status}\n Мастер: {appointment.master_id.first_name} {appointment.master_id.last_name}")
