-- Homework
-- Отключение проверки внешних ключей
PRAGMA foreign_keys = OFF;

-- Начало транзакции
BEGIN TRANSACTION;

-- Создание таблицы мастеров
CREATE TABLE IF NOT EXISTS Masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    middle_name TEXT,
    phone TEXT
);

-- Создание таблицы услуг
CREATE TABLE IF NOT EXISTS Services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    description TEXT,
    price INTEGER
);

-- Создание таблицы записи на услуги
CREATE TABLE IF NOT EXISTS Appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    дата DATE DEFAULT CURRENT_TIMESTAMP,
    comment TEXT,
    master_id INTEGER DEFAULT NULL,
    status TEXT DEFAULT "записана",
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE SET DEFAULT ON UPDATE CASCADE
);

-- Связующие таблицы
-- Таблица для связи мастеров и услуг
CREATE TABLE IF NOT EXISTS masters_services (
    master_id INTEGER DEFAULT NULL,
    service_id INTEGER DEFAULT NULL,
    FOREIGN KEY (master_id) REFERENCES Masters(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    PRIMARY KEY (master_id, service_id)
);

-- Таблица для связи записей и услуг
CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER DEFAULT NULL,
    service_id INTEGER DEFAULT NULL,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    PRIMARY KEY (appointment_id, service_id)
);

-- Добавление индексов
-- Индекс связи мастеров и услуг - Ускорение поиска по названию мастера и услуги
CREATE INDEX masters_services_idx ON masters_services (master_id, service_id);

-- Индекс связи записей и услуг - Ускорение поиска по записи или услуге
CREATE INDEX appointments_services_idx ON appointments_services (appointment_id, service_id);

-- Ускорение поиска по имени мастера
CREATE INDEX appointments_idx ON Appointments (master_id);

-- Ускорение поиска по названию услуги
CREATE INDEX services_idx ON Services (title);


-- Внесение данных
-- Данные о мастерах
INSERT INTO Masters (first_name, last_name, middle_name, phone)
VALUES
('Пётр', 'Сергеев', 'Николаевич', '+7-999-999-99-99'),
('Василий', 'Морозов', 'Антонович', '+7-888-888-88-88');

-- Данные об услугах
INSERT INTO Services (title, description, price)
VALUES
('Мужская стрижка', 'Модельная стрижка волос для мужчин, укладка со специальными средствами', '1000'),
('Окрашивание волос', 'Мелирование, окрашивание в один или несколько цветов, тонирование', '3500'),
('Стрижка бороды', 'Нанесение тонирующих лосьонов, стижка, бритьё', '2000'),
('Стрижка усов и бакенбард', 'Профессиональная стрижка и укладка усов', '1000'),
('Маникюр', 'Маникюр, обработка кутикулы, формирование ногтей, полировка ногтевой пластины, увлажнение кожи рук', '2500');

-- Связывание мастеров и услуг
INSERT INTO masters_services (master_id, service_id)
VALUES
(1, 1),
(2, 2),
(1, 3),
(1, 4),
(2, 5);

-- Добавление записей
INSERT INTO Appointments (name, phone, comment, master_id, status)
VALUES
('Сергей', '+7-666-666-66-66', "тест коммент номер 1", 1, 'выполняется'),
('Иван', '+7-555-555-55-55', "тест коммент номер 2", 2, 'ожидание мастера'),
('Антон', '+7-222-222-22-22', "тест коммент номер 3", 1, 'ожидание мастера'),
('Данила', '+7-111-111-11-11', "тест коммент номер 4", 2, 'выполняется');

-- Связывание записей и услуг
INSERT INTO appointments_services (appointment_id, service_id)
VALUES
(1, 3),
(2, 2),
(3, 1),
(4, 2);

COMMIT;

PRAGMA foreign_keys = ON;